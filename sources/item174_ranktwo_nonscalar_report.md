> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 174 — rank-two determinant zeros, fixed-residue quasipolynomials, and scalar-free lift freedom

Date: 2026-08-29

## 1. Scope and verdict

Work on the prime-number-theorem scale



$$
p\le 4m+1<p^2
$$



and in the genuine rank-two cell $\kappa=0$.  Write



$$
6m=3jp+3s,\qquad 4m+1=2jp+2s+1,
 \qquad 2m=jp+s,                                      \tag{1.1}
$$



where



$$
j\ge1,\qquad 0\le s\le {p-1\over3},\qquad s\equiv j\pmod2. \tag{1.2}
$$



The conclusions are deliberately scoped.

**PROVED — exact entry determinant.**  The two first Cartier images are
dependent if and only if the coefficient determinant $\Delta_{p,s}$ in
(2.4) vanishes.  In the $\kappa=0$ cell this is the necessary and
sufficient entry condition for the *rank-two Cartier mechanism* to force the
first post-normalization copy of $p$.  It is not a converse classification
of accidental factors of the actual content.  A rank-two degree ceiling by
itself forces nothing.

**PROVED — exact scalar-free carry gate.**  Once $\Delta_{p,s}=0$, the
rank-two row has no old rank-zero factor removed, and the two endpoint minors
are divisible by exactly one *forced* power of $p$.  If their normalized
digits are $A_i,B_i$, then



$$
p^2\mid c_m\iff A_0=0,
 \qquad
 p^3\mid c_m\iff A_0=A_1=B_0=0.                         \tag{1.3}
$$



All digits are obtained by the convolution-and-carry law (3.6).  No Cartier
coefficient is divided by, so zero rows and proportional nonzero rows are
handled uniformly.

**PROVED AMBIENT NO-GO — the entry determinant does not determine a lift.**
In the ambient category of integral endpoint triples satisfying precisely the
mod-$p$ proportionality output of the first Cartier theorem, the three
digits $(A_0,A_1,B_0)$ are independently arbitrary.  This is a formal
non-determination theorem, not a claim that every such lift occurs in the
actual mixed-cubic family.  A cubic theorem must use new Hasse-coordinate or
differential information.

**PROVED — fixed-$s$ quasipolynomial reduction.**  For fixed $s$, fixed
$\rho\in\{1,3\}$, and primes



$$
p\equiv\rho\pmod4,\qquad p\ge8s+3, \tag{1.4}
$$



there is an explicit rational constant $C_{s,\rho}$ such that



$$
\boxed{\Delta_{p,s}\equiv C_{s,\rho}\pmod p.} \tag{1.5}
$$



The denominator in (1.5) is a $p$-adic unit.  Therefore, whenever
$C_{s,\rho}\ne0$, the large-prime determinant zeros for this fixed
$(s,\rho)$ are exactly the finite prime divisors of its numerator.

**PROVED COMPUTATION — a bounded fixed-$s$ theorem.**  Exact reduction in
the auxiliary prime characteristic $2^{61}-1$ proves



$$
C_{s,1}C_{s,3}\ne0\qquad(0\le s\le256). \tag{1.6}
$$



The rational values themselves were also computed for $0\le s\le64$;
their denominators are powers of two and $C_{s,3}=-C_{s,1}$ throughout
that certified range.  This finite-range theorem is exact, but it is not
extrapolated to all $s$.

**PROVED — thinness of bounded and slowly growing residual support.**  Since
(1.1) gives $p\mid2m-s$, determinant-zero primes supported on
$0\le s\le S(m)$ have total logarithmic weight at most



$$
(S(m)+1)\log(2m)+O(S(m)).                 \tag{1.7}
$$



It is $o(m)$ whenever $S(m)=o(m/\log m)$.  Every finite collection of
affine rays $p=\alpha s+\beta$ is also zero-rate, even with any fixed
number of additional lifted copies.

**EXPERIMENTAL FINITE.**  The archived $m\le500$ probe contains 18,147
$e=1$, $\kappa=0$ rows, of which 295 vanish; these are 127 distinct
$(p,s)$ pairs.  Ninety-four pairs lie on the three already proved rays and
33 are sporadic in this finite window.  In the archived $m\le100$ lifted
census, 46 determinant-zero rank-two rows supply the first copy, eight
supply a second, and none supplies a third.

**OPEN.**  No positive-mass determinant-zero family, no positive-mass
simultaneous solution of (1.3), and no new asymptotic content exponent is
proved.  Nothing in this item decides the rationality of $e+\pi$.

## 2. Exact determinant in the $\kappa=0$ cell

Put



$$
u=x(1-x),\qquad Q=(1+x)(1+x^2),
$$



and define



$$
P=x^{3s}(1-x)^{3s}Q^{p-2s-2}=\sum_nc_nx^n.             \tag{2.1}
$$



