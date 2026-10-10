> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The balanced centered-cosh quadratic as two bordered Padé determinants

## Exact first moments, a canonical content gcd, and the remaining lower-height gap

Checked: 2026-08-27 UTC

## 1. Scope and statement

Put



$$
F(x)=\frac1{2\cosh\sqrt x}=\sum_{j\geq0}f_jx^j,
 \qquad f_j=\frac{E_{2j}}{2(2j)!},                          \tag{1}
$$



where $E_{2j}$ is the signed secant Euler number.  Let $Q,P$ be a
normal diagonal Padé pair,



$$
\deg Q=\deg P=q,\qquad FQ-P=O(x^{2q+1}),                  \tag{2}
$$



and let $G,R$ be the adjacent pair of type $[q+1/q-1]$.  The exact
cross identity is



$$
RQ-PG=\kappa x^{2q+1},\qquad \kappa\ne0.                  \tag{3}
$$



In the quotient $A=\mathbb Q[x]/(Q)$, define



$$
\omega(U)=[x^{q-1}]\rho_Q(U),\qquad
 \lambda(U)=\omega(G^{-2}U),\qquad h_j=\lambda(x^j).       \tag{4}
$$



The residual-quotient theorem shows that $\lambda$ is the unique
annihilator of the balanced $r=1$ product image for $q\geq2$.  This
note identifies its first two moments exactly.  Set



$$
a_m=[x^m]\frac{P(x)^2}{Q(x)}.                             \tag{5}
$$



If $q_q=\operatorname {lc}(Q)$, then



$$
\boxed{
 h_j=-\frac{q_q}{\kappa^2}\,a_{4q+1-j}
 \quad(j=0,1).}                                            \tag{6}
$$



Consequently, whenever $(h_0,h_1)\ne(0,0)$, the primitive
degree-at-most-one kernel direction is



$$
\boxed{
 C_q^{\rm prim}(x)=
 \operatorname {prim}\bigl(a_{4q}-a_{4q+1}x\bigr).}        \tag{7}
$$



Here $\operatorname {prim}$ means common denominator clearing followed
by division by the coefficient gcd and an irrelevant global sign.
Equation (7) explains the exact finite anchors, for example



$$
C_2^{\rm prim}(x)
 =6337786868+2568511585x.                                  \tag{8}
$$



The second theorem is an integral bordered-determinant description of
(7).  Define the rational $q\times(q+1)$ Padé row matrix



$$
T_q=(f_{q+r-k})_{\substack{1\leq r\leq q\\0\leq k\leq q}},
                                                                    \tag{9}
$$



and, for $m\in\{4q,4q+1\}$, define



$$
\ell_{m,k}
 =2\sum_{i=k}^{q}f_{m-i}f_{i-k}
   -\sum_{v=0}^{m-k}f_vf_{m-k-v}
 \qquad(0\leq k\leq q).                                   \tag{10}
$$



Choose the row clearings



$$
L_r=2(2(q+r))!,\qquad
 \Lambda_q=4(8q+2)!,                                      \tag{11}
$$



and put



$$
T_q^\#=(L_rf_{q+r-k})_{r,k}\in\mathbb Z^{q\times(q+1)},
 \qquad b_m=(\Lambda_q\ell_{m,k})_{k=0}^q\in\mathbb Z^{q+1}.
                                                                    \tag{12}
$$



Let



