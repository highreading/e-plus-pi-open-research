> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Positive pole truncation closes the root-of-unity $\Gamma$ border

## A canonical-product theorem for all three Hermite-cardinal families

Checked: 2026-08-27 UTC

## 1. Verdict

This note continues the frozen files
`sources/root_unity_gamma_logistic_minor_audit.md` and
`sources/root_unity_gamma_augmented_newton_audit.md`.  It does not modify
them.

The confluent-Newton positivity lemma left open in the latter note is true.
More precisely, it follows from a positive finite-pole projection theorem for
the canonical products



$$
\cos(\pi\sqrt{-x})
   =\prod_{r\ge1}\left(1+\frac{x}{(r-\tfrac12)^2}\right),
 \qquad
 \frac{\sin(\pi\sqrt{-x})}{\pi\sqrt{-x}}
   =\prod_{r\ge1}\left(1+\frac{x}{r^2}\right).              \tag{1}
$$



The proof is elementary once the right entire jet extensions are chosen.  A
tail factor has the form



$$
1+\frac{s^2x}{A_\ell}
   =\frac{s^2}{A_\ell}\left(x+\frac{A_\ell}{s^2}\right),
 \qquad \frac{A_\ell}{s^2}>A_k,                             \tag{2}
$$



where every pole retained in the first $k$ blocks has rate at most $A_k$.
Multiplication by (2), followed by deletion of the polynomial part, maps a
positive sum of reciprocal products to another positive sum.  Passing to the
locally uniform infinite-product limit is legitimate because the Hermite
remainder projection depends continuously on finitely many jets.

In fact the proof gives the stronger conclusion required in the preceding
audit: every coefficient in the *ordered* repeated-rate Newton expansion is
strictly positive.  It applies to

1. the generic $\Lambda_0$ row for even $m$, using the cosine product;
2. the generic $\Lambda_0$ row for odd $m$, using the sinc product; and
3. the parity-defect $\Lambda_1$ row for odd $m,n$, again using the sinc
   product.

Together with the all-parameter shifted-coordinate theorem in the preceding
audit, this proves



$$
\boxed{\Gamma\ne0\quad\text{for every }m\ge2
        \text{ and }n\ge D\ge2.}                            \tag{3}
$$



For $m=1$, the already proved classification remains



$$
\Gamma=0\quad\Longleftrightarrow\quad
 n\text{ is even and }D\text{ is odd}.                      \tag{4}
$$



Equation (3) does **not** prove that the corrected endpoint polynomial
$\Delta=W-\Gamma$ is nonzero.  It also gives no primitive-height or endpoint
value estimate.  Thus it gives no transcendence conclusion for $e+\pi$.

The new exact replay files are

* `scripts/root_unity_gamma_positive_pole_truncation_certificate.py`;
* `results/root_unity_gamma_positive_pole_truncation_certificate.json`.

## 2. The unified remainder theorem

Let



$$
0<A_1<A_2<\cdots,\qquad
 \sum_{j\ge1}\frac1{A_j}<\infty,                            \tag{5}
$$



and define the genus-zero canonical product and its first $k$ factors by



$$
\mathcal P(x)=\prod_{j\ge1}\left(1+\frac{x}{A_j}\right),
 \qquad
 \mathcal P_k(x)=\prod_{j=1}^k
                    \left(1+\frac{x}{A_j}\right).          \tag{6}
$$



Fix positive integers $\nu,h$ with



$$
h\in\{\nu,\nu+1\}.                 \tag{7}
$$



Let $w$ be a nonnegative integrable function on $[0,1]$, positive on
some open subinterval of $(0,1)$, and put



$$
F(x)=\int_0^1 w(s)\mathcal P(s^2x)^\nu\,ds.                \tag{8}
$$



Local uniform convergence in (6) makes $F$ entire.  Let
$\mathscr R_{k,h}F$ be the unique polynomial of degree less than $kh$
whose derivatives through order $h-1$ agree with those of $F$ at every
$-A_j$, $1\le j\le k$.  Equivalently,



$$
F-\mathscr R_{k,h}F\quad\text{is divisible, as an entire function, by}
 \quad\mathcal P_k^h.                                       \tag{9}
$$



List each rate $A_j$, $1\le j\le k$, exactly $h$ times, in
nondecreasing order:



$$
\lambda_1\le\lambda_2\le\cdots\le\lambda_{kh}.           \tag{10}
$$



> **Positive pole-truncation theorem.**  Under (5)--(8), there are strictly
> positive real numbers $\gamma_0,\ldots,\gamma_{kh-1}$ such that
>
> 

