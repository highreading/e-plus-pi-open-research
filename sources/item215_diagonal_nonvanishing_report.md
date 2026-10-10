> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 215 — 2-adic candidate classification and algebraic structure of the diagonal anchor

Date: 2026-08-31

## 1. Scope and verdict

Item 210 reduced a rationally singular endpoint-weight band to the vanishing
of the explicit integer



$$
\ell_j=[y^{2j+1}]\frac{(y-1)^{3j+2}}{(1+y^2)^{2j+2}},\qquad j\ge1. \tag{1.1}
$$



This item asks whether $\ell_j\ne0$ can be proved for every $j$.  It
does not infer an all-$j$ statement from the finite scan through
$20{,}000$.

The outcome is:

**PROVED — exact 2-adic candidate theorem.**  There is an explicit finite
sum



$$
\ell_j=(-1)^j\sum_{k=0}^{2j+1}(-1)^k2^k
 {2j+1+k\choose k}{3j+2+k\choose2j+1-k}.             \tag{1.2}
$$



Let $\nu_j(k)$ be the 2-adic valuation of the unsigned $k$-th
summand.  If the minimum of $\nu_j(k)$ is attained at one $k$, then



$$
v_2(\ell_j)=\min_k\nu_j(k)<\infty. \tag{1.3}
$$



Consequently, every possible zero lies in the precisely defined class on
which the minimum is tied.  Deciding membership requires only finitely
many binary carry calculations: since $\nu_j(k)\ge k$, no
$k>\nu_j(0)$ can minimize.

**PROVED — a uniform infinite nonvanishing family.**  For every $j$,



$$
\ell_j\equiv(-1)^j{3j+2\choose j+1}\pmod4.          \tag{1.4}
$$



The binomial coefficient on the right is always even.  If its Kummer
carry count is exactly one, then



$$
v_2(\ell_j)=1.              \tag{1.5}
$$



This is an all-$j$, binary-language theorem, not a scan.  It includes,
for example, the infinite families $j=2^r-1$ for $r\ge1$ and
$j=2^r$ for $r\ge2$.

**PROVED — an exact algebraic ordinary generating function.**  Put



$$
A(z)=\sum_{j\ge0}\ell_jz^j. \tag{1.6}
$$



There is a unique algebraic series $H(z)$, with $H(0)=1$, such that