$$
\delta_q=\gcd_{0\leq k\leq q}
 \det(T_q^\#\hbox{ with column }k\hbox{ deleted}),          \tag{13}
$$



and define the primitive integral kernel vector



$$
c_k=\frac{(-1)^k}{\delta_q}
 \det(T_q^\#\hbox{ with column }k\hbox{ deleted}).          \tag{14}
$$



Finally put



$$
u_m=b_m c=\sum_{k=0}^q b_{m,k}c_k,\qquad
 K_q=\gcd(u_{4q},u_{4q+1}).                                \tag{15}
$$



Then



$$
\boxed{
 C_q^{\rm prim}(x)=
 \frac{u_{4q}-u_{4q+1}x}{K_q}}
                                                                    \tag{16}
$$



up to sign, whenever the pair is nonzero.  Equivalently,



$$
u_m=\frac{(-1)^q}{\delta_q}
 \det\begin{pmatrix}T_q^\#\\ b_m\end{pmatrix}.             \tag{17}
$$



Thus $K_q$ is the exact and only endpoint content left after saturating
the Padé kernel.  It is not replaced by an unproved generic Smith
cancellation.

The canonical clearing also gives the all-parameter height bound



$$
\boxed{
 \log H(C_q^{\rm prim})
 \leq(3+o(1))q^2\log q.}                                   \tag{18}
$$



This improves the generic $O(q^3\log q)$ cofactor bound for the
quadratic endpoint.  It is an upper bound, not a matching lower bound.

## 2. Residue proof of the first-moment identity

Assume first that $Q$ has distinct roots
$\alpha_1,\ldots,\alpha_q$.  Lagrange interpolation gives, for any
$U\in A$,



$$
\omega(U)=q_q\sum_{i=1}^q\frac{U(\alpha_i)}{Q'(\alpha_i)}.
                                                                    \tag{19}
$$



At a root of $Q$, (3) gives



$$
-P(\alpha_i)G(\alpha_i)
   =\kappa\alpha_i^{2q+1}.                                 \tag{20}
$$



Therefore



$$
h_j=\frac{q_q}{\kappa^2}
 \sum_{i=1}^q
 \frac{P(\alpha_i)^2\alpha_i^{j-4q-2}}{Q'(\alpha_i)}.       \tag{21}
$$



On the other hand, for $m>q$, the global residue theorem applied to
$P(x)^2/(Q(x)x^{m+1})$ gives



$$
[x^m]\frac{P(x)^2}{Q(x)}
 =-\sum_{i=1}^q
 \frac{P(\alpha_i)^2}{Q'(\alpha_i)\alpha_i^{m+1}}.          \tag{22}
$$



Take $m=4q+1-j$ in (22).  Equations (21)--(22) prove (6).
The statement for a nonsquarefree $Q$ follows either from confluent
residues or by polynomial continuity on the open set
$\operatorname {Res}(Q,G)\ne0$.  No simplicity assertion about the
Padé roots is required.

Since a coefficient functional with first moments $h_0,h_1$ kills
$h_1-h_0x$, (6) proves (7).

## 3. The bordered Toeplitz formula

Let



$$
H=FQ-P.
$$



By (2), $H=O(x^{2q+1})$, and the exact identity



$$
\frac{P^2}{Q}-(2FP-F^2Q)=\frac{H^2}{Q}=O(x^{4q+2})        \tag{23}
$$



shows that, for $m\leq4q+1$,



$$
a_m=[x^m](2FP-F^2Q).                                     \tag{24}
$$



Write $Q=\sum_{k=0}^qq_kx^k$.  Since



$$
[x^i]P=\sum_{k=0}^{i}q_kf_{i-k}\qquad(0\leq i\leq q),
$$



expanding (24) gives



$$
a_m=\sum_{k=0}^q\ell_{m,k}q_k,                            \tag{25}
$$



with $\ell_{m,k}$ exactly as in (10).

The high Padé equations say $T_qq=0$.  The matrix $T_q$ has rank $q$.
Indeed, its minor in columns $k=1,\ldots,q$ is, up to checkerboard
sign, $2^{-q}s_{(q^q)}(t_0,t_1,\ldots)>0$, where the complete
homogeneous specialization comes from



$$
\cosh\sqrt x=\prod_{\nu\geq0}
 \left(1+\frac{4x}{\pi^2(2\nu+1)^2}\right).                \tag{26}
$$



Thus its cofactor vector is a nonzero kernel vector.  Expanding the
bordered determinant along its last row and using (25) proves the
rational version of (17).

## 4. Integral saturation and the sole content

The clearings in (11)--(12) are integral.  Indeed,



$$
L_rf_j
 =E_{2j}\frac{(2(q+r))!}{(2j)!}\in\mathbb Z
 \qquad(j\leq q+r).                                       \tag{27}
$$



For the border, every product in (10) has indices whose sum is at most
$4q+1$.  Hence



$$
\Lambda_q f_af_b
 =E_{2a}E_{2b}
   \frac{(8q+2)!}{(2a)!(2b)!}\in\mathbb Z.                 \tag{28}
$$



The last factorial ratio is integral: choose disjoint sets of sizes
$2a$ and $2b$ from a set of size $8q+2$, then multiply by the factorial
of the unused size.

For an integer matrix of rank $q$ with $q+1$ columns, the signed maximal
minors divided by their gcd form the primitive integral generator of
its one-dimensional rational kernel.  This proves (13)--(14).  Row
scaling does not change the rational kernel, so $c$ is the primitive
integral diagonal Padé denominator.  Equations (25) and (12) now give
(15)--(17).  Dividing the two endpoint coefficients by their gcd proves
(16).  There is no further endpoint content hidden in this
normalization.

Assume in the rest of this paragraph that
$(u_{4q},u_{4q+1})\ne(0,0)$, so that $K_q>0$.  The exact local
criterion is then immediate.  For every prime $p$,



$$
p\mid K_q
 \quad\Longleftrightarrow\quad
 b_{4q}c\equiv b_{4q+1}c\equiv0\pmod p.                   \tag{29}
$$



If $T_q^\#$ has rank $q$ modulo $p$, its right kernel is spanned by
$c\bmod p$, and (29) is equivalent to



$$
b_{4q},b_{4q+1}
 \in\operatorname {rowspan}_{\mathbb F_p}(T_q^\#).         \tag{30}
$$



Thus a prime content gain is a simultaneous two-border rank event.
Equation (30) is a precise local theorem, but it does not estimate how
often or to what prime-power depth that event occurs.

## 5. Height bound

The beta formula for Euler numbers gives



$$
|E_{2j}|\leq(2j)!\qquad(j\geq0),\qquad |f_j|\leq\frac12.  \tag{31}
$$



For $j\geq1$, this follows from
$4^{j+1}\beta(2j+1)/\pi^{2j+1}<1$; the case $j=0$ is
equality.

The convolution in (10) can be written more sharply.  Put
$N=m-k$ and $d=q-k$.  Since $d<N/2$,



$$
\ell_{m,k}
 =-\sum_{v=d+1}^{N-d-1}f_vf_{N-v}.                        \tag{32}
$$



For $m\in\{4q,4q+1\}$ the sum has at most $3q$ terms, so



$$
|\ell_{m,k}|\leq\frac{3q}{4}.                             \tag{33}
$$



The Euclidean norm of row $r$ of $T_q^\#$ is at most
$\sqrt{q+1}L_r/2$, and the norm of $b_m$ is at most
$3q\sqrt{q+1}\Lambda_q/4$.  Hadamard's inequality and
$\delta_q,K_q\geq1$ give



$$
H(C_q^{\rm prim})
 \leq
 \frac{3q}{2^{q+2}}(q+1)^{(q+1)/2}
 \Lambda_q\prod_{r=1}^qL_r.                               \tag{34}
$$



Stirling's formula yields



$$
\sum_{r=1}^q\log(2(q+r))!
   =(3+o(1))q^2\log q,                                    \tag{35}
$$



while $\log\Lambda_q=O(q\log q)$.  Equations (34)--(35)
prove (18).

## 6. Comparison with the consecutive-Euler gcd

The closer-root fixed-quadratic family has the separate content



$$
G_N=\gcd\bigl((2N+2)(2N+1)|E_{2N}|,\ |E_{2N+2}|\bigr).    \tag{36}
$$



Its local condition concerns two individual consecutive Euler values.
The balanced content $K_q$ instead concerns the two bordered
determinants (17), whose border entries contain the full middle
convolutions (32) and whose kernel contains every Padé row (9).
Therefore the Kummer periodicity theorem for (36) does not, by itself,
bound $K_q$.  Any transfer would need a new identity between the
border rank event (30) and the two Euler values in (36).

There is already a rigorous warning against transferring the dyadic
shape of the closer-root polynomial.  Exact rational calculation at
$q=11$ gives both coefficients of $C_{11}^{\rm prim}$ odd, whereas
the closer-root primitive quadratic always has an even constant
coefficient and an odd quadratic coefficient.  This single exact
counterexample disproves a universal parity-shape identification; it
does not constitute an asymptotic statement about odd primes.

## 7. Analytic and measure ledger

For the balanced parameters



$$
n=3q+1,\qquad t=q,\qquad D=n-1,                            \tag{37}
$$



the centered Schwarz exponent from the global construction is



$$
G_{n,t}
 =(2q+4)\log\frac{2q+4}{e\pi}
  -6q\log\frac\pi2
 =2q\log q+O(q).                                           \tag{38}
$$



This is measured against the normalized global analytic height, not
against the endpoint height alone.  If $s=e+\pi$ were rational, the
degree-two polynomial measure for $e$ would additionally cost about
$2\log H(C_q^{\rm prim})$.  A sufficient comparison has the schematic
form



$$
G_{n,t}>
 \log H_{\rm an}+2\log H(C_q^{\rm prim})+O(q).             \tag{39}
$$



The upper bound (18) supplies a structured construction at
$q^2\log q$ scale, but it does not prove that the actual primitive
height is that large.  Therefore (18) cannot be used as an impossibility
theorem.  Conversely, because its scale is much larger than (38), it
does not by itself give a positive measure margin either.  A successful
positive ledger would need either:

* a much smaller primitive representative and matching global lift; or
* content $K_q$ and global content large enough to remove the apparent
  quadratic-in-$q$ determinant scale.

The exact finite primitive heights through $q=16$ grow roughly on a
$q^2$ scale, while the observed approximation error of the quadratic
root eventually has nearly constant increment $8\log3$ per $q$.
These are diagnostics only.  No $4q\log q$ root-error law or
$q^2\log q$ height lower bound is asserted.

The current sharp conclusions are therefore:

1. (6), (16), and (17) give exact all-parameter formulas.
2. $K_q$ is the precise endpoint content still requiring a local-prime
   theorem.
3. (18) removes the generic cubic cofactor majorant.
4. No proved lower bound excludes a large cancellation in $K_q$, and
   no proved upper bound for the normalized global lift closes the
   measure comparison.

## 8. Deterministic replay and logical boundary

The companion files are:

* scripts/centered_cosh_balanced_quadratic_border_content_certificate.py
* results/centered_cosh_balanced_quadratic_border_content_certificate.json
* results/centered_cosh_balanced_quadratic_border_content_hashes.sha256

The replay checks exact Padé pairs, the residue identity (6), the
border formulas (10), (16), and (17), primitive cofactor saturation,
integral row clearing, the local criterion for a finite set of primes,
and the $q=11$ dyadic counterexample.  The finite nonvanishing checks
are not extrapolated.  In particular, this note does not prove
$(h_0,h_1)\ne(0,0)$ for every $q$.

Nothing here proves that $e+\pi$ is algebraic or transcendental.