The two Cartier polynomials are $P$ and $QP$.  Set



$$
\begin{aligned}
 \alpha_1&=c_{p-1},&\beta_1&=c_{2p-1},\\
 \alpha_0&=\sum_{r=0}^3c_{p-1-r},&
 \beta_0&=\sum_{r=0}^3c_{2p-1-r}.
\end{aligned}                                             \tag{2.2}
$$



Then the two first Cartier images are



$$
F(\alpha_i+\beta_ix)\,dx\qquad(i=0,1),
 \qquad F={u^{3j}\over Q^{2j+1}},                         \tag{2.3}
$$



and hence are dependent exactly when



$$
\boxed{
 \Delta_{p,s}=\alpha_0\beta_1-\beta_0\alpha_1
 =(c_{p-2}+c_{p-3}+c_{p-4})c_{2p-1}
 -(c_{2p-2}+c_{2p-3}+c_{2p-4})c_{p-1}=0
 \quad\hbox{in }\mathbf F_p.}                            \tag{2.4}
$$



For later use introduce



$$
W_s={x^{3s}(1-x)^{5s+2}\over(1-x^4)^{2s+2}}
     =\sum_nw_nx^n,
 \qquad
 Z_s={x^{3s}(1-x)^{5s+1}\over(1-x^4)^{2s+1}}
     =\sum_nz_nx^n.                                      \tag{2.5}
$$



The cancellation already proved in Item 151 gives the equivalent compact
form



$$
\boxed{\Delta_{p,s}=z_{p-1}w_{2p-1}-z_{2p-1}w_{p-1}.} \tag{2.6}
$$



This separates the determinant condition from all later endpoint lifts.
In particular, a row satisfying only the rank-two degree bound has not yet
forced any divisor.

## 3. Exact scalar-free endpoint digits and carries

Let



$$
X_i=pR_i,
 \qquad
 \mathscr A=L_1X_0-L_0X_1,
 \qquad
 \mathscr B=L_1E_0-L_0E_1.                              \tag{3.1}
$$



On a determinant-zero rank-two row, relative Cartier proportionality gives



$$
p\mid\mathscr A,\mathscr B.      \tag{3.2}
$$



Here $p\notin\mathcal P_m$: the $\kappa=0$ first-Cartier degrees are
$3p-3$ and $3p-6$, not both at most $p-2$.  Thus no copy of $p$
was removed by the old squarefree factor $G_m$.  Also
$v_p(D_m^\sharp)=1$.  The primitive normalization therefore gives



$$
v_p(U_m)=1+v_p(\mathscr A/p),
 \qquad
 v_p(V_m)=2+v_p(\mathscr B/p).                            \tag{3.3}
$$



Write



$$
{\mathscr A\over p}=A_0+A_1p+A_2p^2+\cdots,
 \qquad
 {\mathscr B\over p}=B_0+B_1p+B_2p^2+\cdots,            \tag{3.4}
$$



with digits in $\{0,\ldots,p-1\}$.  Formula (3.3) proves (1.3) and, at
all depths,



$$
p^r\mid c_m
 \iff A_0=\cdots=A_{r-2}=0
 \quad\hbox{and}\quad B_0=\cdots=B_{r-3}=0.             \tag{3.5}
$$



The second string is empty at $r=2$.

For completeness, write any determinant $AB-CD$ in coordinate digits
$A=\sum A_np^n$, and similarly for $B,C,D$.  Put



$$
S_n=\sum_{r=0}^n(A_rB_{n-r}-C_rD_{n-r}),\qquad q_{-1}=0,
$$





$$
\tau_n\equiv S_n+q_{n-1}\pmod p,
 \quad0\le\tau_n<p,
 \qquad
 q_n={S_n+q_{n-1}-\tau_n\over p}.                        \tag{3.6}
$$



Then $AB-CD=\sum_n\tau_np^n$.  Apply (3.6) to



$$
(A,B,C,D)=(L_1,X_0,L_0,X_1)
 \quad\hbox{and}\quad(L_1,E_0,L_0,E_1).                 \tag{3.7}
$$



The forced digit is $\tau_0=0$; consequently
$A_r=\tau^{\mathscr A}_{r+1}$ and
$B_r=\tau^{\mathscr B}_{r+1}$.  The quotient in (3.6) is exact by the
definition of $\tau_n$.  This is the promised scalar-free digit/carry
law.

## 4. Ambient lift-freedom theorem

The first Cartier theorem supplies mod-$p$ proportionality, but no formal
rule for the next endpoint digits.  The failure is already surjective.
Fix arbitrary



$$
a_0,a_1,b_0\in\mathbf F_p
$$



and choose integral representatives.  In the ambient endpoint-coordinate
space set



