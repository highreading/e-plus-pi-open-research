> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Full row rank of the endpoint-matched Machin matrix

Date: 2026-08-26

This note proves an all-degree rank theorem for the Machin system used in
`scripts/mixed_hermite_pade_probe.py`.  It is a matrix nondegeneracy result.
It does **not** prove that the resulting linear form in $1,e+\pi$ is
nonzero or small, and it does not control its endpoint-primitive height.

## 1. Statement and reduction

Put



$$
G(z)=16\arctan(z/5)-4\arctan(z/239)=\sum_{r\geq0}g_rz^r .
$$



Thus $g_r=0$ for even $r$, while, for positive odd $r$,



$$
g_r=4(-1)^{(r-1)/2}\frac{4\,5^{-r}-239^{-r}}r.       \tag{1}
$$



For $n\geq1$, let $D_n$ be the $(2n+1)$-by-$(2n+2)$
rational matrix in the variables



$$
(b_0,\ldots,b_n,c_0,\ldots,c_n)
$$



whose first $2n$ rows express



$$
[z^k]\bigl(B(z)e^z+C(z)G(z)\bigr)=0
 \quad(n+1\leq k\leq3n),                         \tag{2}
$$



and whose last row expresses $C(1)=B(1)$.  Equivalently, the jet
rows have entries



$$
\left(\frac1{(k-j)!}\right)_{0\leq j\leq n}
 \mathbin{\Big|}
 \left(g_{k-j}\right)_{0\leq j\leq n},            \tag{3}
$$



with terms of negative index interpreted as zero, and the final row is



$$
(-1,\ldots,-1\mid1,\ldots,1).                    \tag{4}
$$



**Theorem 1.**  For every $n\geq1$, $D_n$ has full row rank
$2n+1$ over $\mathbb Q$.  Consequently its kernel is
one-dimensional.  Every nonzero kernel vector satisfies



$$
B(1)=C(1)\ne0.                                    \tag{5}
$$



More generally, full row rank still holds if the endpoint equation is
$C(1)=\lambda B(1)$ for any fixed $\lambda\in\mathbb Q$.  In that
case every nonzero kernel vector has $B(1)\ne0$, and hence also
$C(1)\ne0$ when $\lambda\ne0$.

The same assertions are immediate for $n=0$.

Here is the standard reduction.  If $D_n$ failed to have full row
rank, its kernel would have dimension at least two.  The functional
$B\mapsto B(1)$ would then have a nonzero kernel vector.  On that
vector (4) also gives $C(1)=0$, so



$$
B=(z-1)\widetilde B,\qquad C=(z-1)\widetilde C,
 \qquad \deg\widetilde B,\deg\widetilde C<n.       \tag{6}
$$



It is therefore enough to prove that the $2n$-by-$2n$ coefficient
matrix $T_n=(P\mid Q)$, with rows $k=n+1,\ldots,3n$, columns
$a=0,\ldots,n-1$, and



$$
P_{k,a}=\frac{k-a-1}{(k-a)!},\qquad
 Q_{k,a}=g_{k-a-1}-g_{k-a},                        \tag{7}
$$



is nonsingular.  Dividing every column of the $Q$-block by $4$
does not affect nonsingularity.  In the rest of the proof $Q$ denotes
this divided block.

The exponential block $P$ is exactly the block treated in
`sources/raw_arctan_bordered_rank_proof.md`.  The point of this note is
that the Machin block has the same decisive $2$-adic minor valuations
as the raw-arctangent block.  We prove this rather than infer it from
finite computations.

## 2. A $2$-adic stability lemma

For $h\geq0$, let $\mathcal A_h$ be the class of power series



$$
H(t)=\sum_{m\geq0}h_mt^m,\qquad h_m\in2^{m+h}\mathbb Z_2.    \tag{8}
$$



Such a series converges at every $t\in\mathbb Z_2$.  Write
$V(x)=\prod_{i<j}(x_j-x_i)$.

**Lemma 2 (square and bordered stability).**  Suppose
$H,H_0\in\mathcal A_0$ and $H-H_0\in\mathcal A_h$.

1.  For integers $x_1,\ldots,x_q,y_1,\ldots,y_q$, define

    

$$
\Phi_q(H;x,y)=\det\bigl(H(x_i-y_j)\bigr)_{1\leq i,j\leq q}.
$$



    If the $x_i$'s and $y_j$'s are distinct, then

    

$$
\frac{\Phi_q(H;x,y)}
    {2^{q(q-1)}V(x)V(y)}\in\mathbb Z_2,             \tag{9}
$$



    and the two normalized quotients for $H$ and $H_0$ are
    congruent modulo $2^h\mathbb Z_2$.

