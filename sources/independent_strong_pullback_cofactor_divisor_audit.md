> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the strong pullback cofactor divisor

Date: 2026-08-26

## Scope and conclusion

This note independently audits the strengthened common-content assertion for
the endpoint-matched high-jet matrix attached to



$$
F(z)=4\arctan\frac{z}{2-z}.
$$



The assertion passes.  With the exact matrix convention below, every signed
maximal cofactor is divisible by



$$
\boxed{\Xi_n=\Lambda_n\Gamma_n\Omega_n^*},        \tag{1}
$$



where



$$
\Lambda_n=\left(\prod_{j=0}^{n-1}j!\right)^2,    \tag{2}
$$





$$
\Gamma_n=\prod_{t=0}^{n-2}
 2^{\delta_t}\operatorname{odd}(t!),
 \quad
 \delta_t=2q_t+1-s_2(q_t),
 \quad
 q_t=\left\lfloor\frac{t+1}{4}\right\rfloor,     \tag{3}
$$



and



$$
\Omega_n^*=\prod_{s=1}^{n-1}
 2^{\epsilon_s}\operatorname{odd}((s-1)!),
 \quad
 \epsilon_s=2d_s-s_2(d_s),
 \quad
 d_s=\left\lfloor\frac{s-1}{4}\right\rfloor.      \tag{4}
$$



Empty products are one.  The three factors are not inferred merely from
separate divisibilities of the same integer.  They arise successively as
literal column factors and then as factors of the residual determinant, so
they may be multiplied even when they share primes.

The asymptotic size is



$$
\log\Xi_n=2n^2\log n+O(n^2).                     \tag{5}
$$



This remains a common-cofactor divisor, not an exact Smith-normal-form
calculation and not a primitive endpoint-height theorem.

## 1. Exact matrix convention

Put



$$
\tau_m=F^{(m)}(0).
$$



The matrix $M_n$ has $2n+1$ rows and $2n+2$ columns.  Its columns,
in order, are



$$
B_0,B_1,\ldots,B_n,C_0,C_1,\ldots,C_n.           \tag{6}
$$



The first $2n$ rows are indexed by



$$
k=n+1,n+2,\ldots,3n,                              \tag{7}
$$



and have entries



$$
M_n(k,B_j)=(k)_j,\qquad
 M_n(k,C_j)=(k)_j\tau_{k-j}.                       \tag{8}
$$



The final endpoint row is



$$
(-1,-1,\ldots,-1\mid1,1,\ldots,1).              \tag{9}
$$



For a column $d$, the corresponding signed maximal cofactor is



$$
\Delta_d=(-1)^d\det M_n^{(d)},                    \tag{10}
$$



where $M_n^{(d)}$ deletes column $d$.  The sign is irrelevant to
divisibility.

The exact jet formula is



$$
\begin{aligned}
 \tau_{4q+1}&=(-1)^q\frac{2(4q)!}{4^q},\\
 \tau_{4q+2}&=(-1)^q\frac{2(4q+1)!}{4^q},\\
 \tau_{4q+3}&=(-1)^q\frac{(4q+2)!}{4^q},\\
 \tau_{4q+4}&=0.                                  \tag{11}
 \end{aligned}
$$



In particular, for a nonzero jet with $m=4q+r$,
$r\in\{1,2,3\}$,



$$
v_2(\tau_m)=2q+1-s_2(q),                         \tag{12}
$$



and



$$
\operatorname{odd}((m-1)!)\mid\tau_m.           \tag{13}
$$



## 2. Endpoint-row expansion and the two omitted columns

Fix a maximal cofactor.  One column $d$ of the original $2n+2$-column
matrix has already been deleted.  Expand the resulting square determinant
along the endpoint row (9).  In each nonzero expansion term, the endpoint
entry selects a second column $h\ne d$.  The remaining high determinant
therefore contains exactly the original columns other than $d,h$.

Thus **exactly two original columns are omitted** in each endpoint-row term.
They may be:

1. two $B$-columns;
2. one $B$- and one $C$-column, in either order;
3. two $C$-columns.

In particular, at least $n-1$ of the $n+1$ $C$-columns remain.  This
case split is the only column-counting input needed below.

## 3. The universal factorial column factor $\Lambda_n$

For both blocks,



$$
(k)_j=j!\binom{k}{j}.                             \tag{14}
$$



Consequently every retained high $B_j$-column has the literal factor
$j!$, and every retained high $C_j$-column has the same literal factor.
If the two omitted columns have degree indices $r,s\in\{0,\ldots,n\}$,
the retained factorial-column product is



$$
\frac{\left(\prod_{j=0}^n j!\right)^2}{r!s!}.
                                                               \tag{15}
