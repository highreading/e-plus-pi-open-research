> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Full row rank of the raw-arctangent bordered matrix

Date: 2026-08-26

This note proves the all-degree rank assertion that was left open in
`research_log.md`.  It concerns only the raw-arctangent matrix; it does not
prove that the resulting endpoint linear forms are small or nonzero.

## Theorem

For every integer $m\geq1$, let $D_m$ be the $(2m-1)\times 2m$ matrix whose
jet rows, indexed by $k=m,\ldots,3m-3$, are

$$
((k)_0,\ldots,(k)_{m-1}\mid
 (k)_0\tau_k,\ldots,(k)_{m-1}\tau_{k-m+1}),
$$

where

$$
\tau_r=\begin{cases}
0,&r\text{ even},\\
(-1)^{(r-1)/2}(r-1)!,&r\text{ odd},
\end{cases}
$$

and whose final row is

$$
(-4,\ldots,-4\mid1,\ldots,1).
$$

Then $D_m$ has full row rank $2m-1$ over $\mathbb Q$.

In fact the same conclusion holds if the $-4$ in the final row is replaced
by any rational number.

## 1. Reduction to a square determinant independent of the border value

The assertion is immediate for $m=1$.  Assume $m\geq2$ and put
$\ell=m-1$.

If $D_m$ did not have full row rank, its kernel would have dimension at
least two.  A kernel vector is a pair of polynomials $(B,C)$ of degrees
less than $m$ such that

$$
[z^k]\bigl(B(z)e^z+C(z)\arctan z\bigr)=0
\quad(m\leq k\leq3m-3)
$$

and $C(1)=4B(1)$.  On a vector space of dimension at least two, the
functional $B\mapsto B(1)$ has a nonzero kernel.  We could therefore choose
a nonzero pair with $B(1)=0$, and the endpoint equation would then also give
$C(1)=0$.  Thus

$$
B=(z-1)\widetilde B,\qquad C=(z-1)\widetilde C,
\qquad \deg\widetilde B,\deg\widetilde C<\ell.
$$

Consequently it suffices to prove that the following $2\ell\times2\ell$
matrix $T_\ell=(P\mid Q)$ is nonsingular.  Its rows are indexed by

$$
\mathcal X=\{\ell+1,\ell+2,\ldots,3\ell\},
$$

its columns in each block are indexed by $a=0,\ldots,\ell-1$, and

$$
P_{k,a}=\frac{k-a-1}{(k-a)!},\qquad
Q_{k,a}=t_{k-a-1}-t_{k-a},                         \tag{1}
$$

where

$$
t_r=[z^r]\arctan z=
\begin{cases}
0,&r\text{ even},\\
(-1)^{(r-1)/2}/r,&r\text{ odd}.
\end{cases}
$$

These are precisely the coefficients of
$z^a(z-1)e^z$ and $z^a(z-1)\arctan z$.

To connect this coefficient formulation exactly to $D_m$, the dot product
of its $k$-th jet row with
$(b_0,\ldots,b_{m-1},c_0,\ldots,c_{m-1})$ is

$$
k![z^k]\bigl(B(z)e^z+C(z)\arctan z\bigr).
$$

Indeed $(k)_a=k!/(k-a)!$ and
$(k)_a\tau_{k-a}=k!t_{k-a}$.  Dividing a jet row by the nonzero integer
$k!$ therefore changes neither its equation nor its rank.

We prove $\det T_\ell\ne0$ by showing that its Laplace expansion along the
first $\ell$ columns has a unique summand of least $2$-adic valuation.
Write $\nu=\nu_2$ and put $\nu(0)=+\infty$.

## 2. The exponential minors

For $q\geq0$ define

$$
A(q)=\sum_{j=0}^{q-1}\nu(j!),\qquad A(0)=0.
$$

For a set $S=\{x_1<\cdots<x_\ell\}\subset\mathcal X$, put
$V(S)=\prod_{i<j}(x_j-x_i)$ and
$W_S(x)=\prod_{u\in S}(x-u)$.  Define the integral linear functional
$\Lambda$ on polynomials of degree at most $\ell$ by

$$
\Lambda((x)_j)=1\quad(0\leq j\leq\ell).
$$

Since

$$
k!P_{k,a}=(k)_{a+1}-(k)_a,
$$

the polynomials $(x)_{a+1}-(x)_a$ form a basis of $\ker\Lambda$.
An alternant calculation (or adjoining the row $\Lambda$ to the evaluation
matrix) gives

$$
\det P_S=(-1)^\ell\,
\frac{V(S)\Lambda(W_S)}{\prod_{u\in S}u!}.         \tag{2}
$$

Here $\Lambda(W_S)$ is an integer: the change of basis from monomials to
falling factorials has integral Stirling-number coefficients.  Hence

