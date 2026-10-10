> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The next Cartier rank: exact determinant, thin zero rays, and a radical-mass ceiling

Date: 2026-08-28

## 1. Statement and normalization

Put



$$
N=6m,\qquad K_0=4m+1,\qquad K_1=4m+2,
$$





$$
u=x(1-x),\qquad Q=(1+x)(1+x^2)=1+x+x^2+x^3,
 \qquad \omega_i={u^N\over Q^{K_i}}\,dx.
$$



Write



$$
H_i=R_i+{L_i\over4}\log 2+{E_i\over8}\pi,
$$





$$
A_m=L_1R_0-L_0R_1,\qquad
 B_m={L_1E_0-L_0E_1\over8}.
$$



For completeness, the primitive item-133 normalization is



$$
M_j=\operatorname {lcm}(1,\ldots,j),\quad
 M=M_{4m+1},\quad
 T=\prod_{2m<p<3m}p,\quad K=M/T,
$$





$$
D_m^\sharp=2^{9m+5}K,\qquad
 X_m=D_m^\sharp A_m,\qquad Y_m=D_m^\sharp B_m.
$$



Let



$$
d_q(n,k)=
 \begin{cases}
  2r,&k\equiv0\pmod q,\\
  2r+3(q-t),&k\equiv t\pmod q,\quad1\le t<q,
 \end{cases}
 \quad r\equiv n\pmod q,\quad0\le r<q,
$$



and let the already removed squarefree rank-zero product be



$$
G_m=\prod_{p\in\mathcal P_m}p,
$$





$$
\mathcal P_m=\{p\text{ odd prime}:
 d_p(N,K_0)\le p-2,\ d_p(N,K_1)\le p-2\}.
$$



Finally set



$$
U_m=X_m/G_m,\qquad V_m=Y_m/G_m,
 \qquad c_m=\gcd(U_m,V_m).
$$



For an odd prime $p\le4m+1$, define



$$
e_p=\max\{e:p^e\le4m+1\},\qquad q_p=p^{e_p}.
$$



The previous rank-one theorem proves



$$
\prod_{p\in\mathcal H_m}p\mid c_m,
$$



where



$$
\mathcal H_m=\{p<2m:p\text{ odd prime},\ 
 d_{q_p}(N,K_0),d_{q_p}(N,K_1)\le2q_p-2\}.
$$



Its prime-number-theorem mass is



$$
\log\prod_{p\in\mathcal H_m}p
 =C_1m+o(m),\qquad
 C_1=-4\log2+6\log3-3
 =0.8190850097688771\ldots .                         \tag{1.1}
$$



This note determines exactly what happens at the next degree cutoff.
It produces an exact additional squarefree divisor, but no additional
positive asymptotic constant is presently forced.

## 2. Exact classification at degree at most $3q-2$

Fix an odd prime $p$, put $q=p^e$, and write



$$
N=aq+r,\qquad K_0=bq+t,\qquad 0\le r,t<q,
 \qquad \delta=2a-3b.                                  \tag{2.1}
$$



The identity $2N=3K_0-3$ gives



$$
\delta q+2r-3t=-3.                                    \tag{2.2}
$$



If $t>0$, direct substitution in the definition of $d_q$ gives



$$
d_q(N,K_0)=(3-\delta)q-3,
 \qquad d_q(N,K_1)=(3-\delta)q-6.                       \tag{2.3}
$$



If $t=0$, equation (2.2) forces



$$
\delta=-1,\qquad r=(q-3)/2,
$$



and



$$
d_q(N,K_0)=q-3,\qquad d_q(N,K_1)=4q-6.                 \tag{2.4}
$$



Consequently, for $q\ge5$,



$$
d_q(N,K_0),d_q(N,K_1)\le3q-2
 \quad\Longleftrightarrow\quad t>0\text{ and }\delta\ge0.       \tag{2.5}
$$



