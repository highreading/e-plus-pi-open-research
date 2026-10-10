> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 210 — exact endpoint-row contents, anchor recurrence, and a global rank-one ceiling

Date: 2026-08-31

## 1. Scope and verdict

This item continues Route 1 from Items 175, 196, 205, 206, and 208.  It
studies only the two first rank-one gates $A_0,B_0$.  It does not identify
the second-lift digit $A_1$, and it does not claim a new valuation copy.

Put



$$
F_j={u^{3j+2}\over Q^{2j+2}},\qquad
 u=x(1-x),\qquad Q=(x+1)(x^2+1),\qquad j\ge1.        \tag{1.1}
$$



The main conclusions are as follows.

**PROVED — exact rank classification at every admissible prime.**  Let
$K=2j+2$, $A=3j+2$, and let $\mu_j$ be the exact rational
$2\times2$ anchor minor defined in Section 2.  Every denominator is a
$p$-unit for $p>K$.  Then



$$
\begin{array}{c|c}
K<p\le A&\operatorname {rank}_p(r^A_j,r^B_j)=0,\\
p>A&\operatorname {rank}_p(r^A_j,r^B_j)=1
       \iff \mu_j\equiv0\pmod p,\\
p>A&\operatorname {rank}_p(r^A_j,r^B_j)=2
       \iff \mu_j\not\equiv0\pmod p.
\end{array}                                             \tag{1.2}
$$



In particular, rank zero is impossible above $3j+2$.  If
$c^A_j,c^B_j$ are the two canonical scalar row contents, then the exact
large-prime radical identity is



$$
\{p>K:p\mid\gcd(c^A_j,c^B_j)\}
 =\{p:K<p\le A\}.                                     \tag{1.3}
$$



**PROVED — the rational anchor has one explicit diagonal obstruction.**
The common kernel identity of Item 206 can be sharpened to



$$
\boxed{\mu_j=L_jH_j,\qquad H_j\ne0,}                 \tag{1.4}
$$



where $L_j$ is the logarithmic coordinate of $F_j\,dx$, and



$$
L_j=2^{-j}\ell_j,\qquad
 \ell_j=[y^{2j+1}]{(y-1)^{3j+2}\over(1+y^2)^{2j+2}}. \tag{1.5}
$$



Thus a rationally singular band, on which every sufficiently large prime
has rank one, exists exactly when the explicit integer $\ell_j$ is zero.
This distinguishes such a band from an ordinary modular rank-one prime,
which merely divides the numerator of a nonzero $\mu_j$.

**PROVED — an order-three recurrence with an exact telescoping
certificate.**  The integers $\ell_j$ satisfy the recurrence in Section
5 for every $j\ge1$.  Both outer coefficients are nonzero, so three
consecutive zeros are impossible.  The recurrence is sign-indefinite and
does not by itself exclude an isolated zero.

**FINITE, EXACT — no diagonal zero through $j=20{,}000$.**  A forward
recurrence scan, cross-checked against the independent terminating
binomial formula through $j=80$, finds



$$
\ell_j\ne0\qquad(1\le j\le20{,}000). \tag{1.6}
$$



This finite theorem yields a rigorous global capacity ceiling even without
extrapolating (1.6).  Every modular determinant prime in a fixed nonzero
band has finite support.  Every still-unresolved rationally singular band
lies above $20{,}000$, so all rank-one rows together have



$$
\limsup_{m\to\infty}{W_{\rm rank1}(m)\over m}
 <{2\over3(20{,}001)}={2\over60{,}003}
 =0.00003333166675\ldots .                            \tag{1.7}
$$



Equivalently, in the archive's normalized units this is



$$
{1\over9(20{,}001)}={1\over180{,}009}
 =0.00000555527779\ldots\quad\hbox{per }6m.           \tag{1.8}
$$



The current Route-1 gap requires
$0.1177979020165907\ldots$ per $m$, or
$G=0.01963298366943179\ldots$ per $6m$.  Therefore the entire
rank-one determinant-exception family is far too small to close the gap
by itself, even if every unresolved row contributed optimally.

**OPEN.**  The all-$j$ statement $\ell_j\ne0$ remains unproved, so a
literal zero-rate theorem for the singular row family is not claimed.
The surviving scalar equation on rank-one rows still has a moving
$s$-dependence.  Nothing here proves a new content exponent or a
conclusion about $e+\pi$.

## 2. Canonical rows, scalar contents, and the anchor

For $a\in\{-1,i,-i\}$, let



$$
C_j=(R_j,L_j,E_j),\qquad
 C_{j,a}=(R_{j,a},L_{j,a},E_{j,a})                  \tag{2.1}
$$



be the endpoint-coordinate vectors of $F_j\,dx$ and $F_j\,dx/(x-a)$.
Define