$$
>  \mathscr R_{k,h}F(x)
>    =\sum_{d=0}^{kh-1}\gamma_d
>       \prod_{j=1}^{d}(x+\lambda_j).                       \tag{11}
>
$$



Consequently



$$
\frac{\mathscr R_{k,h}F(x)}
      {\prod_{j=1}^{kh}(x+\lambda_j)}
  =\sum_{d=0}^{kh-1}
    \frac{\gamma_d}{\prod_{j=d+1}^{kh}(x+\lambda_j)}       \tag{12}
$$



is strictly completely monotone on $(0,\infty)$.  The positive constants
which convert $\mathcal P_k^h$ to the monic denominator in (12) do not
alter any sign.

The theorem is special to the ordered canonical-product situation.  It does
not assert that an arbitrary finite principal part of an arbitrary completely
monotone meromorphic function is completely monotone.

## 3. The algebraic finite-pole lemma

### 3.1 Positive reciprocal-product cone

For the finite ordered list (10), set



$$
D(x)=\prod_{j=1}^{kh}(x+\lambda_j),\qquad
 Q_I(x)=\frac1{\prod_{i\in I}(x+\lambda_i)}                 \tag{13}
$$



for every nonempty submultiset $I$ of the indexed list.  Let
$\mathscr C_\lambda$ be the cone of finite nonnegative linear combinations
of the $Q_I$.

For $0<s\le1$, a tail factor with $\ell>k$ acts on one reciprocal
product as follows.  Choose any $i\in I$.  Then



$$
\left(1+\frac{s^2x}{A_\ell}\right)Q_I
 =\frac{s^2}{A_\ell}Q_{I\setminus\{i\}}
  +\left(1-\frac{s^2\lambda_i}{A_\ell}\right)Q_I.          \tag{14}
$$



If $I\setminus\{i\}$ is empty, its term is polynomial and is discarded by
the polar-part projection.  Both displayed coefficients are nonnegative, and
the second is strictly positive, because



$$
A_\ell>A_k\ge\lambda_i.                   \tag{15}
$$



At $s=0$, the tail factor is one, so the same conclusion follows directly.
Discarding a polynomial term after each step is equivalent to discarding it
only at the end, because every later tail factor is itself a polynomial and
can never recreate a pole.
Iterating (14) proves:

> Multiplication by any finite collection of tail factors, followed by
> deletion of the polynomial part, preserves $\mathscr C_\lambda$.

The polar part of the first $k$ product blocks already lies in this cone.
Indeed,



$$
\frac{\mathcal P_k(s^2x)^\nu}{\mathcal P_k(x)^h}
 =\prod_{j=1}^k
   \left(s^2+(1-s^2)\frac{A_j}{x+A_j}\right)^\nu
   \left(\frac{A_j}{x+A_j}\right)^{h-\nu}.                 \tag{16}
$$



Every coefficient produced by expanding (16) is nonnegative.  If an empty
reciprocal product occurs when $h=\nu$, it is a polynomial constant and is
discarded.  Equations (14)--(16) therefore show that, for every finite cutoff
$L\ge k$, the polar part over the first $k$ poles of



$$
\frac{\mathcal P_L(s^2x)^\nu}{\mathcal P_k(x)^h}           \tag{17}
$$



belongs to $\mathscr C_\lambda$.

### 3.2 Completing a subproduct to the ordered Coxian basis

Membership in $\mathscr C_\lambda$ is already enough for complete
monotonicity, but (11) requires the particular ordered suffix basis.  The
needed completion is also sign preserving.

Let $I\ne\varnothing$, and write the complementary indices as



$$
j_1<j_2<\cdots<j_q.                           \tag{18}
$$



Put $P_d(x)=\prod_{i=1}^{d}(x+\lambda_i)$, with $P_0=1$.  The polynomial



$$
M_I(x)=\frac{D(x)}{\prod_{i\in I}(x+\lambda_i)}
                    =\prod_{r=1}^q(x+\lambda_{j_r})         \tag{19}
$$



has a nonnegative expansion in $P_0,\ldots,P_q$.  This follows by induction
on $r$.  If $d\le r-1$, then $j_r\ge r\ge d+1$, and hence



$$
(x+\lambda_{j_r})P_d
   =P_{d+1}+(\lambda_{j_r}-\lambda_{d+1})P_d,               \tag{20}
$$



with both coefficients nonnegative.  Starting with $P_0$, equation (20)
proves the assertion.