$$
A(z)=\frac{H'(z)}{H(z)}      \tag{1.7}
$$



and $G(z,H)=0$, where the compact exact polynomial $G$ is displayed
in Section 4.  This makes prime-power automata available in principle,
but does not itself prove nonvanishing.

**PROVED — a stronger global ceiling.**  The order-three recurrence from
Item 210 forbids three consecutive zeros.  Applying that spacing theorem,
rather than charging every unresolved band, improves the rank-one
singular-band ceiling from



$$
0.0000333316667499958\ldots
 \quad\hbox{to}\quad
 0.0000222233329074879\ldots\quad\hbox{per }m.       \tag{1.8}
$$



The corresponding bound is



$$
0.00000370388881791465\ldots\quad\hbox{per }6m.     \tag{1.9}
$$



This remains far below the required
$0.117797902016590763\ldots$ per $m$, or
$G=0.0196329836694317938\ldots$ per $6m$.

**EXPERIMENTAL / FINITE EXACT.**  The Item 210 recurrence replay again proves
$\ell_j\ne0$ for $1\le j\le20{,}000$.  On this prefix, 16,029
indices have a unique 2-adic minimum and 3,971 have a tied minimum.  This
profile is evidence about the candidate theorem, not a density theorem.

**OPEN.**  Nonvanishing on the tied-minimum class is not proved.  Thus
Item 215 does not prove $\ell_j\ne0$ for all $j$, does not reduce the
singular-band rate literally to zero, and does not create a new valuation
copy for Route 1.

## 2. The exact 2-adic expansion

Set



$$
A_0=3j+2,\qquad K=2j+2,\qquad n=2j+1.
$$



The identity



$$
1+y^2=(1-y)^2+2y            \tag{2.1}
$$



gives, as a formal power series,



$$
\begin{aligned}
 \frac{(y-1)^{A_0}}{(1+y^2)^K}
 &=(-1)^j(1-y)^{-j-2}
   \left(1+\frac{2y}{(1-y)^2}\right)^{-K}\\
 &=(-1)^j\sum_{k\ge0}(-1)^k2^k{K+k-1\choose k}
   y^k(1-y)^{-j-2-2k}.                              \tag{2.2}
\end{aligned}
$$



Taking the coefficient of $y^n$ proves (1.2).  Define



$$
\boxed{\nu_j(k)=k+v_2{2j+1+k\choose k}
                 +v_2{3j+2+k\choose2j+1-k}.}        \tag{2.3}
$$



Kummer's formula makes this entirely explicit in binary digits:



$$
v_2{N\choose M}=s_2(M)+s_2(N-M)-s_2(N),            \tag{2.4}
$$



where $s_2$ is the binary digit sum.  Equivalently, it is the number
of carries in adding $M$ and $N-M$.

The non-Archimedean triangle inequality proves the candidate theorem.
If one summand has strictly smaller valuation than every other summand,
it cannot be cancelled.  Therefore (1.3) holds.  Conversely, an exact
zero would require the least valuation to occur at least twice.

This criterion is finite for each input without evaluating $\ell_j$.
Indeed, $\nu_j(k)\ge k$, while $\nu_j(0)$ is finite.  Hence only



$$
0\le k\le\nu_j(0)           \tag{2.5}
$$



can minimize.

This is a genuine structural reduction, but it is not yet a complete
classification.  Ties can produce substantial cancellation.  For
example,



$$
\begin{array}{c|c|c|c}
 j&\min_k\nu_j(k)&\hbox{minimizers}&v_2(\ell_j)\\ \hline
 2&3&0,1&4\\
 10&5&0,1&10\\
 42&7&0,1&13
 \end{array}                                         \tag{2.6}
$$



Thus a rule that simply takes the minimum term valuation is false.  On
the certified prefix, the largest cancellation uplift is 14, at
$j=10{,}922$ and $19{,}914$.  These finite examples are decisive
counterexamples to that naive proof strategy, not evidence for a zero.

## 3. The mod-4 and carry-one theorem

Modulo 4, every term of (1.2) with $k\ge2$ vanishes.  The $k=1$
term also vanishes because



$$
2{2j+2\choose1}=4(j+1).                             \tag{3.1}
$$



Only $k=0$ survives, proving



$$
\ell_j\equiv(-1)^j{3j+2\choose2j+1}
          =(-1)^j{3j+2\choose j+1}\pmod4.           \tag{3.2}
$$



The binomial coefficient is always even.  If $j$ is even, the two
summands $j+1$ and $2j+1$ are odd, so their addition has a carry in
the least significant bit.  If $j$ is odd, write
$r=v_2(j+1)\ge1$.  Then $2j+1=2(j+1)-1$ has ones in positions
$0,\ldots,r$, while $j+1$ has a one in position $r$; there is a
carry in position $r$.  Kummer's theorem therefore gives



$$
v_2{3j+2\choose j+1}\ge1.   \tag{3.3}
$$



When the carry count is exactly one, (3.2) is 2 modulo 4 up to sign, so
$v_2(\ell_j)=1$.  This proves (1.5).

The condition is conveniently decidable as



$$
s_2(j+1)+s_2(2j+1)-s_2(3j+2)=1.                   \tag{3.4}
$$



For $j=2^r-1$, $r\ge1$, the only carry occurs where the one of $j+1$ meets
the top one of $2j+1$.  For $j=2^r$, the only carry is the low
$1+1$ carry when $r\ge2$, with the separated high bits producing none.  These give
simple infinite subfamilies of the carry-one language.

## 4. Algebraic generating function

The algebraic representation is independent of the 2-adic argument.
Put



$$
R(y)=\frac{(y-1)^2}{y^2(1+y^2)^2},\qquad
 J(y)=\frac{(y-1)^3}{y^2(1+y^2)^2}.                 \tag{4.1}
$$



Then



$$
\ell_j=\operatorname {Res}_{y=0}R(y)J(y)^j\,dy,
 \qquad
 A(z)=\operatorname {Res}_{y=0}\frac{R(y)}{1-zJ(y)}\,dy. \tag{4.2}
$$



Let



$$
\phi(y)=\frac{y^2(1+y^2)^2}{(y-1)^3}.             \tag{4.3}
$$



The equation $\phi(y)=z$ has two Puiseux roots $y_+(z),y_-(z)$
that tend to zero.  Since



$$
\frac{R(y)}{1-zJ(y)}
   =\frac{1}{(y-1)(\phi(y)-z)},                     \tag{4.4}
$$



the sum of the two small-root residues is



$$
A(z)=\frac{d}{dz}\log\bigl((1-y_+(z))(1-y_-(z))\bigr). \tag{4.5}
$$



Thus



$$
H(z)=(1-y_+)(1-y_-),\qquad A=H'/H. \tag{4.6}
$$



For completeness, the algebraic elimination is explicit.  Factor



$$
y^2(1+y^2)^2-z(y-1)^3
 =(y^2+ay+b)(y^4-ay^3+dy^2+ey+f),                  \tag{4.7}
$$



where the small-root factor has $a(0)=b(0)=0$.  Coefficient comparison
gives



$$
\begin{aligned}
 d&=2+a^2-b,\\
 e&=-z-2a-a^3+2ab,\\
 f+ae+bd&=1+3z,\\
 af+be&=-3z,\\
 bf&=z.                                             \tag{4.8}
\end{aligned}
$$



The factorization is unique by formal Hensel lifting from
$y^2(1+y^2)^2$, whose two displayed factors are coprime.  Since
$H=1+a+b$, elimination of $a,b,d,e,f$ yields



$$
\begin{aligned}
G(z,H)={}&-(H-2)^4(H-1)(H^2+4)(H^2-2H+2)^4\\
&+2zH^2(H-2)^2(H^2-2H+2)^2\\
&\qquad\cdot(3H^5-4H^4-24H^3+36H^2+16H-32)\\
&+z^2H^3(H^3-4)^3=0.                               \tag{4.9}
\end{aligned}
$$



At $(z,H)=(0,1)$, $G_H=-5\ne0$, so (4.9) selects a unique ordinary
power series.  It starts



$$
H=1-2z-3z^2+46z^3+242z^4-2302z^5-23645z^6+\cdots. \tag{4.10}
$$



The checker constructs $H$ exactly from $H'=AH$ and verifies
$G(z,H)=0$ coefficientwise through the declared replay order.

There is also a terminating special-function form:



$$
\ell_j=(-1)^{j+1}{3j+2\choose j+1}
 {}_3F_2\!\left(\begin{matrix}-j,-j-\tfrac12,2j+2\\
                 \tfrac j2+1,\tfrac j2+\tfrac32
              \end{matrix};-1\right).              \tag{4.11}
$$



This does not directly invoke a standard fixed-parameter orthogonal
polynomial zero theorem: all five parameters move with $j$, and the
evaluation is at $-1$.

The critical points of $\phi$ satisfy



$$
3y^3-6y^2-y-2=0,            \tag{4.12}
$$



and their critical values satisfy



$$
729z^3-69444z^2+1728z-512=0. \tag{4.13}
$$



The cubic has one real critical value and a complex-conjugate pair.
Numerically, the conjugate pair has modulus
$0.0858764700572\ldots$, much smaller than the real value
$95.2344468549\ldots$.  This explains the oscillatory signs and is a
method obstruction to a one-real-saddle positivity proof.  It is not a
proof that some other contour argument cannot work.

## 5. Automata: what is available and what is not

Equation (4.9) proves that $A(z)$ is algebraic.  Standard finite-field
automaticity therefore applies to its reductions.  More constructively,
Rowland and Yassawi, *Automatic congruences for diagonals of rational
functions* (arXiv:1310.8635), give algorithms for prime-power congruence
automata for rational diagonals, with an algebraic-series variant.

This framework justifies a possible future finite-state attack, but Item
215 does not hide an unconstructed automaton behind that theorem.  Two
specific gaps remain:

1. an automaton modulo a fixed $p^\alpha$ does not give a valuation
   bound uniform in $\alpha$;
2. automata for distinct primes read representations in distinct bases,
   so their zero languages do not form a simple synchronous product.

The finite diagnostic illustrates the distinction.  On
$1\le j\le20{,}000$, the primes



$$
3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61  \tag{5.1}
$$



cover the prefix: for each $j$, at least one listed prime does not
divide $\ell_j$.  This is a finite congruence replay only.  Without a
same-base all-input construction, it cannot be promoted to an all-$j$
proof.  This is a limitation of the present method, not an impossibility
theorem for finite-prime arguments.

## 6. Zero spacing and the improved rank-one ceiling

Let



$$
w_j=\frac{2}{(3j+2)(j+1)}.  \tag{6.1}
$$



Item 210 proved the order-three recurrence



$$
P_0(j)\ell_j+P_1(j)\ell_{j+1}
 +P_2(j)\ell_{j+2}+P_3(j)\ell_{j+3}=0,             \tag{6.2}
$$



with $P_0(j)P_3(j)\ne0$ for every $j\ge1$.  Three consecutive zeros
would propagate both forward and backward, ultimately contradicting
$\ell_1=-10$.  Hence every block of three consecutive indices contains
at least one nonzero $\ell_j$.

Fix a prefix $1\le j\le J$ on which nonvanishing has been certified and
put $a=J+1$.  Partition the unresolved tail into



$$
\{a+3q,a+3q+1,a+3q+2\},\qquad q\ge0. \tag{6.3}
$$



At most two members of each block can be singular.  Since $w_j$ is
decreasing, their total weight is at most



$$
\sum_{q\ge0}\bigl(w_{a+3q}+w_{a+3q+1}\bigr).      \tag{6.4}
$$



Use



$$
w_j<\frac{2}{3j(j+1)}=\frac23 f(j),\qquad
 f(x)=\frac1{x(x+1)}.                               \tag{6.5}
$$



For decreasing $f$,



$$
\sum_{q\ge0}f(b+3q)
 \le f(b)+\frac13\int_b^\infty f(x)\,dx
 =f(b)+\frac13\log\left(1+\frac1b\right).          \tag{6.6}
$$



Equations (6.4)--(6.6) give the proved bound



$$
\boxed{
 \sum_{\substack{j>J\\\ell_j=0}}w_j
 <\frac23\left(\frac1{a(a+1)}+\frac1{(a+1)(a+2)}\right)
 +\frac29\left[
  \log\left(1+\frac1a\right)
 +\log\left(1+\frac1{a+1}\right)\right].}          \tag{6.7}
$$



For $J=20{,}000$, this is



$$
0.00002222333290748794965950661954\ldots\quad\hbox{per }m, \tag{6.8}
$$



or



$$
0.00000370388881791465827658443659\ldots\quad\hbox{per }6m. \tag{6.9}
$$



It is $0.6667333222\ldots$ times the full-tail bound used in Item 210.
As there, every ordinary modular rank-one prime in a fixed nonzero band
has finite support and contributes asymptotic coefficient zero.  Bound
(6.7) concerns only still-possible rationally singular bands.

## 7. Certificate and exact/finite/open ledger

The deterministic checker performs the following operations using only
the Python standard library:

1. verifies the Item 210 recurrence through $j=20{,}000$, with the
   same sequence hash;
2. cross-checks (1.1) and (1.2) independently through $j=80$;
3. checks the unique-minimum valuation theorem and carry-one consequence
   on the declared finite prefix;
4. reconstructs $H$ from $H'=AH$ and verifies (4.9) as an exact
   formal-series identity through order 96;
5. replays the finite mixed-prime diagnostic; and
6. records the symbolic and decimal forms of (6.7).

The proof-status ledger is:

- **PROVED:** formulas (1.2)--(1.5), the all-input tied-minimum candidate
  theorem, the algebraic representation (4.6)--(4.9), zero spacing, and
  the ceiling (6.7).
- **EXPERIMENTAL / FINITE EXACT:** no zero through $20{,}000$; the 16,029/3,971
  unique/tied profile; the prime cover on that prefix; and the formal
  series replay to order 96.
- **OPEN:** nonvanishing on every tied-minimum index; a uniform 2-adic
  valuation automaton; and a zero-rate theorem for the singular bands.

The correct Route-1 conclusion is therefore limited but rigorous: this
branch sharpens the structural obstruction and lowers its maximal rate,
yet it neither completes Route 1 nor proves Route 1 impossible.