The cases $\delta\ge1$ are precisely the already controlled
rank-one cases: after $e$ Cartier iterates, both differentials lie in
one common constant-coefficient line.  The genuinely new case is
$\delta=0$.  Equation (2.2) then forces a unique integer $s$ with



$$
r=3s,\qquad t=2s+1,\qquad 0\le s\le{q-1\over3}.         \tag{2.6}
$$



There is no rollover from $K_0$ to $K_1$.  In characteristic $p$,
put



$$
F={u^a\over Q^{b+1}},\qquad
 P=x^{3s}(1-x)^{3s}Q^{q-2s-2}.                          \tag{2.7}
$$



Then



$$
\omega_1=F^qP\,dx,\qquad \omega_0=F^qQP\,dx,           \tag{2.8}
$$



and



$$
\deg P=3q-6,\qquad\deg(QP)=3q-3.                       \tag{2.9}
$$



Thus exactly the exponents $q-1$ and $2q-1$ can survive
$\mathcal C^e$.

The only algebraic exception suppressed by $q\ge5$ is $q=3,t=0$.
It cannot occur here with $q=q_p$ and $p<2m$: the equality $q_p=3$
forces $4m+1<9$, hence $m=1$, but then $3\not<2m$.

## 3. The exact $2\times2$ determinant

Let



$$
P=\sum_n c_nx^n\quad\text{in }\mathbb F_p[x],
 \qquad c_n=0\quad(n<0).
$$



Define



$$
\begin{aligned}
 a_1&=c_{q-1},& b_1&=c_{2q-1},\\
 a_0&=\sum_{j=0}^3c_{q-1-j},&
 b_0&=\sum_{j=0}^3c_{2q-1-j}.
\end{aligned}                                             \tag{3.1}
$$



Cartier gives the exact identities



$$
\mathcal C^e(\omega_i)=F(a_i+b_ix)\,dx,
 \qquad i=0,1.                                           \tag{3.2}
$$



Hence the two images are linearly dependent if and only if



$$
\boxed{
 \Delta_{q,s}:=a_0b_1-b_0a_1
 =(c_{q-2}+c_{q-3}+c_{q-4})c_{2q-1}
 -(c_{2q-2}+c_{2q-3}+c_{2q-4})c_{q-1}=0
 \quad\text{in }\mathbb F_p.}                            \tag{3.3}
$$



Formula (3.3) includes the cases in which one or both images vanish.
It is the promised exact classification: at the next rank,
proportionality is no longer a consequence of degree alone; it is one
specific coefficient determinant.

There is an equivalent rational-series form useful for calculation.  Set



$$
W={u^{3s}\over Q^{2s+2}}=\sum_{n\ge0}w_nx^n,
 \qquad Z=QW=\sum_{n\ge0}z_nx^n.
$$



Since $P=Q^qW$ and $Q^q=1+x^q+x^{2q}+x^{3q}$, cancellation in
(3.3) gives



$$
\boxed{\Delta_{q,s}=z_{q-1}w_{2q-1}-z_{2q-1}w_{q-1}.}   \tag{3.4}
$$



Equivalently,



$$
W={x^{3s}(1-x)^{5s+2}\over(1-x^4)^{2s+2}},\qquad
 Z={x^{3s}(1-x)^{5s+1}\over(1-x^4)^{2s+1}}.              \tag{3.5}
$$



## 4. Divisibility of the primitive post-$G_m$ content

Define the new exact zero set



$$
\mathcal Z_m=\{p<2m:p\text{ odd prime},\ q_p\ge5,
 \ \delta_p=0,\ \Delta_{q_p,s_p}=0\},                    \tag{4.1}
$$



where $\delta_p,s_p$ are determined by (2.1) and (2.6) with
$q=q_p$.

**Theorem 4.1.**  The actual primitive item-133 content satisfies



$$
\boxed{\prod_{p\in\mathcal H_m\cup\mathcal Z_m}p\mid c_m.}      \tag{4.2}
$$



Only one copy of each prime is asserted.