$$
T_0=(X_0,L_0,E_0)=(0,1,0),
 \qquad
 T_1=(-p(a_0+pa_1),1,-pb_0).                             \tag{4.1}
$$



The reductions of $T_0,T_1$ are identical, so they satisfy the strongest
possible nonzero proportionality conclusion modulo $p$.  Nevertheless,



$$
{L_1X_0-L_0X_1\over p}=a_0+pa_1,
 \qquad
 {L_1E_0-L_0E_1\over p}=b_0.                            \tag{4.2}
$$



Thus all $p^3$-gate patterns occur while the first-order data are fixed.
Adding arbitrary higher multiples of $p$ in (4.1) realizes the full digit
tower.  The certificate exhausts all $5^3$ triples at $p=5$.

Equation (4.2) is intentionally only an ambient no-go.  Actual endpoint
triples are coupled by the mixed-cubic Hasse recurrence, so a special
identity could still force some digits there.  What (4.2) rules out is a
proof obtained by formally iterating $\Delta_{p,s}=0$ or mod-$p$
proportionality without new arithmetic input.

## 5. Fixed-$s$ quasipolynomials

Fix $s\ge0$, $\rho\in\{1,3\}$, and $a\in\{1,2\}$.  For an
indeterminate $P$, define



$$
\begin{aligned}
 \mathcal W_{a,s,\rho}(P)
 &=\sum_{\substack{0\le k\le5s+2\\
          k\equiv a\rho-1-3s\ (4)}}
 (-1)^k{5s+2\choose k}
 {2s+1+(aP-1-3s-k)/4\choose2s+1},\\
 \mathcal Z_{a,s,\rho}(P)
 &=\sum_{\substack{0\le k\le5s+1\\
          k\equiv a\rho-1-3s\ (4)}}
 (-1)^k{5s+1\choose k}
 {2s+(aP-1-3s-k)/4\choose2s}.
\end{aligned}                                             \tag{5.1}
$$



Generalized binomial coefficients make these rational polynomials in
$P$.  If $p\equiv\rho\pmod4$, the congruence on $k$ makes every
displayed lower-series index integral.  The sufficient bound
$p\ge8s+3$ makes all of them nonnegative, including the worst
$w_{p-1}$ term.  Direct expansion of (2.5) therefore gives the exact
integer equalities



$$
w_{ap-1}=\mathcal W_{a,s,\rho}(p),
 \qquad z_{ap-1}=\mathcal Z_{a,s,\rho}(p).               \tag{5.2}
$$



Set



$$
\mathcal D_{s,\rho}(P)=
 \mathcal Z_{1,s,\rho}(P)\mathcal W_{2,s,\rho}(P)
 -\mathcal Z_{2,s,\rho}(P)\mathcal W_{1,s,\rho}(P),
 \qquad C_{s,\rho}=\mathcal D_{s,\rho}(0).              \tag{5.3}
$$



Equations (2.6) and (5.2) give



$$
\Delta_{p,s}=\mathcal D_{s,\rho}(p). \tag{5.4}
$$



The denominators in (5.1) divide products of powers of four and factorials
of order at most $2s+1$.  Under (1.4), $p$ divides none of them.  Reducing
(5.4) modulo $p$ proves (1.5), and hence



$$
\boxed{
 \Delta_{p,s}=0\text{ in }\mathbf F_p
 \iff p\mid\operatorname{num}(C_{s,\rho})
 }
 \quad(C_{s,\rho}\ne0).                                \tag{5.5}
$$



This is a complete large-prime classification for each fixed $s$, not a
heuristic codimension statement.

### 5.1 Certified nonzero range and examples

The certificate first computes the rational numbers exactly for
$0\le s\le64$.  It then evaluates the same generalized-binomial formulas
in



$$
\mathbf F_q,\qquad q=2^{61}-1,   \tag{5.6}
$$



where $q$ is prime and every relevant denominator through $s=256$ is a
unit.  Every one of the 514 values $C_{s,\rho}\bmod q$ is nonzero.  A
nonzero reduction proves the underlying rational number is nonzero, yielding
(1.6).  The exact and auxiliary evaluations agree on their common range.

The first constants are



$$
\begin{array}{c|cc}
s&C_{s,1}&C_{s,3}\\ \hline
0&-1/4&1/4\\
1&-21/64&21/64\\
2&-1815/512&1815/512\\
3&-59787/1024&59787/1024.
\end{array}                                               \tag{5.7}
$$



Since $73\mid59787$ and $73\equiv1\pmod4$, (5.5) explains the
apparently sporadic zero $(p,s)=(73,3)$.  The same classification explains,
among others, $(347,6)$, $(79,9)$, $(509,9)$, and $(233,14)$.
It also produces isolated zeros well beyond the old scan, for example
$(112291,4)$.  Such isolated prime divisors are genuine determinant zeros,
but they are the opposite of a positive-mass structural family.

