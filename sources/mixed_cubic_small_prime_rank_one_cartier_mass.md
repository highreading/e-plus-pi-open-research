> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Post-Cartier small-prime content: a rank-one divisor and the exact remaining mass

Date: 2026-08-28

## 1. Scope and conclusion

Put



$$
N=6m,\qquad K_0=4m+1,\qquad K_1=4m+2,
$$





$$
\omega_s={u^N\over Q^{K_s}}\,dx,\qquad
 u=x(1-x),\quad Q=(1+x)(1+x^2),\quad s=0,1.
$$



Write



$$
H_s=R_s+{L_s\over4}\log2+{E_s\over8}\pi,
$$





$$
A_m=L_1R_0-L_0R_1,\qquad
 B_m={L_1E_0-L_0E_1\over8}.
$$



As in the frozen item-133 normalization, let



$$
M_j=\operatorname {lcm}(1,\ldots,j),
$$





$$
M=M_{4m+1},\qquad
 T=\prod_{2m<p<3m}p,\qquad K=M/T,
$$





$$
D_m^\sharp=2^{9m+5}K,\qquad
 X_m=D_m^\sharp A_m,\qquad Y_m=D_m^\sharp B_m,
$$



and let



$$
G_m=\prod_{p\in\mathcal P_m}p,
\quad U_m=X_m/G_m,\quad V_m=Y_m/G_m,
\quad c_m=\gcd(U_m,V_m).
$$



The main theorem below gives a new divisor of the **post-$G_m$**
content.  Define, for an odd prime $p$,



$$
d_p(n,k)=
 \begin{cases}
  2r,&k\equiv0\pmod p,\\
  2r+3(p-t),&k\equiv t\pmod p,\quad1\le t<p,
 \end{cases}
 \qquad r\equiv n\pmod p,\quad0\le r<p,                 \tag{1.1}
$$



Explicitly, the already removed rank-zero Cartier set is



$$
\mathcal P_m=\left\{p\text{ odd prime}:
 \begin{array}{l}
 d_p(6m,4m+1)\le p-2,\\
 d_p(6m,4m+2)\le p-2
 \end{array}\right\}.
$$



For each odd prime $p\le4m+1$, put



$$
e_p=\max\{e:p^e\le4m+1\},\qquad q_p=p^{e_p}.
$$



Thus $q_p\le4m+1<pq_p$.  Define



$$
\mathcal H_m=\left\{p:\begin{array}{l}
 p\text{ odd prime},\quad p<2m,\\
 d_{q_p}(6m,4m+1)\le2q_p-2,\\
 d_{q_p}(6m,4m+2)\le2q_p-2
 \end{array}\right\}.                                  \tag{1.2}
$$



Then



$$
\boxed{\prod_{p\in\mathcal H_m}p\mid c_m.}             \tag{1.3}
$$



Moreover,



$$
\boxed{
 \log\prod_{p\in\mathcal H_m}p
 =(-4\log2+6\log3-3)m+o(m).}                             \tag{1.4}
$$



Consequently



$$
\boxed{
 \liminf_{m\to\infty}{\log c_m\over6m}
 \ge {-4\log2+6\log3-3\over6}
 =0.13651416829481286\ldots .}                            \tag{1.5}
$$



This is an unconditional positive exponential lower bound for the actual
extra content.  It is nevertheless far below the matching threshold



$$
h-{d\over2}=1.1561471519642446\ldots .                    \tag{1.6}
$$



The precise unfilled amount is



$$
\boxed{1.0196329836694318\ldots\quad\text{per }6m.}       \tag{1.7}
$$



The distinction is essential: (1.3) controls one valuation layer on an
explicit set of primes.  It does not bound the higher powers of those
primes and does not control simultaneous zeros at the other primes at most
$6m$.

## 2. A relative Cartier congruence without a two-pole restriction

We use the following form of the endpoint calculation.  It is slightly
more general than the relative Cartier lemma used for the middle band.

**Lemma 2.1 (top prime-power denominator layer).**  Let $p$ be odd,
let $e\ge1$, and put $q=p^e$.  Let $\omega$ be a rational
differential over $\mathbb Z_{(p)}$.  Assume that its finite poles are
separable modulo $p$, every pole order is at most $pq$, and every
polynomial-quotient monomial has degree at most $pq-2$.  Let



$$
\mathcal Z(\omega)=(R(\omega),L(\omega),E(\omega))
$$



denote its rational endpoint coordinate and its two simple-residue period
coordinates in the mixed-cubic basis.  Then