$$
w^A_{j,a}=R_jL_{j,a}-L_jR_{j,a},\qquad
 w^B_{j,a}=E_jL_{j,a}-L_jE_{j,a}.                    \tag{2.2}
$$



Conjugation gives two rational rows acting on
$\bigl(V(-1),\operatorname {Re}V(i),\operatorname {Im}V(i)\bigr)$:



$$
r^\square_j=
 \bigl(w^\square_{j,-1},\,2\operatorname {Re}w^\square_{j,i},
                         -2\operatorname {Im}w^\square_{j,i}\bigr),
 \qquad\square\in\{A,B\}.                            \tag{2.3}
$$



For either row, take the least common denominator of its three reduced
entries and clear it.  The positive gcd of the resulting three integers is
the canonical row content $c^A_j$ or $c^B_j$.  This convention is
independent for the two rows and introduces no prime $p>K$.

The universal kernel gives



$$
2r^\square_{j,1}-r^\square_{j,2}-r^\square_{j,3}=0. \tag{2.4}
$$



Consequently all three $2\times2$ minors are controlled by one scalar:



$$
r^A_j\times r^B_j=\mu_j(2,-1,-1),                  \tag{2.5}
$$



or, explicitly,



$$
\mu_j=r^A_{j,2}r^B_{j,1}-r^A_{j,1}r^B_{j,2}.       \tag{2.6}
$$



This exact rational $\mu_j$, rather than an independently primitive
minor, is the anchor used in the rank classification.

## 3. Closed coefficient formulas for both row contents

The following finite coefficient extraction is an exact closed formula for
every entry of (2.3), and hence for both scalar contents and $\mu_j$.
It also proves the denominator assertion used above.

Let ${\cal R}=\{-1,i,-i\}$.  For $a\in{\cal R}$,
$\alpha\in{\cal R}$, and



$$
t_{a,\alpha}=K+\mathbf1_{a=\alpha},                 \tag{3.1}
$$



put



$$
S_{j,a,\alpha}(z)=
 {u(\alpha+z)^A\over
  \prod_{\substack{\beta\in{\cal R}\\\beta\ne\alpha}}
  (\alpha-\beta+z)^{K+\mathbf1_{a=\beta}}}.          \tag{3.2}
$$



The principal-part coefficient of order $n$ at $\alpha$ is



$$
c_{j,a,\alpha,n}=[z^{t_{a,\alpha}-n}]S_{j,a,\alpha}(z),
 \qquad1\le n\le t_{a,\alpha}.                       \tag{3.3}
$$



For the base vector, remove every indicator in (3.1)--(3.3) and use
$t_\alpha=K$.  The coordinates are



$$
\begin{aligned}
 R_{j,a}&=\sum_{\alpha\in{\cal R}}
 \sum_{n=2}^{t_{a,\alpha}}{c_{j,a,\alpha,n}\over n-1}
 \left((-\alpha)^{1-n}-(1-\alpha)^{1-n}\right),\\
 L_{j,a}&=4c_{j,a,-1,1}+2(c_{j,a,i,1}+c_{j,a,-i,1}),\\
 E_{j,a}&=2i(c_{j,a,i,1}-c_{j,a,-i,1}).              \tag{3.4}
\end{aligned}
$$



Equations (2.2)--(2.6) and (3.1)--(3.4) are the promised exact functions
of $j$.  The only rational denominators in (3.4) come from the Gaussian
root differences, whose norms are powers of two, and the integers
$1,\ldots,K$.  Thus all denominators are units at every $p>K$.

For reference, the exact finite ledger through $j=12$ is



$$
\begin{array}{c|r|r|r|l}
j&c^A_j&c^B_j&|\det(\operatorname {prim}r^A,
 \operatorname {prim}r^B)_{1,2}|&p>A\text{ rank one}\\ \hline
1&5&25&1&-\\
2&7&49&4&-\\
3&33&103455&1&19\;(B\text{-row zero})\\
4&143&143143&54&-\\
5&221&341887&455&-\\
6&1615&7824675&87&29\;(\text{parallel})\\
7&7429&12748899471&1343&79\;(\text{parallel})\\
8&50255&23894996125&374&-\\
9&14007&701400875175&16783&1291\;(\text{parallel})\\
10&20677&1250549612325&9920&-\\
11&22475&414938980535625&8123&59\;(B\text{-zero}),8123\;(\text{parallel})\\
12&99789&202632178157829&5164698&1597\;(\text{parallel})
\end{array}                                           \tag{3.5}
$$



This table is finite evidence only; the formulas and rank theorem are not.

## 4. Proof of the all-prime rank theorem

The partial fractions



$$
{2\over x+1}+{-1-i\over x-i}+{-1+i\over x+i}={4\over Q(x)} \tag{4.1}
$$



