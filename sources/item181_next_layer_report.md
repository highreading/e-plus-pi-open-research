> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 181 — the next parity-compatible residual layer

Date: 2026-08-29

## 1. Scope and verdict

Take



$$
\epsilon_j=j\bmod2,\qquad s=\epsilon_j+2,\qquad
 m={(j+1)p-s-1\over2}.                                \tag{1.1}
$$



Thus $s=3$ for odd $j$ and $s=2$ for even $j$.

**PROVED — all-$j$ actual constrained nonidentity.**  For every fixed
$j\ge1$ and both $\rho=p\bmod4$, the next-layer $B_0$ digit is the
reduction of a nonzero rational constant $C^{(2)}_{j,\rho}$.  Hence
$B_0\ne0\pmod p$ for every sufficiently large admissible prime in each
fixed band.

An exact Cayley obstruction satisfies



$$
B_0=0\text{ over }\mathbb Q\Longrightarrow
 \Omega^{(2),\#}_{j,\rho}=0,\qquad
 \boxed{\operatorname {sgn}\Omega^{(2),\#}_{j,\rho}=(-1)^{j+1}}.
                                                               \tag{1.2}
$$



The sign formula is a theorem for every $j$, not a finite observation.

**PROVED — zero-rate scope.**  At fixed $m$, the union over all these
bands has at most


$$
\log((2m+3)(2m+4))=O(\log m)          \tag{1.3}
$$


log-prime weight.  Thus it gives no positive-rate content constant and no
conclusion about $e+\pi$.

## 2. Exact coefficients and primitives

Retain Item 172's repaired convention: form
$\widetilde\gamma_\nu$ and the resonantly cancelled primitive exactly
over $\mathbb Z$, then reduce.

For fixed $s$, Item 175's four-section formula gives



$$
\bar\gamma_0=\mathcal F(-5s-4,2s+1,3s+2),\qquad
\bar\gamma_1=\mathcal F(-5s-3,2s,3s+2),                \tag{2.1}
$$



because $\binom{p-c}{r}\equiv\binom{-c}{r}\pmod p$ for $p>r$.
Exact evaluation gives



$$
\begin{array}{c|r|r}
s&\bar\gamma_0&\bar\gamma_1\\ \hline
2&191600&118696\\
3&31260320&19414656.
\end{array}                                             \tag{2.2}
$$



Let $Q=1+x+x^2+x^3$, $u=x(1-x)$, and define $B_s$ by



$$
uB_s'-(3s+2)u'B_s
 =Q^{2s}(\bar\gamma_1Q-\bar\gamma_0),\qquad
 \deg B_s\le6s+2.                                      \tag{2.3}
$$



If $B_s=\sum b_rx^r$ and the right side is $\sum N_rx^r$, the exact
downward recurrence



$$
b_{r-1}={N_r-(r-3s-2)b_r\over6s+5-r},
 \quad r=6s+3,\ldots,1,\qquad b_{6s+3}=0               \tag{2.4}
$$



determines every coefficient.  The certificate stores the full lists and
verifies (2.3) by multiplication.  A convenient characteristic-$p$
primitive is



$$
\widehat T_s=u^{p-3s-2}B_s.       \tag{2.5}
$$



As in Item 177, a possible $c x^p$ difference from the literal reduction
of the exact primitive contributes only a multiple of the base vector and
drops from the wedge.

A sufficient cell threshold is



$$
\begin{array}{c|c}
s=2\ (j\text{ even})&p\ge\max(11,\,2j+3),\\
s=3\ (j\text{ odd})&p\ge\max(13,\,2j+3).
\end{array}                                             \tag{2.6}
$$



After this admissibility threshold, only the finite primes dividing the
numerator or denominator of the fixed rational constant must be omitted.

## 3. Actual constrained divisor data

After Gaussian Frobenius and $\tau_p$, assemble the actual values at
$-1,i,-i$ into $h=N(x)/Q(x)$.  Exact calculation gives



$$
\begin{array}{c|c|c}
s&\rho&N(x)\\ \hline
2&1&(-61360+2048x+12x^2)/21\\
2&3&(-63408-2048x-2036x^2)/21\\
3&1&(41795136+311296x+272384x^2)/165\\
3&3&(41483840-311296x-38912x^2)/165.
\end{array}                                             \tag{3.1}
$$



Under



$$
y={x+1\over1-x},\quad t=y-1,\quad D(y)=y(1+y^2),\quad
\Delta(t)=D(1+t)=2+4t+3t^2+t^3,                       \tag{3.2}
$$



put $M(y)=(1+y)^3N((y-1)/(y+1))$.  Clearing denominators gives the
coefficients of $M(1+t)$, low degree first:



$$
\begin{array}{c|c|c|rrrr}
s&\rho&\text{factor}&m_0&m_1&m_2&m_3\\ \hline
2&1&21&-490880&-728128&-359944&-59300\\
2&3&21&-507264&-769088&-392712&-67492\\
3&1&165&334361088&502786816&252560768&42378816\\
3&3&165&331870720&496560896&247580032&41133632.
\end{array}                                             \tag{3.3}
$$



These are actual primitive values, not ambient free coordinates.

The fixed rational constant is explicitly



$$
C^{(2)}_{j,\rho}=\chi_4(\rho)(-2j-2)
\sum_{a\in\{-1,i,-i\}}\tau_\rho(\widehat T_s(a))w^B_{j,a}. \tag{3.4}
$$



The first two bands are



$$
\begin{array}{c|c|c|c}
j&s&C^{(2)}_{j,1}&C^{(2)}_{j,3}\\ \hline
1&3&-2213120/33&8439040/33\\
2&2&8513771/16&-3277547/16.
\end{array}                                             \tag{3.5}
$$



The factor $\chi_4$ is the Item 177 correction to Item 172 (4.11).

## 4. Cayley obstruction

Put



$$
A=3j+2,\quad K=2j+2,\quad P(t)=\Delta(t)^K,\quad
p_r=[t^{A+r}]P(t)\ (r=2,3,4).                         \tag{4.1}
$$



Define



$$
q_j=\begin{pmatrix}2(A+1)\\4(A+1-K)\\3(A+1-2K)\\A+1-3K\end{pmatrix},
\qquad d=\begin{pmatrix}2\\4\\3\\1\end{pmatrix},       \tag{4.2}
$$





$$
c_j=\begin{pmatrix}
0\\
-2(A+2)p_2\\
-4(A+2-K)p_2-2(A+3)p_3\\
-3(A+2-2K)p_2-4(A+3-K)p_3-2(A+4)p_4
\end{pmatrix}.                                         \tag{4.3}
$$



With $m^\#_{s,\rho}$ from (3.3), set



$$
\Omega^{(2),\#}_{j,\rho}=\det[q_j\ c_j\ d\ m^\#_{s,\rho}]. \tag{4.4}
$$



Item 178's rational-exactness argument applies verbatim: vanishing of the
actual $B_0$ wedge forces an exact linear combination, whose four final
primitive coefficients force (4.4) to vanish.

For odd $j$,



$$
\begin{aligned}
\Omega^{(2),\#}_{j,1}
 &=1245184(j+1)\{(15j+12)p_2-(23j+33)p_3+(6j+12)p_4\},\\
\Omega^{(2),\#}_{j,3}
 &=1245184(j+1)\{(15j+12)p_2+(17j-9)p_3-(42j+84)p_4\}.
                                                               \tag{4.5}
\end{aligned}
$$



For even $j$,



$$
\begin{aligned}
\Omega^{(2),\#}_{j,1}
 &=128(j+1)\{-(1265j+1012)p_2+(-1027j+1003)p_3
 +(3054j+6108)p_4\},\\
\Omega^{(2),\#}_{j,3}
 &=128(j+1)\{-(1265j+1012)p_2+(1533j+2539)p_3
 -(18j+36)p_4\}.
                                                               \tag{4.6}
\end{aligned}
$$



## 5. Uniform sign proof

Let



$$
n=j+1,\quad k=3n+3,\quad
a_L=[t^{k-5}]\Delta^{2n-1},\quad
a_R=[t^{k-4}]\Delta^{2n-1}.                            \tag{5.1}
$$



Item 178's binomial decomposition proves



$$
a_L>a_R>0.                    \tag{5.2}
$$



Apply



$$
[t^k](t\,d/dt-k)(S\Delta^{2n})=0                     \tag{5.3}
$$



to the braces in (4.5)-(4.6), using



$$
\begin{array}{c|c|c}
s&\rho&S(t)\\ \hline
3&1&2-5t-3t^2\\
3&3&-14-13t-3t^2\\
2&1&1018+1015t+253t^2\\
2&3&-6+503t+253t^2.
\end{array}                                             \tag{5.4}
$$



Exact collection reduces the four braces to



$$
\begin{array}{c|c|c}
s&\rho&\text{brace}\\ \hline
3&1&2n(3a_L-a_R)>0\\
3&3&n(14a_R+6a_L)>0\\
2&1&-n(1018a_R+506a_L)<0\\
2&3&n(6a_R-506a_L)<0.
\end{array}                                             \tag{5.5}
$$



All signs follow from (5.2), proving (1.2) for every $j$.

## 6. Fixed-$m$ scope and replay

Equation (1.1) becomes



$$
\begin{array}{c|c}
j\text{ even},\ s=2&(j+1)p=2m+3,\\
j\text{ odd},\ s=3&(j+1)p=2m+4.
\end{array}                                             \tag{6.1}
$$



Thus relevant primes divide $2m+3$ or $2m+4$, and



$$
\sum\log p\le\log(2m+3)+\log(2m+4)=O(\log m).          \tag{6.2}
$$



The portable certificate verifies all coefficient, primitive, divisor,
determinant, and Euler identities.  It replays the theorem exactly for
$1\le j\le500$; this finite run is not the basis of the all-$j$
claim.  Its ordered obstruction stream digest is

    dd8ae14a67b5c5f011aa14bf5705193d8f526266b3a412c21fcde4af9ecc0aa6

Reproduction command:

    python work/item181_next_layer_certificate.py --max-j 500 --output work/item181_next_layer_certificate_replay.json

From work, default output is beside the script.  Archived under scripts,
default output is ../results/item181_next_layer_certificate.json.