$$
\boxed{
 (qR(\omega),L(\omega),E(\omega))\pmod p
 =\operatorname{Frob}^{e}\bigl(
 \mathcal Z(\mathcal C^{e}\bar\omega)\bigr).}                    \tag{2.1}
$$



Here $\mathcal C$ is Cartier, the equality may be read after passing to
the unramified splitting algebra of $Q$, and Frobenius acts on that
algebra.  In particular, proportional Cartier images give proportional
vectors on the left of (2.1).

**Proof.**  Work term by term in the partial-fraction expansion.  The root
differences are units because $\operatorname {disc}Q=-16$.  Hence all
local Laurent coefficients are $p$-integral, also when the roots lie in
the unramified quadratic extension.

A pole term $a(x-\alpha)^{-j}dx$ contributes to the rational endpoint
coordinate with denominator $j-1$.  After multiplication by $q$, it
vanishes modulo $p$ unless



$$
j-1=qk,\qquad1\le k<p.
$$



For a surviving term,



$$
q\int_0^1{a\,dx\over(x-\alpha)^{qk+1}}
 =-{a\over k}\bigl((1-\alpha)^{-qk}-(-\alpha)^{-qk}\bigr),          \tag{2.2}
$$



which is the $e$-fold Frobenius of the endpoint integral of
$\mathcal C^e(a(x-\alpha)^{-qk-1}dx)$.  The restriction below $pq$
ensures that $k$ is a unit.  The same calculation for a polynomial term
$ax^jdx$ retains exactly the indices $j+1=qk$.  Simple poles are
retained by every Cartier iterate and give the two unscaled period
coordinates.  This proves (2.1).  Frobenius may interchange $i$ and
$-i$, but it acts on both coordinate vectors in the same semilinear way,
so proportionality is preserved. $\square$

For $\omega_0,\omega_1$, there is no polynomial part in the original
variable.  Their pole orders are at most
$K_1=4m+2\le p q_p$, so Lemma 2.1 applies with $q=q_p$.

## 3. The rank-one Cartier image

Fix an odd prime $p$, put $e=e_p$, $q=q_p$, and write



$$
N=aq+r,\qquad K_s=b_sq+t_s,qquad0\le r,t_s<q.                    \tag{3.1}
$$



Since $q$ is a power of $p$, in characteristic $p$,



$$
\omega_s=F_s^qP_s(x)\,dx,                                      \tag{3.2}
$$



where



$$
(F_s,P_s)=
 \begin{cases}
 \left(u^a/Q^{b_s},u^r\right),&t_s=0,\\
 \left(u^a/Q^{b_s+1},u^rQ^{q-t_s}\right),&t_s>0.
 \end{cases}                                                     \tag{3.3}
$$



The degree of $P_s$ is exactly $d_q(N,K_s)$.  If it is at most
$2q-2$, $\mathcal C^e$ can select only the coefficient of
$x^{q-1}dx$; the next eligible exponent is $2q-1$.  Hence



$$
\mathcal C^e(\omega_s)=\gamma_sF_s\,dx                          \tag{3.4}
$$



for some $\gamma_s$ in $\mathbb F_p$.

Under the two degree inequalities in (1.2), the functions $F_0,F_1$
are the same.  Indeed, $t_0=0$ is impossible, since it would give



$$
d_q(N,K_1)=2r+3(q-1)>2q-2.                                     \tag{3.5}
$$



If $1\le t_0\le q-2$, both denominators in (3.3) are
$Q^{b_0+1}$.  If $t_0=q-1$, then $t_1=0$, $b_1=b_0+1$, and
the two denominators are again equal.  Therefore



$$
\boxed{\mathcal C^e(\omega_0),\mathcal C^e(\omega_1)
 \text{ lie in one common one-dimensional space}.}               \tag{3.6}
$$



Zero is allowed in (3.6); no nonvanishing of either scalar $\gamma_s$
is assumed.

## 4. Divisibility after removing the squarefree Cartier product

Fix $p\in\mathcal H_m$, write $e=e_p$, $q=p^e$, and note that
$p<2m$ keeps it out of the omitted middle product $T$.  We have



$$
v_p(K)=v_p(M_{4m+1})=e,
 \qquad v_p(D_m^\sharp)=e.                                      \tag{4.1}
$$



By (2.1) and (3.6), the two vectors



$$
(qR_s,L_s,E_s),\qquad s=0,1,                                  \tag{4.2}
$$



are proportional modulo $p$.  Their two relevant minors give



$$
qA_m=L_1(qR_0)-L_0(qR_1)\equiv0\pmod p,                        \tag{4.3}
$$