**Proof.**  For $p\in\mathcal Z_m$, (3.3) makes the two Cartier images
dependent.  The relative endpoint congruence at the top denominator layer
therefore makes



$$
(q_pR_i,L_i,E_i),\qquad i=0,1,
$$



dependent modulo $p$.  Taking the two relevant minors gives



$$
q_pA_m\equiv0\pmod p,
 \qquad 8B_m\equiv0\pmod p.                              \tag{4.3}
$$



The restriction $p<2m$ keeps $p$ out of $T$, and



$$
v_p(D_m^\sharp)=v_p(K)=e_p.                              \tag{4.4}
$$



If $p\notin\mathcal P_m$, equations (4.3)--(4.4) give



$$
v_p(X_m)\ge1,\qquad v_p(Y_m)\ge e_p+1.                  \tag{4.5}
$$



No factor is removed by $G_m$, so $p\mid U_m,V_m$.

If $p\in\mathcal P_m$, the first Cartier images of both
differentials are zero.  Therefore their $e_p$-fold images are zero,
and the relative endpoint congruence gives each coordinate separately
zero modulo $p$.  The two minors are then one valuation deeper:



$$
v_p(X_m)\ge2,\qquad v_p(Y_m)\ge e_p+2.                  \tag{4.6}
$$



Division by the single squarefree factor of $G_m$ leaves



$$
v_p(U_m)\ge1,\qquad v_p(V_m)\ge e_p+1.                  \tag{4.7}
$$



Thus $p\mid c_m$ in both cases.  The previous rank-one theorem handles
$\mathcal H_m$, and (4.2) follows. $\square$

This proof is again about content after removal of $G_m$.  It neither
recounts the removed rank-zero factor nor proves a second surviving
$p$-adic digit.

## 5. Floor intervals and the absolute rank-two radical ceiling

For the prime-number-theorem scale, primes with $q_p>p$ have
$p\le\sqrt{4m+1}$ and total radical logarithm $o(m)$.  Put $q=p$
and suppose $\delta=0$.  Then



$$
a=3j,\qquad b=2j,\qquad j\ge1,                          \tag{5.1}
$$



and, away from endpoints, $x=p/m$ lies in



$$
\boxed{{6\over3j+1}<x<{2\over j}.}                      \tag{5.2}
$$



The exact residue parameter satisfies



$$
2m=jp+s,\qquad0\le s\le{p-1\over3},\qquad s\equiv j\pmod2.    \tag{5.3}
$$



If every determinant in every interval (5.2) vanished, the largest
possible additional radical mass would be



$$
\begin{aligned}
 C_2
 &=\sum_{j\ge1}\left({2\over j}-{6\over3j+1}\right)\\
 &=6-{\pi\over\sqrt3}-3\log3\\
 &=0.8903637697614535\ldots .                              \tag{5.4}
\end{aligned}
$$



Indeed, the ordinary PNT applies after truncating the interval union, and
the omitted tail lies below $O(m/J)$, exactly as in the rank-one
calculation.  Since $\mathcal Z_m$ is a subset of these intervals,



$$
\limsup_{m\to\infty}{1\over m}
 \log\prod_{p\in\mathcal Z_m}p\le C_2.                  \tag{5.5}
$$



Thus even the maximal hypothetical case in which every next-rank determinant
vanished could improve the normalized radical lower bound only to



$$
{C_1+C_2\over6}=0.28490812992172176\ldots .              \tag{5.6}
$$



The target is



$$
h-{d\over2}=1.1561471519642446\ldots,
$$



so rank at most two would still miss it by at least



$$
\boxed{0.8712390220425228\ldots\quad\text{per }6m}       \tag{5.7}
$$



even under maximal vanishing.  This is a radical ceiling, not a bound on
higher prime powers in $c_m$.

## 6. Three proved zero rays are arithmetically thin

The determinant does vanish on several exact moving-residue rays.  The
following three families are uniform for $q=p$.

### 6.1 The reciprocal ray $p=3s+4$

If $p=3s+4$ is prime, then $s$ is odd and



