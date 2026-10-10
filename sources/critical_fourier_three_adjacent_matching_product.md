> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Three adjacent critical-Fourier forms: an exact local product gain and its obstruction

Date: 2026-08-27.

## 1. Outcome

Fix an even integer $n\ge2$, put $q=q_n$, and consider the three
critical-Fourier forms with



$$
K_i=K+i,\qquad k_i=K_i+1,\qquad 0\le i\le2.
 \tag{1}
$$



For the $i$-th form, write its reduced Fourier coordinate ratio as



$$
\frac{4S_i}{C_{0,i}}=\frac{A_i}{B_i},
 \qquad \gcd(A_i,B_i)=1,\qquad B_i>0,
 \tag{2}
$$



and put



$$
d_i=\gcd(q,B_i),\qquad
 g_i=\gcd(M_i,d_i),\qquad
 h_i=d_i g_i.
 \tag{3}
$$



Here $M_i=(q/d_i)A_i-(B_i/d_i)p_n$, so $g_i$ is the complete
matching content after minimal coefficient matching.

Define the common one-block interval



$$
\mathcal I_{n,K}=\{p\text{ odd prime}:K+2<p\le2(K-n)\}.
 \tag{4}
$$



The endpoint-period recurrence and its nonzero Casoratian imply the exact
local inequality



$$
\boxed{
 p^a\parallel q,\ p\in\mathcal I_{n,K}
 \quad\Longrightarrow\quad
 \sum_{i=0}^{2}v_p(h_i)\le5a.}
 \tag{5}
$$



This includes all prime powers and all exceptional cases
$D_{n,K_i,p}=0$ or $U_{n,K_i,p}=0$.  No generic-digit hypothesis is
needed in (5).

Let



$$
q_{\mathrm{out}}
 =\prod_{\substack{p^a\parallel q\\p\notin\mathcal I_{n,K}}}p^a.
 \tag{6}
$$



Also put



$$
G_3=\gcd(g_0,g_1,g_2).
 \tag{6a}
$$



Then



$$
\boxed{
 \prod_{i=0}^{2}h_i
 \le q^5G_3
 \le q^5q_{\mathrm{out}}.}
 \tag{7}
$$



Consequently at least one $i\in\{0,1,2\}$ satisfies



$$
h_i
 \le q^{5/3}G_3^{1/3}
 \le q^{5/3}q_{\mathrm{out}}^{1/3}.
 \tag{8}
$$



If $\mathcal L_i=A_i+B_i\pi>0$ is the oriented primitive
$\pi$-form and $\Lambda_i^{\mathrm{prim}}$ is the fully primitive
matched value, then for at least one $i$,



$$
\boxed{
 \Lambda_i^{\mathrm{prim}}
 \ge
 \frac{\min_{0\le j\le2}\mathcal L_j}
 {q^{2/3}G_3^{1/3}}
 \ge
 \frac{\min_{0\le j\le2}\mathcal L_j}
 {q^{2/3}q_{\mathrm{out}}^{1/3}}.}
 \tag{9}
$$



Thus the hoped-for exponent $2/3$ follows if the triple common content
$G_3$, or more strongly the complementary factor
$q_{\mathrm{out}}$, is negligible.  There is no such theorem at
present.  In fact the unconditional estimate obtained by setting
$G_3\le q$ is exactly the old loss $\Lambda\ge\mathcal L/q$.

The obstruction is genuine already in the smallest nontrivial degree.
For $n=2$, $q_2=7$, and $K=9,10,11$, exact arithmetic gives



$$
d_i=g_i=7\qquad(0\le i\le2).
 \tag{10}
$$



Hence



$$
\prod_{i=0}^{2}h_i=7^6=q_2^6>q_2^5.
 \tag{11}
$$



Here $G_3=q_{\mathrm{out}}=q_2=7$; the prime $7$ lies below all
three one-block bands.  Therefore the
no-three-consecutive theorem does **not** imply an unconditional
$q^{5/3}$ bound or lower the established high-region constant
$1/\log2$.

## 2. The common band really gives three consecutive period indices

Suppose $p\in\mathcal I_{n,K}$.  For $0\le i\le2$, put



$$
s_i=2(K_i-n)-p,\qquad v_i=\frac{s_i-1}{2}.
 \tag{12}
$$



The inequalities in (4) show that each $p$ belongs to the one-block
band



$$
K_i<p\le2(K_i-n).
 \tag{13}
$$



The integers $s_i$ are odd, $0\le s_i<p$, and



$$
v_{i+1}=v_i+1.
 \tag{14}
$$



Moreover, (4) can be nonempty only when $K>2n+2$, and then



$$
p>K+2>2n+4.
 \tag{15}
$$