$$
8B_m=L_1E_0-L_0E_1\equiv0\pmod p.                             \tag{4.4}
$$



If $p\notin\mathcal P_m$, equations (4.3)--(4.4) imply



$$
v_p(A_m)\ge1-e,\qquad v_p(B_m)\ge1.
$$



Using (4.1),



$$
v_p(X_m)\ge1,\qquad v_p(Y_m)\ge e+1.                           \tag{4.5}
$$



No factor $p$ is removed by $G_m$, so $p\mid U_m,V_m$.

It remains to audit the rank-zero case, because here one copy of $p$
is removed by $G_m$.  If $p\in\mathcal P_m$, then



$$
d_p(N,K_0),d_p(N,K_1)\le p-2,
$$



so $\mathcal C(\omega_0)=\mathcal C(\omega_1)=0$, and therefore
their $e$-fold Cartier images also vanish.  Equation (2.1) now gives,
separately for each $s$,



$$
qR_s\equiv L_s\equiv E_s\equiv0\pmod p.                        \tag{4.6}
$$



Thus



$$
v_p(R_s)\ge1-e,\qquad v_p(L_s),v_p(E_s)\ge1.                  \tag{4.7}
$$



The determinants have the one-deeper bounds



$$
v_p(A_m)\ge2-e,\qquad v_p(B_m)\ge2.                            \tag{4.8}
$$



After the clearing in (4.1),



$$
v_p(X_m)\ge2,\qquad v_p(Y_m)\ge e+2.                           \tag{4.9}
$$



Division by the single squarefree factor in $G_m$ still leaves



$$
v_p(U_m)\ge1,\qquad v_p(V_m)\ge e+1.                           \tag{4.10}
$$



This proves (1.3) in both cases.  Notice that the proof is genuinely about
the content after $G_m$: merely repeating the old rank-zero divisor
would not prove (4.10).

## 5. Prime-number-theorem mass

Away from interval endpoints, put $p/m\to x$, and set



$$
a=\left\lfloor{6\over x}\right\rfloor,
 \qquad b=\left\lfloor{4\over x}\right\rfloor.                  \tag{5.1}
$$



The two inequalities in (1.2) are equivalent to



$$
2a-3b\ge1.                                                       \tag{5.2}
$$



To solve (5.2), put $y=4/x$.  If $b=2j$, then



$$
2j+{2\over3}<y<2j+1,
$$



which gives



$$
{4\over2j+1}<x<{6\over3j+1}.                                   \tag{5.3}
$$



If $b=2j+1$, then



$$
2j+{4\over3}<y<2j+2,
$$



which gives



$$
{2\over j+1}<x<{6\over3j+2}.                                  \tag{5.4}
$$



For primes $p>\sqrt{4m+1}$, one has $e_p=1$, so (5.2) describes
$\mathcal H_m$ exactly away from endpoints.  The restriction $p<2m$
removes the $j=0$ intervals from both families.  The remaining primes
$p\le\sqrt{4m+1}$, on which the top layer is a higher prime power, have
total radical logarithm $o(m)$.  Therefore the prime number theorem,
first on finitely many intervals and then with a Chebyshev bound on the
tail, gives



$$
{1\over m}\log\prod_{p\in\mathcal H_m}p
 \longrightarrow C_{\rm even}+C_{\rm odd},                      \tag{5.5}
$$



where



$$
\begin{aligned}
 C_{\rm even}
 &=\sum_{j\ge1}\left({6\over3j+1}-{4\over2j+1}\right)\\
 &=-4\log2+{\pi\over\sqrt3}+3\log3-2,                          \tag{5.6}
\end{aligned}
$$



and



$$
\begin{aligned}
 C_{\rm odd}
 &=\sum_{j\ge1}\left({6\over3j+2}-{2\over j+1}\right)\\
 &=2\bigl(\psi(2)-\psi(5/3)\bigr)\\
 &=-1-{\pi\over\sqrt3}+3\log3.                                \tag{5.7}
\end{aligned}
$$



Their sum is



$$
\boxed{C_{\rm even}+C_{\rm odd}=-4\log2+6\log3-3
 =0.8190850097688771\ldots .}                                   \tag{5.8}
$$



For rigor in the infinite union, truncate at $j\le J$.  The ordinary
PNT handles that fixed finite union.  Every omitted interval lies below
$O(m/J)$, so Chebyshev's bound makes its logarithmic prime mass
$O(m/J)$.  Let $m\to\infty$, then $J\to\infty$.  The $+1,+2$
in $K_0,K_1$ can change only endpoint-sized sets in each fixed
truncation and therefore contribute $o(m)$.  This proves (1.4).