$$



After division by $\Lambda_n$, this becomes



$$
\frac{(n!)^2}{r!s!}\in\mathbb Z,                 \tag{16}
$$



because $r!\mid n!$ and $s!\mid n!$.  Every endpoint-row term is
therefore divisible by $\Lambda_n$.

## 4. The extra $C$-column factor $\Gamma_n$

For a $C_j$-column set



$$
t=n-j.                                            \tag{17}
$$



In high row $k$, put $m=k-j$.  Then $m\geq t+1$.  The function



$$
q\longmapsto 2q+1-s_2(q)                         \tag{18}
$$



is strictly increasing: if $a$ is the number of trailing ones in the
binary expansion of $q$, its increment at $q+1$ is $1+a$.  The least
possible $q$ for a nonzero jet with $m\geq t+1$ is
$q_t=\lfloor(t+1)/4\rfloor$.  If $t+1\equiv0\pmod4$, the first jet is
zero and the next jet has exactly this $q_t$.

Equations (12)--(13) therefore prove the literal factorization



$$
(k)_j\tau_{k-j}
 =j!D_t\,U_{k,j},\qquad U_{k,j}\in\mathbb Z,       \tag{19}
$$



where



$$
D_t=2^{\delta_t}\operatorname{odd}(t!).          \tag{20}
$$



Zero entries satisfy (19) with $U_{k,j}=0$.

The numbers $D_t$ form a divisibility chain as $t$ increases:
$\operatorname{odd}((t-1)!)\mid\operatorname{odd}(t!)$, and
$\delta_t$ is nondecreasing.  Each endpoint-row term retains at least
$n-1$ $C$-columns, so its product of $D_t$-factors is divisible by the
product of the $n-1$ smallest members of this chain,



$$
D_0D_1\cdots D_{n-2}=\Gamma_n.                   \tag{21}
$$



Equations (14) and (19) are genuine simultaneous factorizations: a retained
$C_j$-column contains $j!D_t$, not merely an integer separately divisible
by $j!$ and by $D_t$.  Hence the conclusions of Sections 3 and 4 multiply,
and every endpoint-row term is divisible by $\Lambda_n\Gamma_n$.  There is
no coprimality assumption and no double-counting error.

## 5. The residual row-assignment factor $\Omega_n^*$

It remains to inspect the residual integer $U_{k,j}$ in (19).  Index the
high rows by



$$
s=k-n\in\{1,2,\ldots,2n\}.                       \tag{22}
$$



Then $m=k-j=s+t$.  For every odd prime $p$, (11) and (20) give



$$
\begin{aligned}
 v_p(U_{k,j})
 &=v_p\binom{k}{j}+v_p(\tau_{s+t})-v_p(t!)\\
 &\geq v_p((s+t-1)!)-v_p(t!)\\
 &\geq v_p((s-1)!).                               \tag{23}
 \end{aligned}
$$



The last inequality is exactly the integrality of



$$
\frac{(s+t-1)!}{t!(s-1)!}=\binom{s+t-1}{t}.       \tag{24}
$$



The same residual has a uniform dyadic factor.  For a nonzero jet put



$$
q_m=\left\lfloor\frac{s+t}{4}\right\rfloor,
 \qquad q_t=\left\lfloor\frac{t+1}{4}\right\rfloor.                \tag{25}
$$



Writing $t+1=4q_t+r$ and $s-1=4d_s+a$, with
$0\leq r,a<4$, gives



$$
q_m-q_t=d_s+\left\lfloor\frac{r+a}{4}\right\rfloor\geq d_s.     \tag{26}
$$



The function $\delta(q)=2q+1-s_2(q)$ is increasing.  Binary digit
subadditivity,



$$
s_2(q+d)\leq s_2(q)+s_2(d),                      \tag{27}
$$



therefore gives



$$
\begin{aligned}
 v_2(U_{k,j})
 &\geq\delta(q_m)-\delta(q_t)\\
 &\geq\delta(q_t+d_s)-\delta(q_t)\\
 &\geq2d_s-s_2(d_s)=\epsilon_s.                  \tag{28}
 \end{aligned}
$$



If $s+t\equiv0\pmod4$, the original entry is zero and is divisible by
every asserted factor.  Thus no zero-residue exception is needed.

Combining (23) and (28), after the column factors $j!D_t$ have already
been removed, a residual $C$-entry assigned to high row $s$ is still
divisible by



$$
R_s=2^{\epsilon_s}\operatorname{odd}((s-1)!).    \tag{29}
$$