$$
\boxed{\Delta_{p,s}=0.}                                  \tag{6.1}
$$



For $p\ge13$, write



$$
P=x^{3s}J,\qquad
 J=(1-x)^{2s-2}(1-x^4)^{s+2}=\sum h_nx^n.
$$



The degree of $J$ is $2p-2$, and reciprocity gives



$$
h_{2p-2-n}=-h_n,\qquad h_{p-1}=0.                       \tag{6.2}
$$



Since $a_1=h_3$ and $a_0=h_0+h_1+h_2+h_3$, the low coefficients give



$$
a_1=-{2(s-2)(s-1)(2s-3)\over3},\qquad
 a_0=-{(s-2)(2s-5)(2s-3)\over3},
$$



and $p=3s+4$ therefore gives



$$
14a_0=23a_1\pmod p.                                    \tag{6.3}
$$



To obtain the other ratio, logarithmic differentiation of $J$ gives



$$
(n+1)h_{n+1}+(2s-2)(h_n+h_{n-1}+h_{n-2})
 +(2p+1-n)h_{n-3}=0.                                    \tag{6.4}
$$



At $n=p-2$, use (6.2) and $s\equiv-4/3\pmod p$ to get



$$
h_{p-2}+h_{p-3}+h_{p-4}={9\over14}h_{p-5}.              \tag{6.5}
$$



Here



$$
b_1=-h_{p-5},\qquad
 b_0=-(h_{p-5}+h_{p-4}+h_{p-3}+h_{p-2}).
$$



Thus reciprocity and (6.5) give



$$
14b_0=23b_1\pmod p,                                     \tag{6.6}
$$



which proves (6.1).  For $p=7,s=1$, both coefficients of the
$\omega_1$ image vanish directly.

### 6.2 The sparse-support ray $p=5s+2$

If



$$
p=5s+2,\qquad s\equiv1\pmod4,
$$



then



$$
P=x^{3s}(1-x^4)^{3s}.                                   \tag{6.7}
$$



Neither $p-1$ nor $2p-1$ lies in its exponent support.  Hence



$$
a_1=b_1=0,\qquad \boxed{\Delta_{p,s}=0}.                 \tag{6.8}
$$



The congruence condition is equivalent to $p\equiv7\pmod{20}$.

### 6.3 The common-constant ray $p=5s+1$

If



$$
p=5s+1,\qquad s\equiv2\pmod4,
$$



then



$$
QP=x^{3s}(1-x^4)^{3s},\qquad
 P=x^{3s}(1-x^4)^{3s-1}(1-x).                            \tag{6.9}
$$



The coefficient of $x^{2p-1}$ vanishes in both polynomials.  Thus



$$
b_0=b_1=0,\qquad \boxed{\Delta_{p,s}=0}.                 \tag{6.10}
$$



Here the congruence condition is $p\equiv11\pmod{20}$.

For a fixed $m$, equation (5.3) turns these rays into divisors of three
linear integers:



$$
\begin{array}{c|c}
 p=3s+4 & p\mid3m+2,\\
 p=5s+2 & p\mid5m+1,\\
 p=5s+1 & p\mid10m+1.
\end{array}                                               \tag{6.11}
$$



Therefore the product of all primes supplied by these three families is
at most



$$
(3m+2)(5m+1)(10m+1),                                    \tag{6.12}
$$



and its logarithm is $O(\log m)=o(m)$.  These are genuine new
divisors but supply no positive asymptotic radical constant.

The three rays are not asserted to exhaust (3.3).  For example,
$(p,s)=(53,13),(73,3),(79,9),(107,23),(137,17)$ are additional
prime-layer zeros in the finite audit.  At present they have no proved
uniform continuation or positive-density law.

## 7. No whole floor cell forces the determinant to vanish

The failure of an interval-only conclusion can be made exact.  For
$s=0$, direct extraction from



$$
W={1\over Q^2}={(1-x)^2\over(1-x^4)^2}
$$



gives