## 6. Thin-support theorems

### 6.1 Bounded or slowly growing $s$

For any candidate in the $\kappa=0$ cell, (1.1) gives



$$
p\mid2m-s.                  \tag{6.1}
$$



Let $\mathcal S_m$ be any set of distinct primes whose residual indices
lie in $0\le s\le S(m)$.  Then



$$
\prod_{p\in\mathcal S_m}p
 \mid\prod_{s=0}^{S(m)}|2m-s|,                           \tag{6.2}
$$



after omitting any zero factor, which cannot occur in the present range.
Consequently



$$
\sum_{p\in\mathcal S_m}\log p
 \le(S(m)+1)\log(2m)+O(S(m)).                            \tag{6.3}
$$



Thus every fixed finite $s$-union is $O(\log m)$, and every strip
$S(m)=o(m/\log m)$ has weight $o(m)$.  This thinness conclusion does not
need determinant nonvanishing: it applies even if every candidate in the
strip vanished and passed a fixed number of deeper gates.

### 6.2 Every fixed affine ray

Suppose



$$
p=\alpha s+\beta            \tag{6.4}
$$



for fixed integers $\alpha\ge1,\beta$.  Substitution of $s=2m-jp$ gives



$$
2\alpha m+\beta=(\alpha j+1)p.     \tag{6.5}
$$



Hence every prime on this ray divides the fixed linear integer
$2\alpha m+\beta$.  A finite collection of affine rays has radical
logarithm $O(\log m)$.  Multiplying each supported prime by any fixed
number of additional certified copies changes only the constant.  The three
known determinant rays are special cases of (6.5).

The fixed-$s$ theorem and the affine-ray theorem do not cover a genuinely
two-dimensional moving zero set with $s\asymp p$.  Such a set is exactly
what a positive-mass result would have to control.

## 7. Finite diagnostics

The archived $m\le500$ determinant probe gives



$$
\begin{array}{l|r}
e=1,\ \kappa=0\text{ rows}&18{,}147\\
\Delta_{p,s}=0\text{ rows, counting repeated }j&295\\
\text{distinct zero }(p,s)\text{ pairs}&127\\
p=3s+4\text{ pairs}&64\\
p=5s+2\text{ pairs}&18\\
p=5s+1\text{ pairs}&12\\
\text{other pairs}&33.
\end{array}                                               \tag{7.1}
$$



Thirteen of the sporadic pairs lie in the certified range
$s\le256,\ p\ge8s+3$; each is exactly a prime-numerator zero predicted by
(5.5).  Finite frequencies in (7.1) have no asserted limiting density.

The archived $m\le100$ scalar-free replay gives



$$
\begin{array}{c|rrrrr}
\text{required content layer}&p^1&p^2&p^3&p^4&p^5\\ \hline
\text{surviving rank-two-zero rows}&46&8&0&0&0.
\end{array}                                               \tag{7.2}
$$



The eight second-layer rows are



$$
(m,p)=(11,7),(12,11),(23,11),(34,13),
 (65,31),(69,19),(88,19),(96,31).                         \tag{7.3}
$$



In every case $A_0=0$, as required.  None has both $A_1=0$ and
$B_0=0$, so none passes the cubic gate.  This is an exact finite replay,
not a uniform nonvanishing theorem.

## 8. Deterministic replay and final status

The standard-library checker

`work/item174_ranktwo_nonscalar_certificate.py`

performs the following exact checks:

1. rational fixed-$s$ constants through $s=64$;
2. nonzero auxiliary-characteristic witnesses through $s=256$;
3. 1,806 direct coefficient-versus-quasipolynomial comparisons;
4. every available $m\le500$ cell identity and fixed-$s$ comparison;
5. all archived rank-two lifted gates through $p^5$;
6. exhaustive ambient lift freedom at $p=5$; and
7. 2,000 deterministic random carry comparisons with direct determinants.

All checks pass.  The final classification is:

### PROVED

- The exact rank-two determinant and the scalar-free all-depth gate.
- Ambient non-determination of every higher digit from first-order
  proportionality alone.
- The fixed-$s$ quasipolynomial theorem (5.5).
- Nonvanishing of its constants for $0\le s\le256$.
- Zero-rate bounds for slowly growing residual support and fixed affine rays.

### EXPERIMENTAL FINITE

- The 127-pair determinant-zero census through $m=500$.
- Eight second-layer and zero cubic survivors through $m=100$.

### OPEN

- Any positive-mass determinant-zero theorem with $s$ moving on linear
  scale.
- Any positive-mass solution of $A_0=A_1=B_0=0$.
- Enough fourth/fifth-layer or sequential mass to close Route 1.
- Any conclusion about the rationality, irrationality, or transcendence of
  $e+\pi$.