Now expand a retained high determinant by the Leibniz formula.  Its retained
$C$-columns are assigned to the same number of distinct high rows.  There
are at least $n-1$ such rows.  The factors
$R_1,R_2,\ldots,R_{2n}$ form a divisibility chain: the odd factorial
parts chain, and $d\mapsto2d-s_2(d)$ is increasing.  Hence the product over
any set of at least $n-1$ distinct assigned rows is divisible by



$$
R_1R_2\cdots R_{n-1}=\Omega_n^*.                 \tag{30}
$$



Every Leibniz monomial, hence every retained high determinant and every
endpoint-row term, is divisible by the residual factor $\Omega_n^*$.
Because this factor is found **after** division by all $j!D_t$, it
multiplies $\Lambda_n\Gamma_n$ without overlap.  This proves (1).

### Sharpness of the bare residual row factor

The row estimate above is optimal if one uses only the jet quotient and
allows all column offsets.  More precisely, for fixed $s\geq1$, put



$$
V_{s,t}=\frac{\tau_{s+t}}{D_t}
 \quad(t\geq0,\ \tau_{s+t}\ne0).
$$



Then



$$
\gcd_{\substack{t\geq0\\\tau_{s+t}\ne0}}|V_{s,t}|=R_s.
$$



The lower divisibility is exactly (23) and (28), with the outer binomial
factor omitted.  For the reverse odd-prime inequality, fix an odd prime
$p$, choose $L$ above all base-$p$ digits of $s-1$, and choose
$c\in\{1,\ldots,p-1\}$ so that $s+cp^L\not\equiv0\pmod4$.  Such a
choice exists (for $p=3$, one of $c=1,2$ works).  With $t=cp^L$,
there is no base-$p$ carry in $(s-1)+t$, so Lucas's theorem gives



$$
\binom{s+t-1}{s-1}\not\equiv0\pmod p.
$$



Consequently $v_p(V_{s,t})=v_p((s-1)!)$.

For $p=2$, write $s-1=4d_s+a$.  If $a=0$, take $t=0$.  If
$a>0$, take $t+1=4\cdot2^L$ with $L$ above the binary support of
$d_s$.  In both cases the resulting jet is nonzero, adding $d_s$ to
the relevant binary quotient produces no carry, and equality holds in
(28).  Thus its 2-adic valuation is exactly $\epsilon_s$.

This sharpness statement does **not** prove that $\Omega_n^*$ is the full
row contribution for a fixed degree.  The actual entry in (19) also has the
finite-range binomial factor $\binom{n+s}{n-t}$.  It does show that a
larger degree-independent row factor cannot be obtained from
$\tau_{s+t}/D_t$ alone; any improvement must exploit that binomial,
the restriction $0\leq t\leq n$, or interactions between rows and
columns.

## 6. Asymptotic size

The hyperfactorial estimate gives



$$
\sum_{j<n}\log(j!)=\frac12n^2\log n+O(n^2).      \tag{31}
$$



Therefore



$$
\log\Lambda_n=n^2\log n+O(n^2).                 \tag{32}
$$



Removing powers of two from factorials changes the logarithm by only
$O(n^2)$, while $\sum\delta_t=O(n^2)$.  Hence



$$
\log\Gamma_n=\frac12n^2\log n+O(n^2),
 \qquad
 \log\Omega_n^*=\frac12n^2\log n+O(n^2).         \tag{33}
$$



Adding (32)--(33) proves (5).

## 7. Exact finite verification through degree 15

The archived exact matrix generator is

```text
scripts/mobius_arctan_hp_probe.py
```

During this audit, for every $1\leq n\leq15$, all $2n+2$ maximal minors
were recomputed over $\mathbb Z$, their gcd was taken, and divisibility by
$\Xi_n$ was checked.  The archived probe obtains the same gcd independently
from a primitive kernel vector and one nonzero cofactor.  The following table
gives decimal digit counts.  The last column is the number of digits left in
the exact cofactor gcd after division by $\Xi_n$.

| $n$ | actual gcd | $\Lambda_n$ | $\Gamma_n$ | $\Omega_n^*$ | $\Xi_n$ | quotient |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | 1 | 1 | 1 | 1 | 1 | 1 |
| 3 | 3 | 1 | 1 | 1 | 2 | 2 |
| 4 | 6 | 3 | 1 | 1 | 4 | 3 |
| 5 | 12 | 5 | 2 | 1 | 8 | 4 |
| 6 | 20 | 10 | 4 | 2 | 14 | 7 |
| 7 | 32 | 15 | 5 | 3 | 23 | 10 |
| 8 | 47 | 23 | 8 | 5 | 34 | 13 |
| 9 | 65 | 32 | 11 | 8 | 50 | 15 |
| 10 | 87 | 43 | 15 | 11 | 68 | 20 |
| 11 | 115 | 56 | 20 | 16 | 91 | 25 |
| 12 | 144 | 71 | 25 | 21 | 116 | 29 |
| 13 | 179 | 89 | 32 | 27 | 146 | 33 |
| 14 | 219 | 108 | 39 | 34 | 180 | 39 |
| 15 | 263 | 130 | 47 | 42 | 218 | 46 |