$$
\Delta_{p,0}=
 \begin{cases}
  -(3p+1)/4,&p\equiv1\pmod4,\\
  (p+1)/4,&p\equiv3\pmod4,
 \end{cases}                                             \tag{7.1}
$$



and hence



$$
\Delta_{p,0}\equiv\mp{1\over4}\ne0\pmod p.            \tag{7.2}
$$



For $s=1$, coefficient extraction from



$$
W={x^3(1-x)^7\over(1-x^4)^4}
$$



gives



$$
\Delta_{p,1}=
 \begin{cases}
 -\dfrac{7(p-1)^2(2p^3+2p^2+15p+9)}{192},&p\equiv1\pmod4,\\[2mm]
 -\dfrac{(p-3)(p-1)(p+1)(34p^2-20p-21)}{192},&p\equiv3\pmod4.
 \end{cases}                                             \tag{7.3}
$$



Thus



$$
\Delta_{p,1}\equiv
 \begin{cases}-21/64,&p\equiv1\pmod4,\\+21/64,&p\equiv3\pmod4,
 \end{cases}                                             \tag{7.4}
$$



which is nonzero for every admissible prime except $p=7$.

For the even-parity interior witness one may similarly extract the
$s=2$ coefficients.  Modulo $p$, they give



$$
\Delta_{p,2}\equiv
 \begin{cases}-1815/512,&p\equiv1\pmod4,\\+1815/512,&p\equiv3\pmod4.
 \end{cases}                                             \tag{7.5}
$$



This is nonzero for every admissible prime $p>11$.  For an even floor
label $j$, choose $s=2$; for an odd label choose $s=1$.  Equation
(5.3) then gives an integer $m$, and for every sufficiently large prime
it lies strictly inside the $j$-th delta-zero cell with $q_p=p$.
Equations (7.4) and (7.5) show that its determinant is nonzero.  Therefore
no entire floor interval (5.2) is an automatic
Cartier-zero interval.  A positive mass theorem for $\mathcal Z_m$
would require new information about the roots of (3.3), not merely the
degree cutoff.

## 8. Consequence for the remaining content problem

For $q_p\ge5$, equations (2.3) and (2.6) show that
$\mathcal H_m$ and $\mathcal Z_m$ are disjoint.  The exact theorem
therefore gives



$$
{\log c_m\over6m}\ge
 {1\over6m}\log\prod_{p\in\mathcal H_m}p
 +{1\over6m}\log\prod_{p\in\mathcal Z_m}p.               \tag{8.1}
$$



The three proved moving rays contribute only $o(1)$ to the second
term.  Hence the currently proved asymptotic lower bound remains



$$
\liminf {\log c_m\over6m}\ge0.13651416829481286\ldots,   \tag{8.2}
$$



and the still-unfilled amount remains



$$
\boxed{1.0196329836694318\ldots\quad\text{per }6m.}      \tag{8.3}
$$



The stronger number (5.7) is only an optimistic ceiling calculation for
all rank-at-most-two radicals.  Neither statement controls the
multiplicity term



$$
\sum_p\bigl(v_p(c_m)-\mathbf1_{p\in\mathcal H_m\cup\mathcal Z_m}\bigr)
 \log p.                                                  \tag{8.4}
$$



Even after all fresh primes are excluded, that prime-power mass remains
the decisive unresolved quantity.

## 9. Deterministic replay

The companion program

`scripts/mixed_cubic_rank_two_cartier_certificate.py`

uses frozen exact coordinates for $1\le m\le100$ and the isolated
factor probes at $m=150,200$.  It checks the degree classification,
the determinant, divisibility of the post-$G_m$ content, the sharper valuation bounds
$v_p(U_m)\ge1$, $v_p(V_m)\ge e_p+1$, the fixed-$s$ formulas, and
the three uniform rays.  The frozen run contains 1,062 delta-zero rows,
124 vanishing rows, and zero failures.  This finite computation audits
normalization and formulas only; all uniform and asymptotic assertions
above are proved independently.