$$
\nu(\det P_S)=
\nu(V(S))-\sum_{u\in S}\nu(u!)+\nu(\Lambda(W_S)). \tag{3}
$$

We shall use the standard integral-Vandermonde bound

$$
\nu(V(S))\geq A(\ell).                              \tag{4}
$$

Indeed $V(S)/\prod_{j=0}^{\ell-1}j!$ is the determinant of the
integer matrix $\bigl(\binom{x_i}{j}\bigr)$.  Equality holds for
consecutive integers.

Among all $\ell$-subsets of $\mathcal X$, the sum
$\sum_{u\in S}\nu(u!)$ is largest only for the following two sets:

$$
S_0=\{2\ell+1,2\ell+2,\ldots,3\ell\},             \tag{5}
$$

$$
S_*=\{2\ell\}\cup\{2\ell+2,2\ell+3,\ldots,3\ell\}. \tag{6}
$$

This follows because $\nu(n!)$ is nondecreasing and its only consecutive
ties are $\nu((2r)!)=\nu((2r+1)!)$.  Moreover,

$$
\nu(V(S_0))=A(\ell),\qquad
\nu(V(S_*))=A(\ell)+\nu(\ell).                     \tag{7}
$$

For the second identity, separate the final $\ell-1$ consecutive points;
the differences from the first point are $2,3,\ldots,\ell$.

The parity of the remaining factor in (2) is also explicit.  If
$c=2\ell+1$, then

$$
W_{S_0}(x)=(x-c)_\ell.
$$

The binomial identity for falling factorials gives

$$
\Lambda(W_{S_0})
=\sum_{r=0}^{\ell}\binom\ell r(-c)_r
\equiv1+\ell c\equiv1+\ell\pmod2,                 \tag{8}
$$

because $(-c)_r$ is even for $r\geq2$.  Also

$$
W_{S_*}-W_{S_0}=\prod_{j=c+1}^{c+\ell-1}(x-j),
$$

and applying the same calculation to this consecutive product, whose first
root is even, shows

$$
\Lambda(W_{S_*})\equiv\ell\pmod2.                 \tag{9}
$$

Thus $\Lambda(W_{S_0})$ is odd when $\ell$ is even, whereas for odd
$\ell$ it is even and $\Lambda(W_{S_*})$ is odd.

## 3. The arctangent minors

Set

$$
g(q)=\frac{q(q-1)}2+A(q).                          \tag{10}
$$

For $q$ distinct integers of one parity, their Vandermonde has valuation at
least $g(q)$: divide all differences by $2$ and use (4).

The substitution

$$
q_0=-c_0,\quad q_j=c_{j-1}-c_j\ (1\leq j<\ell),
\quad q_\ell=c_{\ell-1}                            \tag{11}
$$

identifies $\mathbb Z^\ell$ unimodularly with the lattice
$\sum_{j=0}^{\ell}q_j=0$.  In these variables an even row $k$ sees only
the odd $j$ and an odd row sees only the even $j$; after harmless row and
column signs, each nonzero block has entries $1/(k-j)$.  These denominators
are odd.

Here are the row and column operations explicitly.  Let $I$ be the
$(\ell+1)\times\ell$ incidence matrix

$$
I_{j,a}=\mathbf1_{j=a+1}-\mathbf1_{j=a}
\quad(0\leq j\leq\ell,\ 0\leq a<\ell),
$$

and, for an $\ell$-row set $U$, let
$M_U=(t_{k-j})_{k\in U,0\leq j\leq\ell}$.  Then (1) says exactly
$Q_U=M_UI$.  Cauchy--Binet, or expansion in maximal minors of $M_U$, gives

$$
\det Q_U=(-1)^\ell
\det\begin{pmatrix}M_U\\1&1&\cdots&1\end{pmatrix}. \tag{11a}
$$

No division occurs in this passage.  Next reorder the ordinary rows as
even rows followed by odd rows, and reorder the columns as odd $j$ followed
by even $j$.  For the nonzero entries,

$$
t_{2K-(2J+1)}=\frac{(-1)^{K-1}(-1)^J}{2K-(2J+1)},
$$

$$
t_{(2K+1)-2J}=\frac{(-1)^K(-1)^J}{(2K+1)-2J}.       \tag{11b}
$$

Factor the displayed row signs from the ordinary rows and the displayed
$(-1)^J$ signs from the columns.  All factors are $2$-adic units.  Each
ordinary diagonal block is now a Cauchy block $1/(k-j)$, while the entries
in the appended row become $(-1)^J$ in the corresponding parity block.

Let

$$
e=\#\{0\leq j\leq\ell:j\text{ even}\},\qquad
o=\#\{0\leq j\leq\ell:j\text{ odd}\}.
$$