2.  For distinct integers $x_1,\ldots,x_s$, define

    

$$
\Psi_s(H;x)=
    \det\begin{pmatrix}
    H(x_i-j)_{\substack{1\leq i\leq s\\0\leq j\leq s}}\\
    ((-1)^j)_{0\leq j\leq s}
    \end{pmatrix}.                                  \tag{10}
$$



    Then

    

$$
\frac{\Psi_s(H;x)}
    {2^{s^2}V(x)\prod_{j=0}^{s-1}j!}\in\mathbb Z_2,             \tag{11}
$$



    and again the normalized quotients for $H$ and $H_0$ are
    congruent modulo $2^h\mathbb Z_2$.

The congruence assertion also applies to $H$ and $cH_0$, for a
$2$-adic unit $c$; in that case the comparison term in (9) is
$c^q\Phi_q(H_0;x,y)$, and that in (11) is
$c^s\Psi_s(H_0;x)$.

**Proof.**  It is enough first to use polynomial truncations of the
series; the stated results then pass to the $2$-adic limit.

For (9), expand the determinant in powers of the $x_i$'s and $y_j$'s.
It is alternating in each set of variables, hence is divisible by
$V(x)V(y)$.  A nonzero bialternant has total $x$-degree at least
$q(q-1)/2$ and total $y$-degree at least $q(q-1)/2$.  Every use of
a coefficient of degree $m$ supplies a factor $2^m$ by (8).
This proves the factor $2^{q(q-1)}$ in (9).  The alternant quotients
have integral coefficients (they are integral combinations of Schur
polynomials).  If one coefficient comes from $H-H_0\in\mathcal A_h$,
there is an additional factor $2^h$.  Expanding the difference of the
two determinants proves the congruence.

For (11), perform the unimodular column transformation



$$
\widetilde C_r=\sum_{j=0}^r(-1)^{r-j}\binom rj C_j
 \quad(0\leq r\leq s).                             \tag{12}
$$



In an ordinary row the new entry is an $r$-th finite difference of
$H$, while in the last row it is $(-1)^r2^r$.  If
$H\in\mathcal A_0$, then



$$
\frac{\Delta^rH(t)}{2^r r!}                       \tag{13}
$$



is again a power series whose coefficient of $t^d$ belongs to
$2^d\mathbb Z_2$.  One direct verification uses



$$
\frac{\Delta^r(t)_m}{r!}=\binom mr(t)_{m-r}
$$



after expanding ordinary powers in the falling-factorial basis.
Expand (12) along the final row.  If column $r$ is used there, the
ordinary columns supply



$$
\prod_{\substack{0\leq j\leq s\\j\ne r}}2^j j!,
$$



and the final-row entry supplies $2^r$.  Hence every term contains
$2^{s(s+1)/2}\prod_{j=0}^{s-1}j!$; the factorial divisibility follows
from $s!/r!\in\mathbb Z$.  The determinant of the remaining normalized
ordinary columns is an alternant in the $x_i$'s.  Applying the same
one-variable argument as above supplies
$2^{s(s-1)/2}V(x)$.  The two powers of $2$ add to $s^2$, proving
(11).  If one entry comes from $\mathcal A_h$, all these operations
retain its additional factor $2^h$, which proves the bordered
congruence.  This also proves the unit-scaled formulation. $\square$

## 3. The Machin kernel is a stable Cauchy kernel

For an odd positive integer $d=1+2t$, put



$$
K_d=\frac{4\,5^{-d}-239^{-d}}d=F(t),              \tag{14}
$$



where



$$
F(t)=\frac{N(t)}{1+2t},\qquad
 N(t)=\frac45\left(\frac1{25}\right)^t
      -\frac1{239}\left(\frac1{239^2}\right)^t.  \tag{15}
$$



Let



$$
R(t)=\frac1{1+2t},\qquad
 c=N(0)=\frac45-\frac1{239}=\frac{951}{1195}.      \tag{16}
$$



Both $1/25$ and $1/239^2$ belong to $1+8\mathbb Z_2$, so their
$2$-adic logarithms are defined and have valuations



$$
v_2\!\left(\log(1/25)\right)=3,\qquad
 v_2\!\left(\log(1/239^2)\right)=5.               \tag{17}
$$



For $r\geq1$, the coefficient of $t^r$ in $N(t)-c$ is



$$
\frac45\frac{\log(1/25)^r}{r!}
 -\frac1{239}\frac{\log(1/239^2)^r}{r!}.          \tag{18}
$$



Using $v_2(r!)\leq r-1$, the two terms in (18) have valuations at
least



$$
2+3r-v_2(r!)\geq r+4,
 \qquad
 5r-v_2(r!)\geq r+4.                              \tag{19}
$$



Consequently