At $n=15$, the exact common cofactor gcd has 263 digits,
$\Xi_{15}$ has 218 digits, and the quotient has 46 digits.  Its 2-adic
valuation is 315, while $v_2(\Xi_{15})=220$.

The finite computation is corroboration, not a substitute for Sections
2--5.  Conversely, (1) is only a proved divisor: the nontrivial quotient in
the last column shows that the full determinantal divisor has not yet been
identified.

## 8. Prime-by-prime residual experiment

Let



$$
Q_n=\frac{\gcd_d(\Delta_d)}{\Xi_n}.
$$



The following are complete exact factorizations, not floating-point
estimates.  They were obtained independently from all maximal minors and
are also recorded by the archived exact probe.

| $n$ | factorization of $Q_n$ | $\log(Q_n)/n^2$ |
|---:|:---|---:|
| 1 | $3$ | 1.0986 |
| 2 | $2$ | 0.1733 |
| 3 | $2^3 3$ | 0.3531 |
| 4 | $2^5 3^2$ | 0.3539 |
| 5 | $2^7 3^2 5$ | 0.3463 |
| 6 | $2^{12}3^3 5^2$ | 0.4120 |
| 7 | $2^{18}3^4 5^2 7$ | 0.4497 |
| 8 | $2^{24}3^4 5^2 7^2$ | 0.4397 |
| 9 | $2^{29}3^6 5^2 7^2$ | 0.4173 |
| 10 | $2^{38}3^8 5^3 7^2$ | 0.4385 |
| 11 | $2^{48}3^8 5^4 7^3 11$ | 0.4689 |
| 12 | $2^{58}3^9 5^4 7^2 11^2$ | 0.4529 |
| 13 | $2^{68}3^{10}5^4 7^2 11^2 13$ | 0.4486 |
| 14 | $2^{81}3^{10}5^4 7^3 11^2 13^2$ | 0.4558 |
| 15 | $2^{95}3^{11}5^5 7^4 11^2 13^2$ | 0.4608 |

For every $2\leq n\leq15$, no prime larger than $n$ occurs.  (The
exceptional degree $n=1$ has $Q_1=3$.)  For $2\leq n\leq15$,
the odd part of $Q_n$ equals



$$
\frac{\operatorname{odd}(n!)^2}{\operatorname{odd}(n)}
$$



except for one additional factor $7$ at $n=11$.  This striking finite
pattern is **not** asserted as a theorem.  The normalized logarithms in the
last column are compatible with $Q_n=\exp(O(n^2))$, rather than another
factor $\exp(cn^2\log n)$, but fifteen degrees cannot prove such an
asymptotic upper bound.

For a full-row-rank integer matrix, $\gcd_d(\Delta_d)$ is its top
determinantal divisor, equivalently the product of all nonzero Smith
invariant factors.  Direct exact Smith computations through $n=14$
agree with the cofactor gcds above.  They reveal no further uniform
row/column factorization; they do not constitute an all-degree Smith theorem.

The exact artifacts used for these checks are frozen as follows:

```text
d812595d92abff631366a889aa8c6e8a13402ace684c93c1fffe56b8032981b6  scripts/mobius_arctan_hp_probe.py
ff0405c94960eb27940b4684de0dcab05cab5b6dd0311abc27f5ed1d85a7691b  results/mobius_arctan_hp_n15.json
dcde8ac063fe704b5eaa3caaee3ef5a4bebf44d24192b7da9f4fd9e5901ee3fa  scripts/mobius_arctan_hp_smith_probe.py
cfc05cc5782a14bc9ff427b60ce96276d34e44ea511e771c1907a500fde84213  results/mobius_arctan_hp_smith_n14.json
```

## 9. Accepted conclusion and remaining question

The strengthened divisor $\Lambda_n\Gamma_n\Omega_n^*$ is valid, and the
three factors multiply without any hidden coprimality premise.  It removes a
forced factor of size



$$
\exp(2n^2\log n+O(n^2))                           \tag{34}
$$



from the raw signed-cofactor vector before primitive normalization.

The remaining exact gcd is still substantial in the tested degrees.  A full
Smith-normal-form description of $M_n$ is not proved here and is the next
arithmetic question.  Nothing in this audit establishes endpoint smallness,
nonvanishing in all degrees, irrationality, or transcendence of $e+\pi$.