Divide (19) by $D$.  Every $Q_I$ is therefore a nonnegative combination
of the ordered suffixes



$$
\frac{P_d(x)}{D(x)}
              =\frac1{\prod_{j=d+1}^{kh}(x+\lambda_j)}.    \tag{21}
$$



Thus every finite polar part in (17) has nonnegative ordered coefficients.

## 4. Infinite-product passage and strictness

### 4.1 Continuity of the Hermite projection

Condition (5) implies that $\mathcal P_L\to\mathcal P$ locally uniformly,
uniformly also after substituting $s^2x$ with $0\le s\le1$ on a fixed
compact $x$-set.  Hence



$$
\int_0^1w(s)\mathcal P_L(s^2x)^\nu ds
       \longrightarrow F(x)                                \tag{22}
$$



locally uniformly.

The map $f\mapsto\mathscr R_{k,h}f$ is a continuous linear map for local
uniform convergence.  To see this without any abstract machinery, choose
small disjoint circles around $-A_1,\ldots,-A_k$.  Local uniform convergence
and Cauchy's formula give convergence of the finitely many derivatives
$f^{(a)}(-A_j)$, $0\le a<h$.  The coefficients of the Hermite remainder
are fixed linear combinations of those jets.  They therefore converge.

Equivalently, the polar-part projection



$$
\operatorname {pp}_{k,h}\!\left(\frac f{\mathcal P_k^h}\right)
       :=\frac{\mathscr R_{k,h}f}{\mathcal P_k^h}            \tag{23}
$$



is continuous.  It is also linear, so it commutes with the $s$-integration
in (8).  Taking $L\to\infty$ in (17) proves that every ordered coefficient
in (11) is nonnegative.

### 4.2 Why every coefficient is strictly positive when $h=\nu$

Fix $d\in\{0,\ldots,kh-1\}$, and let



$$
I_d=\{d+1,\ldots,kh\}.             \tag{24}
$$



When $h=\nu$, the expansion of (16) contains the reciprocal product
$Q_{I_d}$ with a strictly positive coefficient for every $0<s<1$: in
each equal-rate block, simply choose the number of reciprocal terms prescribed
by the suffix $I_d$.

For every later tail factor, follow the second, retaining branch in (14),
using one fixed $\lambda_i$ with $i\in I_d$.  The infinite retained
coefficient contains



$$
\prod_{\ell>k}
 \left(1-\frac{s^2\lambda_i}{A_\ell}\right)^\nu>0.         \tag{25}
$$



The product is strictly positive because every factor is positive and
$\sum_{\ell>k}A_\ell^{-1}<\infty$.  Thus the ordered suffix (21) with index
$d$ has a strictly positive contribution for every $0<s<1$.  Integration
against $w$ makes $\gamma_d>0$.  Possible vanishing at $s=0$ or $s=1$
is irrelevant.

### 4.3 Why every coefficient is strictly positive when $h=\nu+1$

Now the last factor in (16) forces at least one copy of every first-block
rate into the denominator.  The full reciprocal product $Q_{I_0}=1/D$
nevertheless occurs with a strictly positive coefficient for $0<s<1$.

To obtain the target suffix $I_d$, use $d$ distinct tail linear factors
and follow the first branch of (14), successively deleting the indexed copies
$\lambda_1,\ldots,\lambda_d$.  Every deletion coefficient
$s^2/A_\ell$ is strictly positive for $s>0$.  There are infinitely many
tail factors, so all $d\le kh-1$ deletions are available.  After the last
deletion, retain $Q_{I_d}$ along every remaining factor.  The remaining
infinite product is again of the form (25), apart from finitely many positive
factors, and is strictly positive.

This constructs a positive contribution to every ordered suffix for every
$0<s<1$.  Since $w$ is positive on an open subinterval, all
$\gamma_d$ are strictly positive.  This completes the proof of the positive
pole-truncation theorem.

## 5. Even $m$: the cosine extension

Set



$$
h=n+1,\qquad
 \nu=2\left\lfloor\frac n2\right\rfloor+1.                 \tag{26}
$$



Then $\nu$ is odd and $h\in\{\nu,\nu+1\}$.  Let $m=2k$,
$c=k-\tfrac12$, and



$$
a_r=r-\frac12,qquad A_r=a_r^2,qquad
 T(u)=\int_0^u\cos(\pi t)^\nu dt,qquad
 \tau=\int_0^{1/2}\cos(\pi t)^\nu dt>0.                   \tag{27}
$$



Because $\nu$ is odd,



$$
T(a_r)=(-1)^{r-1}\tau.                    \tag{28}
$$