For an $\ell$-row set $U$, the minor $Q_U$ is structurally zero unless the
number of even rows is $o$ or $o-1$.  In the first case the odd-pole block is
square and the even-pole block has one fewer row than columns; in the second
case their roles are reversed.  The condition $\sum q_j=0$ appends a final
row of ones to the latter block.

More precisely, after the permutations in (11b), a nonzero determinant in
(11a) factors, up to sign, into one square Cauchy determinant and one
bordered Cauchy determinant of the form in (13).  This is because the sole
appended row must be assigned to the parity block having one more column
than ordinary rows.  If neither block has this size profile, every term in
the determinant expansion is zero.

We need the following bordered-Cauchy valuation.  For $r\geq1$, put
$n=r-1$ and

$$
\beta(r)=\frac{n(n-1)}2+A(n)+
\begin{cases}
n,&n\text{ even},\\
n+1,&n\text{ odd}.
\end{cases}                                        \tag{12}
$$

If $x_1<\cdots<x_n$ have parity opposite to
$p,p+2,\ldots,p+2n$, then

$$
\nu\det\begin{pmatrix}
\dfrac1{x_i-(p+2h)}\\[2mm]
(-1)^h
\end{pmatrix}_{\substack{1\leq i\leq n\\0\leq h\leq n}}
\geq \nu(V(x_1,\ldots,x_n))+\beta(r).              \tag{13}
$$

To prove it, expand along the last row and use the Cauchy determinant
formula.  The cofactor sign and $(-1)^h$ cancel, so all cofactors have the
same sign.  If

$$
S_n=\sum_{h=0}^{n}\binom nh
\prod_{i=1}^{n}(x_i-p-2h),                          \tag{14}
$$

one obtains exactly

$$
\left|\det\begin{pmatrix}
\dfrac1{x_i-(p+2h)}\\[2mm](-1)^h
\end{pmatrix}\right|
=\frac{|V(x)V(p,p+2,\ldots,p+2n)|}
{\prod_{i,h}|x_i-(p+2h)|}\,
\frac{|S_n|}{2^n n!}.                              \tag{14a}
$$

Indeed, deleting column $h$ removes from the pole Vandermonde the factor
$2^n h!(n-h)!$ and restores the factors
$\prod_i(x_i-p-2h)$ to the denominator product; multiplication by
$\binom nh$ puts all cofactors over the common factor in (14a).  Thus

$$
\nu(\text{bordered determinant})
=\nu(V(x))+\frac{n(n-1)}2+A(n)+\nu(S_n).           \tag{15}
$$

after cancelling the factor $2^n n!$ in the Cauchy formula.  (Equivalently,
the right side of (15) has $\nu(S_n)$ where (12) uses its lower bound.)

Every factor in (14) is odd, and

$$
\nu(S_n)=n\quad(n\text{ even}),\qquad
\nu(S_n)\geq n+1\quad(n\text{ odd}).               \tag{16}
$$

For completeness, expand the product in powers of $2h$, expand $h^j$ in
falling factorials, and use

$$
\sum_{h=0}^{n}\binom nh(h)_q=(n)_q2^{n-q}.
$$

After division by $2^n$, reduction modulo $2$ leaves only the diagonal
terms $q=j$.  If $n$ is even only $j=0$ survives, while if $n$ is odd the
$j=0$ and $j=1$ terms are both odd and cancel.  This proves (16).

We shall also need an equality case.  If

$$
x_i-p=a+2(i-1)\quad(1\leq i\leq n)
$$

are consecutive in their parity class, define

$$
F_n(a)=2^{-n}S_n
=2^{-n}\sum_{h=0}^n\binom nh
  \prod_{i=0}^{n-1}(a+2i-2h).                     \tag{17a}
$$

Here is a complete mod-$4$ calculation.  Since
$u^{\overline n}=n![z^n](1-z)^{-u}$,

$$
F_n(a)=n![z^n](1-z)^{-a/2}(2-z)^n.                 \tag{17b}
$$

The diagonal-series identity