$$
N(t)-c\in\mathcal A_4.                           \tag{20}
$$



Since $R(t)=\sum_{m\geq0}(-2)^mt^m\in\mathcal A_0$, convolution of
coefficients in $(N-c)R$ gives



$$
F-cR\in\mathcal A_4.                             \tag{21}
$$



The definitions in (15) are valid for every $t\in\mathbb Z_2$, not only
for nonnegative integers: for $u\in1+8\mathbb Z_2$ we define
$u^t=\exp(t\log u)$.  At a negative ordinary integer this agrees with
the usual rational inverse power.  Also $1+2t$ is always odd, hence a
unit, for $t\in\mathbb Z_2$.  Thus $F(t)$ and the series comparison
(21) remain valid at all negative arguments which could occur in the
formal determinant lemma.  In the coefficient matrices below the actual
odd differences satisfy $d\geq1$, so their $t=(d-1)/2$ are in fact
nonnegative.

Notice that $c$ is a $2$-adic unit.  Lemma 2 therefore says the
following.

* Every square determinant made from the Machin kernel $K_d$, with
  odd row-to-pole differences, has exactly the same $2$-adic valuation
  as the corresponding raw Cauchy determinant $1/d$.  Indeed, after
  division by its row and pole Vandermonde factors, the raw determinant
  is a unit by the Cauchy formula, and (21) preserves that unit modulo
  $16$.
* Every bordered determinant with final row $(-1)^j$ has at least the
  raw-Cauchy lower bound.  Whenever the normalized raw bordered
  determinant has valuation zero or one, the Machin determinant has the
  same valuation, again by congruence modulo $16$.

For clarity, the raw bordered facts needed below are the following.  If
$s$ ordinary row points of one parity face the $s+1$ consecutive pole
points $p,p+2,\ldots,p+2s$, then



$$
v_2(\hbox{bordered determinant})
 \geq v_2(V(\hbox{rows}))+\beta(s+1),              \tag{22}
$$



with



$$
\beta(r)=\frac{(r-1)(r-2)}2+A(r-1)+
 \begin{cases}
 r-1,&r-1\text{ even},\\
 r,&r-1\text{ odd},
 \end{cases}
 \quad
 A(q)=\sum_{j=0}^{q-1}v_2(j!).                    \tag{23}
$$



Here is the exact match between Lemma 2's denominator and (22).  Write
the original row points as $x_i=p+1+2X_i$.  Then



$$
v_2(V(x_1,\ldots,x_s))
 =\frac{s(s-1)}2+v_2(V(X_1,\ldots,X_s)).           \tag{22a}
$$



The valuation of the universal factor in (11) is



$$
s^2+v_2(V(X))+A(s).                               \tag{22b}
$$



On the other hand, the explicit raw bordered formula (equation (15) of
the raw proof) has valuation



$$
s(s-1)+v_2(V(X))+A(s)+v_2(S_s).                  \tag{22c}
$$



After division by (22b), the raw normalized quotient therefore has
valuation $v_2(S_s)-s$.  This is zero when $s$ is even.  When $s$ is
odd it is at least one, and it is exactly one in the equality case below.
This proves explicitly that the normalization used in Lemma 2 is the one
needed for the raw bound, rather than merely a proportional factor.

For consecutive row points, equality holds when $s$ is even; when
$s$ is odd it holds if the first row-to-pole difference is $3\pmod4$.
These assertions follow from the explicit bordered Cauchy evaluation
and recurrence in equations (13)--(17) of
`sources/raw_arctan_bordered_rank_proof.md`.  In the equality cases the
raw quotient after the universal factor has valuation respectively zero
or one, so Lemma 2 and (21) prove the identical assertions for $K_d$.

## 4. Parity splitting and the unique term

Let $U$ be any $n$-element subset of the row set



$$
\mathcal X=\{n+1,n+2,\ldots,3n\}.
$$



Introduce the $(n+1)$-column coefficient matrix



$$
M_U=(\gamma_{k-j})_{\substack{k\in U\\0\leq j\leq n}},
 \quad
 \gamma_d=\begin{cases}
 0,&d\text{ even},\\
 (-1)^{(d-1)/2}K_d,&d\text{ odd}.
 \end{cases}                                      \tag{24}
$$



and the incidence matrix



$$
I_{j,a}=\mathbf1_{j=a+1}-\mathbf1_{j=a}
 \quad(0\leq j\leq n,\ 0\leq a<n).              \tag{25}
$$



Then $Q_U=M_UI$, and the integral maximal-minor identity for $I$
gives



$$
\det Q_U=(-1)^n
 \det\begin{pmatrix}M_U\\1&1&\cdots&1\end{pmatrix}.           \tag{26}
$$