Since $p$ is odd, $p\ge2n+7$.  Thus



$$
c=\frac{p-2n-1}{2}\ge3,
 \tag{16}
$$



and the three values in (14) are consecutive admissible indices for the
accepted endpoint-period scalar recurrence.

For later use, write



$$
D_i=D_{n,K_i,p}\equiv C_{0,i}/p\pmod p,
 \qquad
 U_i=U_{n,K_i,p}\equiv S_i\pmod p.
 \tag{17}
$$



The first-digit theorem proves $p\mid C_{0,i}$ for all three forms,
whether or not $D_i$ vanishes.

## 3. Proof of the local prime-power inequality

Fix $p^a\parallel q$ with $p\in\mathcal I_{n,K}$.  Put



$$
\delta_i=v_p(C_{0,i}),\qquad
 \sigma_i=v_p(S_i),\qquad
 \beta_i=v_p(B_i).
 \tag{18}
$$



Since $p>K_i$, the Fourier denominators are $p$-adic units, so
$\sigma_i\ge0$, with the usual convention
$\sigma_i=+\infty$ when $S_i=0$.  The exact denominator formula is



$$
\beta_i=\max(0,\delta_i-\sigma_i),
 \tag{19}
$$



and $\delta_i\ge1$.  The exact matching-localization theorem gives



$$
p\mid g_i\quad\Longrightarrow\quad\beta_i=a.
 \tag{20}
$$



We first prove that $p$ can divide at most two of the three $g_i$.

### The case $a=1$

Put $\bar q=q/p\pmod p$.  It is nonzero, and
$p_n\ne0\pmod p$ because $\gcd(p_n,q_n)=1$.  The accepted
endpoint-period target



$$
F_i=4\bar q\,U_i-p_nD_i
 \tag{21}
$$



is a nonzero scalar solution of the order-three recurrence.

Suppose $p\mid g_i$.  By (19)--(20),



$$
\delta_i-\sigma_i=1.
 \tag{22}
$$



If $\delta_i=1$, then $\sigma_i=0$, and the exact normalized matching
congruence, divided by $p$, gives $F_i=0$.  If
$\delta_i\ge2$, then (22) gives $\sigma_i\ge1$, so



$$
D_i=0,\qquad U_i=0,
 \tag{23}
$$



and again $F_i=0$.  Thus



$$
p\mid g_i\quad\Longrightarrow\quad F_i=0.
 \tag{24}
$$



The nonzero solution $F$ cannot vanish at three consecutive admissible
indices.  Hence $p$ divides at most two of the $g_i$.

### The case $a\ge2$

If $p\mid g_i$, equations (19)--(20) give



$$
\delta_i-\sigma_i=a\ge2.
 \tag{25}
$$



In particular $\delta_i\ge2$, so $D_i=0$.  The central endpoint
period $D$ is itself a nonzero scalar solution: its nonzeroness follows
at once from the accepted nonzero three-by-three initial Casoratian.
It cannot have three consecutive zeros.  Therefore $p$ again divides
at most two of the $g_i$.

In either case,



$$
\sum_{i=0}^{2}v_p(d_i)\le3a,\qquad
 \sum_{i=0}^{2}v_p(g_i)\le2a,
 \tag{26}
$$



because $d_i\mid q$, $g_i\mid d_i$, and at least one $g_i$ has
zero $p$-adic valuation.  Adding (26) proves (5).

This proof explains exactly why neither exceptional digit is a loophole.
For $a=1$, an exceptional surviving prime forces both first digits to
vanish and is still a zero of $F$.  For $a\ge2$, any surviving
prime power forces a zero of $D$.  A value $U_i=0$ on the ordinary
branch $\delta_i=1$ gives $\beta_i=0$, so it cannot contribute to
$d_i$ or $g_i$.

## 4. Global product and the remaining support

Fix any prime $p^a\parallel q$, and put



$$
x_i=v_p(d_i),\qquad y_i=v_p(g_i),\qquad
 m=\min_{0\le i\le2}y_i.
 \tag{27}
$$



The unconditional divisibilities $g_i\mid d_i\mid q$ give
$0\le x_i,y_i\le a$.  Therefore



$$
\sum_{i=0}^{2}x_i\le3a,\qquad
 \sum_{i=0}^{2}y_i\le2a+m.
 \tag{27a}
$$



Indeed, after choosing an index at which $y_i=m$, each of the other
two valuations is at most $a$.  Consequently



$$
\sum_{i=0}^{2}v_p(h_i)\le5a+m.
 \tag{27b}
$$



Multiplication over all prime powers exactly gives the unconditional
inequality



$$
\boxed{\prod_{i=0}^{2}h_i\le q^5G_3.}
 \tag{28}