and the polynomial identity



$$
3u'Q-2uQ'-8+5Q=0             \tag{4.2}
$$



give



$$
{4F_j\over Q}\,dx={5\over2}F_j\,dx
             +d\!\left({uF_j\over2j+2}\right).       \tag{4.3}
$$



The primitive vanishes at both endpoints.  Hence both rows annihilate
$(2,-1,-1)$, proving (2.4)--(2.5).

It remains to show that there is no second cohomological relation when
$p>A$.  Use



$$
y={x+1\over1-x},\qquad D=y(1+y^2).                  \tag{4.4}
$$



Up to a nonzero scalar,



$$
F_j\,dx={(y-1)^A\over D^K}\,dy.                    \tag{4.5}
$$



A general pole combination minus a scalar multiple of the base has the
form



$$
{(y-1)^AS(y)\over D^{K+1}}\,dy,\qquad\deg S\le3.   \tag{4.6}
$$



If it is relatively exact, its primitive is $R/D^K$, with
$\deg R<3K$, and vanishes at $y=1,\infty$.  The order at $y=1$
forces



$$
R=(y-1)^{A+1}T.              \tag{4.7}
$$



Substitution gives



$$
S=(A+1)DT+(y-1)(DT'-KD'T).                          \tag{4.8}
$$



If $d=\deg T\ge1$, then $d\le3j+2$, while the leading coefficient
of the right side in degree $d+3$ is



$$
d-3j-3\ne0.                 \tag{4.9}
$$



This contradicts $\deg S\le3$.  Hence $T$ is constant and (4.3)
spans the complete relation space.  The same proof works in
characteristic $p>A$, because every nonzero integer in (4.9) has
absolute value less than $p$.

Therefore the four classes consisting of the base and the three pole
divisions span the full three-dimensional endpoint-coordinate space, with
only the relation (4.3).  They cannot make both rows zero when $p>A$.
Together with (2.5), this proves the second and third lines of (1.2).

For $K<p\le A$, Item 206's Cartier degree argument applies: after
Frobenius extraction, the base and one-pole numerator degrees are $p-2$
and $p-3$, so both rows are zero.  This proves the first line of (1.2)
and the radical identity (1.3).

For the anchor factorization, take



$$
h_0={1\over x+1},\qquad h_1={2x\over x^2+1}.        \tag{4.10}
$$



Writing $C_0=C(F_j\,dx)$, $C_1=C(h_0F_j\,dx)$, and
$C_2=C(h_1F_j\,dx)$, direct determinant expansion gives



$$
\mu_j=L_j\det(C_0,C_1,C_2).                         \tag{4.11}
$$



The determinant is nonzero by the uniqueness just proved: the universal
relation (4.1) uses the independent imaginary pole direction and does not
lie in the span of $1,h_0,h_1$.  Finally, taking the residue at $y=0$
in (4.5) gives (1.5), proving (1.4).

## 5. Exact recurrence and what it does not prove

The terminating formula is



$$
\ell_j=\sum_{t=0}^{j}(-1)^{j+1+t}
 {3j+2\choose2j+1-2t}{2j+1+t\choose t}.             \tag{5.1}
$$



For $n\ge1$, put



$$
P_0(n)\ell_n+P_1(n)\ell_{n+1}
       +P_2(n)\ell_{n+2}+P_3(n)\ell_{n+3}=0,          \tag{5.2}
$$



where



$$
\begin{aligned}
P_0={}&-9(n+1)(3n+4)(3n+5)(3n+7)(3n+8)
       (165n^2+895n+1166),\\
P_1={}&6(2n+3)(3n+7)(3n+8)
       (106095n^4+893770n^3+2704043n^2+3484796n+1609084),\\
P_2={}&-48(n+2)(2n+3)(2n+5)(3n+8)
       (495n^3+3345n^2+7103n+4533),\\
P_3={}&64(n+2)(n+3)(2n+3)(2n+5)(2n+7)
       (165n^2+565n+436).
                                                               \tag{5.3}
\end{aligned}
$$



This recurrence is proved, not guessed.  Set



$$
R(y)={(y-1)^2\over y^2(1+y^2)^2},\qquad
 J(y)={(y-1)^3\over y^2(1+y^2)^2},                  \tag{5.4}
$$



so that
$\ell_n=\operatorname {Res}_{y=0}R(y)J(y)^n\,dy$.
The certificate contains an explicit polynomial $N_n(y)$, of degrees
$(6,15)$ in $(n,y)$, for which