Moreover, $T'=\cos^\nu(\pi u)$ has a zero of order $\nu$ at every
half-integer.  Thus $T/\tau$ has exactly the alternating value jets and
zero derivative jets through order $n$ required by the centered cardinal
polynomial, up to one global sign.

Put



$$
\mathcal C(x)=\cos(\pi\sqrt{-x}).                          \tag{29}
$$



With $u=\sqrt{-x}$, the entire quotient determined by the jets is



$$
F_C(x)=\frac{T(u)}u
       =\int_0^1\cos(\pi su)^\nu ds
       =\int_0^1\mathcal C(s^2x)^\nu ds.                   \tag{30}
$$



This is (8) with weight $w(s)=1$ and rates
$A_r=(r-\tfrac12)^2$.

Let the *raw* centered cardinal transform be



$$
\Lambda_0(c+u)=uN_{2k,n}^{(0)}(-u^2).                     \tag{31}
$$



The node $c+a_r=k+r-1$ has sign
$(-1)^{k+r-1}=(-1)^k(-1)^{r-1}$.  Hence, with
$\sigma_k=(-1)^k$, uniqueness of Hermite interpolation gives the exact
positive-scalar relation



$$
\boxed{
 N_{2k,n}^{(0)}(x)
   =\frac{\sigma_k}{\tau}\,\mathscr R_{k,h}F_C(x).}         \tag{32}
$$



Dividing by $u$ and changing from the local coordinate $u-a_r$ to
$x+A_r$ preserves all multiplicities because $a_r\ne0$.  This justifies
the remainder identification in (32), including all confluent jets.

The theorem proves that the raw Newton coefficients in (31) all have sign
$\sigma_k$.  After the harmless global sign normalization used in the
preceding audit, every one is strictly positive.

## 6. Odd $m$: the sinc extension for $\Lambda_0$

Let $m=2k+1$, $c=k$, and retain (26).  Define



$$
V(u)=\int_0^u\sin(\pi t)^\nu dt,qquad
 \eta=\int_0^1\sin(\pi t)^\nu dt>0,                        \tag{33}
$$



and



$$
E_0(u)=1-\frac2\eta V(u).                                 \tag{34}
$$



Since $\nu$ is odd,



$$
V(u+1)=\eta-V(u),\qquad E_0(u+1)=-E_0(u),qquad
 E_0(r)=(-1)^r.                                             \tag{35}
$$



Also $E_0'$ has a zero of order $\nu$ at every integer, so $E_0$
matches all required $\Lambda_0$ jets through order $n$.  At the central
integer,



$$
E_0(u)-1\text{ vanishes to order }\nu+1
    =h+(h\bmod2).                                           \tag{36}
$$



Put



$$
\mathcal S(x)=\frac{\sin(\pi\sqrt{-x})}{\pi\sqrt{-x}}.   \tag{37}
$$



Then



$$
F_S(x)=\frac{V(u)}{u^{\nu+1}}
       =\pi^\nu\int_0^1s^\nu\mathcal S(s^2x)^\nu ds.      \tag{38}
$$



The irrelevant factor $\pi^\nu>0$ may either be retained or absorbed in
the weight.  Formula (38) is (8), with rates $A_r=r^2$ and positive weight
$s^\nu$.

Let $\sigma_k=(-1)^k$, the value of the centered cardinal at zero, and
define the raw transform by



$$
\Lambda_0(c+u)-\sigma_k
       =u^{\nu+1}N_{2k+1,n}^{(0)}(-u^2).                   \tag{39}
$$



Since the centered cardinal is $\sigma_k$ times the Hermite interpolant of
$E_0$, while $E_0-1=-2V/\eta$, one gets the exact scalar and sign



$$
\boxed{
 N_{2k+1,n}^{(0)}(x)
   =-\frac{2\sigma_k}{\eta}\,\mathscr R_{k,h}F_S(x).}      \tag{40}
$$



Thus the raw coefficients all have sign $-\sigma_k$, and the normalized
coefficients are strictly positive for every $k,n$.

## 7. The parity defect: the sinc extension for $\Lambda_1$

In the defect, $m=2k+1$ and $n$ is odd.  Hence $h=n+1$ is even and



$$
\nu=n=h-1.                        \tag{41}
$$



Use the same $E_0,V,\eta$ as in Section 6 and define



$$
E_1(u)=\int_0^uE_0(t)dt,qquad
 W(u)=\int_0^uV(t)dt.                                      \tag{42}
$$