$$



For a prime in $\mathcal I_{n,K}$, the local theorem (5) says that at
least one $y_i$ is zero.  Hence no prime in the common band divides
$G_3$.  Since every $g_i\mid q$, one obtains



$$
\boxed{G_3\mid q_{\mathrm{out}}.}
 \tag{28a}
$$



Equations (28)--(28a) prove (7)--(8).  Equivalently, for a prime outside
$\mathcal I_{n,K}$, the elementary estimate alone gives only



$$
\sum_{i=0}^{2}v_p(h_i)\le6a.
 \tag{28b}
$$



The accepted positivity estimate for each matched form is



$$
\Lambda_i^{\mathrm{prim}}
 \ge\frac{q\mathcal L_i}{h_i}.
 \tag{29}
$$



Apply (29) to an index satisfying (8) and replace its
$\mathcal L_i$ by the minimum of the three.  This proves (9).

The one-block bands of the individual forms are



$$
\mathcal I_i=(K+i,\,2(K+i-n)].
 \tag{30}
$$



Their common part is (4).  When it is nonempty, the crossing primes in
the union but not the common part lie in the two short intervals



$$
(K,K+2]\ \cup\
 (2(K-n),\,2(K+2-n)].
 \tag{31}
$$



They are included in $q_{\mathrm{out}}$, because fewer than three
admissible period indices do not permit the no-three-consecutive
argument.  More importantly, $q_{\mathrm{out}}$ also contains every
prime factor of $q$ below all three bands and every factor above all
three bands.  No current result bounds this far-out part by
$q^{o(1)}$.

If along some chosen family one could prove



$$
\log G_3\le(\theta+o(1))\log q
 \qquad(0\le\theta\le1),
 \tag{32}
$$



then (9), the accepted estimate
$\log q\le(1+o(1))n\log n$, and the critical-Fourier lower bound would
give the conditional threshold



$$
c>\frac{2+\theta}{3\log2}
 \qquad\text{for }K\sim c\,n\log n.
 \tag{33}
$$



The proposed $2/(3\log2)$ is the special case $\theta=0$.
The only unconditional value is $\theta=1$, which returns
$1/\log2$.  A corresponding bound for $q_{\mathrm{out}}$ is a
sufficient, but stronger, hypothesis because of (28a).  Equation (9)
selects at least one member of each triple; it is not a bound for every
prescribed member.

## 5. Exact counterexample to an unconditional $q^5$ product

For $n=2$, the primitive exponential pair is



$$
(p_2,q_2)=(19,7).
 \tag{34}
$$



The three exact reduced Fourier ratios and matching residuals are



$$
\begin{array}{c|r|r|r|r|r}
k&K&A&B&M&d=g\\ \hline
10&9&-149056&135135&-515851&7\\
11&10&-70016&75075&-273791&7\\
12&11&-1313792&1684683&-5886503&7
\end{array}
\tag{35}
$$



In every row $v_7(B)=1$, $7\mid M$, and $49\nmid M$.  Therefore
$d=g=7$ exactly.  Since $7\le K_i$, it lies outside every
one-block interval and



$$
G_3=q_{\mathrm{out}}=q_2=7.
 \tag{35a}
$$



Thus equality holds in the first and last bounds of (7), and
(10)--(11) follow.

The counterexample is finite but logically decisive: it refutes the
unconditional local-to-global step, not merely an asymptotic heuristic.
It does not rule out a future theorem showing that
$q_{\mathrm{out}}$ is negligible in a specified asymptotic family.

## 6. Certificate and exact scope

The companion script reconstructs all three Fourier polynomials over
$\mathbb Z[i]$, computes $C_0,S,A,B,M,d,g$ with exact integer and
rational arithmetic, and verifies every entry of (35), including the
valuation statements, (35a), equality in (11), and equality in the
unconditional product bound (28).

Run

    python -m py_compile scripts/critical_fourier_three_adjacent_matching_product_certificate.py
    python scripts/critical_fourier_three_adjacent_matching_product_certificate.py

For a byte-identical rerun, use

    python scripts/critical_fourier_three_adjacent_matching_product_certificate.py \
      --output /tmp/critical_fourier_three_adjacent_matching_product_certificate.json
    cmp results/critical_fourier_three_adjacent_matching_product_certificate.json \
      /tmp/critical_fourier_three_adjacent_matching_product_certificate.json

The all-parameter content of this note is the local inequality (5), the
unconditional triple-gcd inequality (28), and its common-band
specialization (7).  The note does not prove a bound on $G_3$ or
$q_{\mathrm{out}}$, an improved unconditional high-region threshold,
divergence for every member of an adjacent block, or any arithmetic
classification of $e+\pi$.