$$
C_n={(y-1)N_n(y)\over y^5(1+y^2)^5},\qquad
 C_n'+C_n\left({R'\over R}+n{J'\over J}\right)
 =\sum_{k=0}^{3}P_k(n)J^k.                            \tag{5.5}
$$



Multiplication by $RJ^n$ makes the right side an exact derivative;
its residue is zero, proving (5.2).  The checker verifies (5.5) as an
identically zero bivariate polynomial, rather than at sampled values.

Both $P_0(n)$ and $P_3(n)$ are nonzero for $n\ge1$.  Hence (5.2)
propagates in both directions and forbids three consecutive zeros.  It
does not forbid isolated zeros, and its alternating signs supply no
positivity induction.  The still-missing all-$j$ nonzero theorem is the
precise obstruction to upgrading (1.7) to a literal zero-rate statement.

## 6. Global log-weight theorem and quantifiers

Fix $J$ for which $\ell_j\ne0$ has been verified for every
$1\le j\le J$.  Then $\mu_j$ is a fixed nonzero rational number in
each such band.  It has finitely many prime divisors.  For fixed $(j,p)$,
the cell equation



$$
2m+1=(j+1)p-s,\qquad0\le s\le{p-3\over3}            \tag{6.1}
$$



allows only finitely many $m$.  Thus all determinant-singular rows with
$j\le J$ have asymptotic coefficient zero.

No assertion about $\ell_j$ is made for $j>J$.  Bounding every one of
those bands by the whole rank-one cell gives



$$
\begin{aligned}
 \limsup_{m\to\infty}{W_{\rm rank1}(m)\over m}
 &\le\sum_{j>J}\left({6\over3j+2}-{2\over j+1}\right)\\
 &=\sum_{j>J}{2\over(3j+2)(j+1)}
 <{2\over3(J+1)}.                                    \tag{6.2}
\end{aligned}
$$



Taking the certified $J=20{,}000$ proves (1.7)--(1.8).  This argument
does not silently extrapolate the finite scan: every unverified band is
charged at full capacity.

## 7. Surviving equations on genuine rank-one rows

On rank one, one must retain the surviving scalar row.  It is invalid to
apply the regular-rank common-content equivalence.

At $(j,p)=(3,19)$, the $B$-row is zero and the normalized surviving
$A$-equation is



$$
V(-1)+17\operatorname {Re}V(i)
                    +4\operatorname {Im}V(i)=0\pmod {19}. \tag{7.1}
$$



For the admissible residuals $s=1,3,5$, the exact gate pairs are



$$
(A_0,B_0)=(9,0),(0,0),(2,0). \tag{7.2}
$$



Thus only $s=3$ is joint.

At $(j,p)=(7,79)$, both rows are nonzero and parallel.  This corrects
the tentative description of this witness as another zero $B$-row.  The
normalized surviving equation is



$$
V(-1)+21\operatorname {Re}V(i)
                    +60\operatorname {Im}V(i)=0\pmod {79}. \tag{7.3}
$$



Among the thirteen admissible odd residuals $1\le s\le25$, the exact
finite replay finds a joint zero only at $s=15$.  These two examples
illustrate why rank one is a one-equation moving problem, not automatic
common content.

## 8. Certificate and status

The standard-library checker

    work/item210_rankone_anchor_certificate.py

performs the following exact tasks.

1. It reconstructs the rational rows and their two canonical contents
   from the pinned Item 175 coordinate engine.
2. It verifies (1.5), (2.4)--(2.6), the row contents, and every rank-drop
   prime through $j=12$.
3. It verifies the telescoping identity (5.5) symbolically over
   $\mathbb Z[n,y]$.
4. It scans (5.2) through $j=20{,}000$, checks exact divisibility at
   every step, and independently checks (5.1) through $j=80$.
5. It reproduces the surviving equations and all residual rows in
   (7.1)--(7.3).
6. It records both capacity units and compares them with the current
   Route-1 gap.

Canonical and replay JSON outputs are required to be byte-identical.  The
portable work artifact set is

    work/item210_rankone_anchor_report.md
    work/item210_rankone_anchor_certificate.py
    work/item210_rankone_anchor_certificate.json
    work/item210_rankone_anchor_certificate_replay.json
    work/item210_rankone_anchor_hashes.sha256

Status summary:

- **PROVED:** the exact row-content radical and all-prime rank
  classification (1.2)--(1.3).
- **PROVED:** the anchor factorization (1.4)--(1.5) and the order-three
  telescoper recurrence.
- **PROVED FROM A FINITE EXACT PREFIX:** the global ceiling
  $2/60003$ per $m$, or $1/180009$ per $6m$, which cannot close
  the current Route-1 gap alone.
- **FINITE:** no $\ell_j$ zero through $20{,}000$, row ledger through
  $j=12$, and the two selected moving residual scans.
- **OPEN:** $\ell_j\ne0$ for all $j$, a zero-rate theorem rather than
  the displayed ceiling, the surviving moving equation in general,
  $A_1$, any new valuation copy, and the arithmetic nature of $e+\pi$.