The symmetry $E_0(1-u)=-E_0(u)$ gives
$\int_0^1E_0=0$.  Together with antiperiodicity, this implies



$$
E_1(r)=0,qquad E_1'(r)=(-1)^r                            \tag{43}
$$



at every integer.  All higher required derivatives vanish.  Furthermore,



$$
E_1(u)-u=-\frac2\eta W(u)                                 \tag{44}
$$



vanishes to order $\nu+2=h+1$ at zero.  A second elementary change of
variables gives



$$
F_1(x)=\frac{W(u)}{u^{\nu+2}}
       =\pi^\nu\int_0^1(1-s)s^\nu
                    \mathcal S(s^2x)^\nu ds.               \tag{45}
$$



This is (8) with the positive weight $(1-s)s^\nu$.

Define the raw defect transform by



$$
\Lambda_1(c+u)-\sigma_ku
       =u^{\nu+2}N_{2k+1,n}^{(1)}(-u^2).                   \tag{46}
$$



The centered $\Lambda_1$ cardinal is $\sigma_k$ times the Hermite
interpolant of $E_1$.  Therefore



$$
\boxed{
 N_{2k+1,n}^{(1)}(x)
   =-\frac{2\sigma_k}{\eta}\,\mathscr R_{k,h}F_1(x).}      \tag{47}
$$



Again the raw sign is $-\sigma_k$, and every normalized ordered Newton
coefficient is strictly positive.

## 8. Normalized products versus the denominators in the preceding audit

The preceding audit used the monic finite products



$$
B_k(x)=\prod_{r=1}^k(x+A_r),                               \tag{48}
$$



whereas the canonical products use



$$
\mathcal P_k(x)=\prod_{r=1}^k\left(1+\frac{x}{A_r}\right)
                =\frac{B_k(x)}{\prod_{r=1}^kA_r}.           \tag{49}
$$



Thus



$$
\frac{R(x)}{\mathcal P_k(x)^h}
   =\left(\prod_{r=1}^kA_r\right)^h\frac{R(x)}{B_k(x)^h}.   \tag{50}
$$



All conversion factors in (32), (40), (47), and (50) are positive except
for the explicitly displayed signs $\sigma_k$ or $-\sigma_k$.  Hence no
normalization ambiguity remains: after the same one-sign normalization used
in the frozen certificate, the actual rational functions (22), (25), and
(34) of the preceding audit have precisely the strictly positive ordered
Newton expansions claimed there.

## 9. Consequence for $\Gamma$, and what remains open

For the generic parity blocks, the preceding audit reduced the augmented
border to a divided-difference determinant for the rational functions built
from $N^{(0)}$.  Equations (12), (32), and (40) make those rational
functions strictly completely monotone.  The Hermite--Genocchi sign and
Andreief's identity therefore make the augmented block nonzero.

In the parity defect, the preceding audit used the stronger coefficient
form of the Newton-to-Toeplitz lemma.  Equation (47) supplies its missing
hypothesis for every $k,n$.  The already proved shifted-coordinate theorem
supplies the other border factor.  This proves (3).

The logical boundary is important:

* $\Gamma\ne0$ does not imply
  $\Delta=W-\Gamma\ne0$; cancellation with the Wronskian remains possible.
* The theorem gives no lower bound for the actual degree of $\Delta$.
* It gives no control of primitive content, primitive height, or
  $|\Delta(i\pi)|$.
* It therefore does not beat an algebraic measure for $e$ and does not
  prove anything new about the arithmetic nature of $e+\pi$.

## 10. Exact finite replay

The certificate works only over $\mathbb Q$.  For each of the three
families on its recorded grid, it

1. constructs $\Lambda_0$ or $\Lambda_1$ by polynomial CRT and verifies
   every cardinal jet;
2. reconstructs the centered factorization (31), (39), or (46) and checks the
   exact raw sign predicted by (32), (40), or (47);
3. reconstructs every actual ordered Newton coefficient and proves it
   positive by exact rational comparison;
4. replaces the infinite product by a finite product through
   $L=2k+1$, evaluates (30), (38), or (45) coefficientwise with exact beta
   moments, and computes its Hermite remainder modulo $\mathcal P_k^h$;
5. verifies the quotient-remainder identity and every ordered Newton
   coefficient of the finite polar part exactly; and
6. exhausts all nonempty reciprocal subproducts for several distinct and
   repeated rate lists, checking the completion lemma (18)--(21).

The exact finite replay is a consistency certificate, not the source of the
all-parameter conclusion.  The proof in Sections 2--7 supplies that
conclusion.