Here is the sign factorization explicitly.  Write an even ordinary row
as $k=2K$, an odd ordinary row as $k=2K+1$, an odd pole column as
$j=2J+1$, and an even pole column as $j=2J$.  Then



$$
\gamma_{2K-(2J+1)}=(-1)^{K-1}(-1)^J
 K_{2K-(2J+1)},                                    \tag{26a}
$$





$$
\gamma_{(2K+1)-2J}=(-1)^K(-1)^J
 K_{(2K+1)-2J}.                                    \tag{26b}
$$



Reorder ordinary rows by parity and columns $j$ by the opposite parity.
Factoring the displayed row signs and the column signs $(-1)^J$ turns
every nonzero ordinary entry into $K_d=F((d-1)/2)$.  The original
appended row consists of ones, so after the same column factor it becomes
$(-1)^J$ inside each parity block.  All extracted signs are $2$-adic
units and do not change valuations.  Thus a nonzero determinant in
(26) factors into one square kernel determinant and one bordered kernel
determinant.  It is structurally zero unless the number of even rows is
one of the two sizes described in the raw proof.  By Section 3, every
such Machin factor has the same lower bound as its raw counterpart, and
the equality cases used in the raw proof remain equality cases.

There is no index shift hidden here.  The raw proof denotes by $m$ the
number of coefficients before factoring and sets $\ell=m-1$.  The
present unreduced polynomials have degree at most $n$, hence $m=n+1$ and
$\ell=n$.  After (6) there are exactly $n$ coefficients in each block,
the square matrix has rows $n+1,\ldots,3n$, and its row set is precisely
$\mathcal X$ above.  Thus every occurrence of $\ell$ in the raw minor
analysis is replaced by $n$, with no further change.

We can now copy the final valuation comparison without any extrapolation.
Expand



$$
\det T_n=\sum_{\substack{S\subset\mathcal X\\|S|=n}}
 \pm\det P_S\det Q_{\mathcal X\setminus S}.        \tag{27}
$$



The exponential-minor formula is



$$
\det P_S=(-1)^n
 \frac{V(S)\Lambda(W_S)}{\prod_{u\in S}u!},
 \qquad W_S(x)=\prod_{u\in S}(x-u),                \tag{28}
$$



where $\Lambda((x)_j)=1$ for $0\leq j\leq n$.  Its valuation
analysis is independent of the arctangent function.  Among the
$n$-subsets, the only two which maximize
$\sum_{u\in S}v_2(u!)$ are



$$
S_0=\{2n+1,2n+2,\ldots,3n\},                     \tag{29}
$$





$$
S_*=\{2n\}\cup\{2n+2,2n+3,\ldots,3n\}.          \tag{30}
$$



If $n$ is even, the $S_0$ term in (27) attains every exponential,
square-kernel, and bordered-kernel lower bound; its normalized bordered
Machin factor is a unit by Sections 2--3.  Every other term has strictly
larger valuation: $S_*$ pays the positive extra $v_2(n)$, and every
other set loses in the factorial sum.

If $n$ is odd, the $S_*$ term attains all the lower bounds.  In the
only bordered equality case requiring the extra parity check, its first
row-to-pole difference is $3\pmod4$, so the normalized raw bordered
factor has valuation one and (21) shows that the Machin factor also has
valuation one.  The competing $S_0$ term has even (or zero)
$\Lambda(W_{S_0})$, and all remaining terms lose in the factorial sum.

Thus (27) has a unique summand of least $2$-adic valuation for every
$n\geq1$.  It cannot vanish in $\mathbb Q_2$, so



$$
\det T_n\ne0.                                     \tag{31}
$$



The reduction in Section 1 proves Theorem 1.  Once full row rank is
known, a nonzero kernel vector with $B(1)=0$ would again lead through
(6) to a nonzero vector in the kernel of $T_n$, which is impossible.
This proves (5) as well.  The reduction used only the implication
$B(1)=0\Rightarrow C(1)=0$, so it is unchanged for the rational border
$C(1)=\lambda B(1)$, proving the extension stated in Theorem 1.

## 5. Exact scope

The theorem establishes, for every degree, the existence and uniqueness
up to scale of the endpoint-matched type-I Hermite--Padé vector and the
nonvanishing of its coefficient $B(1)=C(1)$.  It does not establish

* nonvanishing of $A(1)+B(1)(e+\pi)$;
* decay of that specialized real linear form;
* a useful upper bound for the primitive endpoint coefficients after
  their gcd is removed; or
* algebraicity or transcendence of $e+\pi$.

Those are separate obligations.  In particular, this rank theorem does
not repair the large endpoint-primitive values observed through degree
18, and it is independent of the failed tentative $239$-adic valuation
pattern at degree 65.