$$
\sum_{n\geq0}[z^n]A(z)B(z)^n t^n
=\frac{A(w)}{1-tB'(w)},\qquad w=tB(w),             \tag{17c}
$$

applied to $A(z)=(1-z)^{-a/2}$ and $B(z)=2-z$ gives

$$
\mathcal F_a(t):=\sum_{n\geq0}F_n(a)\frac{t^n}{n!}
=(1+t)^{a/2-1}(1-t)^{-a/2}.                        \tag{17d}
$$

(Equation (17c) is the one-variable Lagrange inversion formula; here its
solution is simply $w=2t/(1+t)$.)  Logarithmic differentiation of (17d)
gives

$$
(1-t^2)\mathcal F_a'(t)=(a-1+t)\mathcal F_a(t),
$$

and coefficient comparison yields the integral recurrence

$$
F_0(a)=1,\quad F_1(a)=a-1,\quad
F_{n+1}(a)=(a-1)F_n(a)+n^2F_{n-1}(a).              \tag{17e}
$$

In particular every $F_n$ lies in $\mathbb Z[a]$.  For odd $a$, recurrence
(17e) proves directly by induction that

$$
F_{2s}(a)\equiv1\pmod4,
\qquad F_{2s+1}(a)\equiv a-1\pmod4.               \tag{17f}
$$

Indeed, in the step from an odd index to an even one, $(a-1)^2$ is divisible
by $4$ and the odd square multiplying the preceding even term is $1$ modulo
$4$.  In the step from an even index to an odd one, the even square is
divisible by $4$.  Thus, for odd $n$ and odd $a$,

$$
2^{-n}S_n=F_n(a)\equiv a-1\pmod4.                 \tag{17}
$$

For even $n$, equality in (16) already holds.  For odd $n$, (17) shows
that $\nu(S_n)=n+1$ whenever $a\equiv3\pmod4$.  Therefore (13) is an
equality whenever the $x_i$ are consecutive in their parity class and,
when $r$ is even, $a\equiv3\pmod4$.

A square Cauchy block of size $q$ has valuation equal to the sum of its row
and pole Vandermonde valuations.  It follows from (10)--(13) that the least
possible valuation of an arctangent minor in either admissible parity
orientation is obtained by replacing each row Vandermonde by its lower
bound $g(\cdot)$, each square block by the corresponding two $g$ terms, and
each bordered block of size $r$ by $g(r-1)+\beta(r)$.

When $\ell=2r$ one orientation therefore has lower bound

$$
L_A=3g(r)+\beta(r+1),                               \tag{18}
$$

and the other has

$$
L_B=2g(r+1)+g(r-1)+\beta(r).                        \tag{19}
$$

Directly from (10)--(12),

$$
L_B-L_A=
\begin{cases}
0,&r\text{ odd},\\
2+2\nu(r),&r\text{ even},
\end{cases}                                        \tag{20}
$$

so $L_A$ is the global lower bound.  For $U=\mathcal X\setminus S_0$,
all row sets in the two parity blocks are consecutive.  Its bordered block
has size $r+1$; if that size is even, its first row-to-pole difference is
$2r+1\equiv3\pmod4$.  Hence (17) shows that $Q_U$ attains (18).

When $\ell=2r+1$, both pole sets have size $R=r+1$, and both orientations
have the same lower bound

$$
L_C=2g(R)+g(R-1)+\beta(R).                          \tag{21}
$$

For $U=\mathcal X\setminus S_*$, both parity row sets are consecutive.
The bordered block has first row-to-pole difference $2r+1$, which is
$3\pmod4$ exactly when $R$ is even.  Thus (17) shows that this minor attains
(21).

## 4. Unique least-valuation Laplace term

Expand $\det T_\ell$ along its first $\ell$ columns.  A term indexed by
$S\subset\mathcal X$, $|S|=\ell$, is, up to sign,
$\det P_S\det Q_{\mathcal X\setminus S}$.

If $\ell$ is even, equations (3)--(9) and (18)--(20) show that the term
indexed by $S_0$ attains all the global lower bounds and has
$\Lambda(W_{S_0})$ odd.  Every set other than $S_0,S_*$ has a strictly
smaller factorial-valuation sum in (3).  The remaining set $S_*$ has the
same factorial sum but, by (7), pays the positive extra valuation
$\nu(\ell)$.  Hence the $S_0$ term is the unique term of least valuation.

If $\ell$ is odd, the term indexed by $S_*$ attains all lower bounds in
(3), (4), and (21), and (9) makes its $\Lambda$ factor odd.  The only other
set with the maximal factorial-valuation sum is $S_0$; by (8) its
$\Lambda$ factor is even (or zero).  Every other set loses at least one in
the factorial sum.  Hence the $S_*$ term is the unique term of least
valuation.

A sum in $\mathbb Q_2$ with a unique least-valuation summand cannot be zero.
Therefore $\det T_\ell\ne0$.  The reduction in Section 1 proves that $D_m$
has full row rank for every $m$.

The reduction used only the implication
$B(1)=0\Longrightarrow C(1)=0$.  If the final row is
$(\lambda,\ldots,\lambda\mid1,\ldots,1)$, its equation is
$C(1)=-\lambda B(1)$, so the same implication holds.  Thus the proof works
for every rational border coefficient $\lambda$, not only
$\lambda=-4$.