## 6. Exact valuation ledger and the prime-power obstruction

Let



$$
\widehat A_m=2^{9m+4}M_{4m+1}A_m\in\mathbb Z,
 \qquad \widehat B_m=2^{9m+5}B_m\in\mathbb Z.
$$



The exact local formula remains



$$
\begin{aligned}
 v_p(U_m)&={\bf1}_{p=2}+v_p(\widehat A_m)-v_p(T)-v_p(G_m),\\
 v_p(V_m)&=v_p(K)+v_p(\widehat B_m)-v_p(G_m),\\
 v_p(c_m)&=\min\{v_p(U_m),v_p(V_m)\}.                            \tag{6.1}
\end{aligned}
$$



The new theorem uses the full top denominator layer $q_p=p^{e_p}$, but
still supplies only



$$
v_p(c_m)\ge1\qquad(p\in\mathcal H_m).                          \tag{6.2}
$$



It does **not** supply a second $p$-adic digit.  Cartier is a
characteristic-$p$ operator: proportionality in (3.6) proves the
determinant congruences modulo $p$, but says nothing about their lifts
modulo $p^2$.  The iterate $\mathcal C^{e_p}$ detects the denominator
layer $p^{e_p}$ modulo $p$; it is not a congruence modulo
$p^{e_p}$.  A claim such as



$$
v_p(c_m)=O(\log_p m)                                             \tag{6.3}
$$



would make all primes $p\le\sqrt m$ contribute only $o(m)$, but no
such uniform bound follows from the residue or Hermite formulas currently
proved.

The local valuation ledger is sharp if one retains only the Cartier
congruences.  In the rank-one case, the two abstract coordinate triples



$$
(qR_0,L_0,E_0)=(1,1,1),\qquad
 (qR_1,L_1,E_1)=(1+p,1,1+p)                                    \tag{6.4}
$$



are proportional modulo $p$, but both relevant minors have valuation
exactly one.  Thus after a clearing of valuation $e$, the two cleared
coordinates can have valuations exactly $1$ and $e+1$.  In the
rank-zero case, take instead



$$
(qR_0,L_0,E_0)=(p,p,0),\qquad
 (qR_1,L_1,E_1)=(0,p,p).                                        \tag{6.5}
$$



Both triples vanish modulo $p$, while both minors have valuation exactly
two.  After the clearing and removal of one squarefree $G_m$-factor, the
two normalized valuations can be exactly $1$ and $e+1$.  These are
not claimed to be the actual period coordinates; they prove that the
Cartier congruences themselves contain no hidden second-digit conclusion.

Define the exact excess mass



$$
\mathcal E_m=
 \sum_p\left(v_p(c_m)-{\bf1}_{p\in\mathcal H_m}\right)\log p.    \tag{6.6}
$$



Then (1.3) gives $\mathcal E_m\ge0$, and exactly



$$
{\log c_m\over6m}
 ={\log\prod_{p\in\mathcal H_m}p\over6m}
  +{\mathcal E_m\over6m}.                                      \tag{6.7}
$$



If the separate fresh-prime theorem establishes
$p\mid c_m\Rightarrow p\le6m$, then (6.6) is a sum only over
$p\le6m$.  That support theorem does not bound its multiplicities.
To reach the matching threshold by internal content alone, one still needs
along the relevant subsequence



$$
{\mathcal E_m\over6m}>1.0196329836694318\ldots+o(1).             \tag{6.8}
$$



Smooth support alone cannot prove or disprove (6.8): an arbitrary power of
2 has support below $6m$ and can carry any prescribed linear logarithmic
mass.  Thus excluding all fresh primes combines with (1.3) to give a clean
support-and-mass reduction, but it does not close the prime-power problem.

Combining (1.5) with the already proved irrationality-measure upper bound
for the same actual content gives the rigorous bracket



$$
0.13651416829481286\ldots
 \le\liminf{\log c_m\over6m}
 \le\limsup{\log c_m\over6m}
 \le1.99566316016\ldots,                                        \tag{6.9}
$$



which still straddles (1.6).

## 7. Deterministic replay

The companion script

`scripts/mixed_cubic_small_prime_rank_one_cartier_certificate.py`

reads the frozen exact coordinate data for every $1\le m\le100$ and the
isolated exact probes at $m=150,200$.  It constructs $\mathcal H_m$
from (1.1)--(1.2) and checks integer divisibility of the exact $c_m$.
All 102 checked indices pass.  This is a finite audit of normalization and
endpoints only; (1.3)--(1.5) are proved above and are not extrapolated from
the table.
