> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Positive integer CRT localizers cancel asymptotically the full prime window

Checked: 2026-08-27 UTC.

## 1. Verdict

Put



$$
u=1+x^2.
$$



For every sufficiently large positive integer $q$, this note constructs
an explicit integer polynomial $h_q$ such that



$$
\boxed{
 h_q\equiv1\pmod {u^2},\qquad h_q(0)=0,\qquad
 0\leq h_q(x)\leq1\quad(0\leq x\leq1).}                  \tag{1}
$$



Its order and degree are



$$
\boxed{
 n_q=\operatorname {ord}_0h_q=20q,\qquad
 d_q=\deg h_q=48q+11.}                                   \tag{2}
$$



Write



$$
r_q=\frac{h_q-1}{u},\qquad
 I_{0,q}=\int_0^1r_q(x)\,dx,\qquad
 I_{1,q}=\int_0^1xr_q(x)\,dx,                            \tag{3}
$$



and let $D_q$ be the least positive common clearing denominator of
$I_{0,q},I_{1,q}$.

The complete natural prime window is



$$
\frac{48q+11}{3}<p<20q.          \tag{4}
$$



Define



$$
K_q=40q^2+44q+5,                \tag{5}
$$



and



$$
{\cal P}_q=
 \left\{p\ {\rm prime}:
 \frac{48q+11}{3}<p<20q,\quad p\nmid K_q\right\}.         \tag{6}
$$



For every $p\in{\cal P}_q$, both moments are $p$-integral:



$$
\boxed{
 2r_{p-1}+r_{2p-1}\equiv0\pmod p,\qquad
 r_{2p-2}\equiv0\pmod p.}                                \tag{7}
$$



Moreover,



$$
\boxed{
 \sum_{p\in{\cal P}_q}\log p=4q+o(q),}                   \tag{8}
$$



while the mass of the complete window (4) is also $4q+o(q)$.
Thus the cancelled fraction tends to one:



$$
\boxed{
 \frac{\sum_{p\in{\cal P}_q}\log p}
 {\sum_{d_q/3<p<n_q}\log p}\longrightarrow1.}            \tag{9}
$$



More precisely,



$$
\boxed{
 \gcd\!\left(D_q,\prod_{d_q/3<p<n_q}p\right)\mid K_q.}    \tag{10}
$$



Consequently the part of the common moment denominator supported in the
entire one-third window has logarithmic size only $O(\log q)$, even
though that window has Chebyshev mass $4q+o(q)$.

This is an unconditional, arbitrarily growing positive integral family.
The CRT coefficient is an ordinary integer; no rational scaling is used,
and the constant term of the correction factor is one.

The theorem closes the aggregate question for the two isolated moments
in the negative: positivity and $h\equiv1\pmod {u^2}$ do not force a
positive proportion of the window product into their common
denominator.  It does not address a third moment or the full correction
output.

This package proves neither irrationality nor transcendence of
$e+\pi$.

## 2. The base and shifted padding

Use the sparse positive base



$$
B_q(x)=x^{20q}(5q+1-5qx^4).      \tag{11}
$$



The identity



$$
y^m(m+1-my)-1
 =-(y-1)^2\sum_{j=0}^{m-1}(j+1)y^j                      \tag{12}
$$



with $m=5q,y=x^4$ proves



$$
B_q\equiv1\pmod {u^2}.           \tag{13}
$$



The derivative



$$
\frac{d}{dy}\left(y^{5q}(5q+1-5qy)\right)
 =5q(5q+1)y^{5q-1}(1-y)\geq0
$$



on $[0,1]$ proves



$$
0\leq B_q\leq1.                 \tag{14}
$$



Also,



$$
\operatorname {ord}_0B_q=20q,\qquad
 \deg B_q=20q+4.                                         \tag{15}
$$



Put



$$
R_q=\frac{B_q-1}{u}.             \tag{16}
$$



Then $R_q\in\mathbb Z[x]$ is even and has degree $20q+2$.

The shifted padding is



$$
\boxed{
 w_q(x)=x^{12q}(1-x^4)^{4q}(1-x^2).}                    \tag{17}
$$



The exponents correspond to



$$
m=5q,\qquad L=4q,\qquad A=2L-m=3q.                     \tag{18}
$$



Define



$$
G_q=B_quw_q.                    \tag{19}
$$



Because $u(1-x^2)=1-x^4$,



$$
\boxed{
 G_q=x^{32q}(5q+1-5qx^4)(1-x^4)^{4q+1}.}                \tag{20}
$$



Thus $G_q$ is supported only in degrees divisible by four.

## 3. Every actual window prime lies in the coefficient range

Let $p$ satisfy the natural window (4), and set



$$
E_p=2p-2,\qquad O_p=2p-1,
$$





$$
t=t_q(p)=\frac{p-1}{2}-8q.       \tag{21}
$$



Since $p$ is odd and



$$
p>16q+\frac{11}{3},
$$



one has $p\geq16q+5$, and hence



$$
t\geq2.                    \tag{22}
$$



The upper bound $p<20q$ gives $p\leq20q-1$, so



$$
t\leq2q-1<4q+1.            \tag{23}
$$



Thus the coefficient in (20) is always within the range of
$(1-x^4)^{4q+1}$; no bottom subwindow is lost.

For both cases $p\equiv1,3\pmod4$, $E_p\equiv0\pmod4$,
whereas



$$
E_p-1\equiv3,\qquad O_p\equiv1,\qquad O_p-1\equiv0
 \pmod4.                                                 \tag{24}
$$



Consequently the ITEM96 coefficient matrix is diagonal:



$$
\begin{pmatrix}
 [x^{E_p}]G_q &[x^{E_p-1}]G_q\\
 [x^{O_p}]G_q &[x^{O_p-1}]G_q
 \end{pmatrix}
 =
 \begin{pmatrix}g_p&0\\0&g_p\end{pmatrix},
 \qquad g_p=[x^{E_p}]G_q.                                \tag{25}
$$



Also,



$$
E_p\geq32q+8>20q+2=\deg R_q,                            \tag{26}
$$



so $[x^{E_p}]R_q=0$.  Equation (25) has exactly the ITEM96
orientation: its first row controls $r_{2p-2}$, while its second row
controls $r_{2p-1}$ in
$2r_{p-1}+r_{2p-1}$.

## 4. Exact diagonal nonvanishing

Writing $y=x^4$ in (20) and using (21) gives



$$
\begin{aligned}
 g_p
 &=(-1)^t\left\{
 (5q+1)\binom{4q+1}{t}
 +5q\binom{4q+1}{t-1}\right\}\\
 &=(-1)^t\binom{4q+1}{t}
 \frac{(5q+1)(4q+2)-t}{4q+2-t}.                          \tag{27}
\end{aligned}
$$



All factorials in the binomial coefficient, and the denominator in the
second line, are strictly between zero and $p$.  They are therefore
units modulo $p$.

Substitution of (21) gives the exact identity



$$
2\bigl((5q+1)(4q+2)-t\bigr)
 =40q^2+44q+5-p=K_q-p.                                  \tag{28}
$$



Since $p$ is odd, (27)--(28) prove



$$
\boxed{
                         g_p\equiv0\pmod p
                         \iff p\mid K_q.}                 \tag{29}
$$



Thus every prime in ${\cal P}_q$ has an invertible diagonal matrix.
All determinant failures in the complete natural window are supported
on prime divisors of the single quadratic integer $K_q$.

## 5. The nondegenerate product has full window mass

Let



$$
P_q=\prod_{p\in{\cal P}_q}p.
$$



Distinct degenerate primes divide $K_q$, hence



$$
\sum_{\substack{d_q/3<p<n_q\\p\mid K_q}}\log p
 \leq\log K_q=O(\log q).                                 \tag{30}
$$



The prime number theorem, in the form
$\vartheta(x)=x+o(x)$, gives



$$
\begin{aligned}
 \log P_q
 &=\vartheta(20q)-\vartheta((48q+11)/3)+O(\log q)\\
 &=4q+o(q).                                              \tag{31}
\end{aligned}
$$



This proves (8), and also shows that ${\cal P}_q$ is nonempty for
every sufficiently large $q$.

## 6. One integer CRT coefficient

For $p\in{\cal P}_q$, put



$$
\varepsilon_p=(-1)^{(p+1)/2}.
$$



Impose



$$
c\equiv2\varepsilon_pg_p^{-1}
                         \pmod p.                         \tag{32}
$$



Let $c_q$ be the least nonnegative simultaneous CRT representative:



$$
0\leq c_q<P_q.                  \tag{33}
$$



Each residue in (32) is nonzero, and ${\cal P}_q\ne\varnothing$ for
large $q$, so



$$
0<c_q<P_q.                      \tag{34}
$$



This is an ordinary integer CRT.  There is no division in the
coefficients of the eventual polynomial.

## 7. Exact capacity of the shifted padding

For $z=x^4\in[0,1]$, the varying part of (17) is



$$
z^{3q}(1-z)^{4q}.
$$



Its logarithmic derivative vanishes only at $z=3/7$, and its endpoint
values are zero.  Therefore



$$
\boxed{
 \max_{0\leq z\leq1}z^{3q}(1-z)^{4q}
 =\left(\frac37\right)^{3q}
  \left(\frac47\right)^{4q}.}                            \tag{35}
$$



Define the real capacity



$$
Q_q=
 \frac{7^{7q}}{4\,3^{3q}4^{4q}}.                        \tag{36}
$$



Then



$$
\log Q_q
 =q\bigl(7\log7-3\log3-4\log4\bigr)-\log4.              \tag{37}
$$



The strict margin over the prime-window mass is



$$
\boxed{
 \Gamma=7\log7-3\log3-4\log4-4>0.}                      \tag{38}
$$



For a completely elementary verification of the sign, observe that



$$
\frac{7^7}{3^3\,4^4}>81>e^4,
$$



where $e<3$.  Taking logarithms proves (38).

Equations (31), (37), and (38) give



$$
\log(Q_q/P_q)=\Gamma q+o(q).                            \tag{39}
$$



Hence, for all sufficiently large $q$,



$$
\frac{Q_q}{P_q}\geq
 \exp\!\left(\frac{\Gamma}{2}q\right)>2.                 \tag{40}
$$



Combining (34) and (40) yields



$$
4c_q
 \left(\frac37\right)^{3q}
 \left(\frac47\right)^{4q}\leq1.                         \tag{41}
$$



Thus the least CRT representative fits with an explicit exponential
capacity margin.

## 8. The positive integral construction

Define



$$
\boxed{
 h_q(x)=B_q(x)\left(1-c_qu^2xw_q(x)\right).}              \tag{42}
$$



All coefficients are integers.  Both factors are congruent to one
modulo $u^2$, and the second factor has constant term one.  Therefore
$h_q(0)=0$ and



$$
\operatorname {ord}_0h_q=20q.    \tag{43}
$$



On $[0,1]$, the factors $x$, $1-x^2$, and $u^2/4$ lie in
$[0,1]$.  Equations (35) and (41) give



$$
0\leq c_qu^2xw_q\leq1.           \tag{44}
$$



Hence the second factor in (42) lies in $[0,1]$.  The same is true of
$B_q$, proving (1).

Because $c_q>0$,



$$
\begin{aligned}
 \deg w_q&=28q+2,\\
 \deg(1-c_qu^2xw_q)&=28q+7,\\
 \deg h_q&=(20q+4)+(28q+7)=48q+11,                       \tag{45}
\end{aligned}
$$



which proves (2).

Division of (42) by $u$ gives



$$
\boxed{
 r_q=R_q-c_qxG_q.}                                       \tag{46}
$$



For $p\in{\cal P}_q$, equations (25)--(26), (32), and (46) imply



$$
r_{2p-2}=0,\qquad
 r_{2p-1}=-c_qg_p\equiv-2\varepsilon_p\pmod p.           \tag{47}
$$



Since $p<n_q$, the forced low coefficient is
$r_{p-1}=\varepsilon_p$.  Thus (7) holds in exactly the ITEM96
orientation, and both moments are $p$-integral.

## 9. Aggregate denominator conclusion

Every nondegenerate window prime belongs to ${\cal P}_q$ and is absent
from $D_q$.  Any window prime which can divide $D_q$ must therefore
divide $K_q$.  Since the product



$$
\prod_{d_q/3<p<n_q}p
$$



is squarefree, (10) follows.

There is no hidden higher prime-power layer here.  For a window prime,
$d_q<3p\leq p^2$, while the monomial denominators in (3) are at most
$d_q$.  Hence the $p$-part of the reduced common denominator has
exponent at most one.  The gcd in (10) is therefore exactly the factor of
$D_q$ supported on window primes.

The complete window mass is



$$
\begin{aligned}
 \sum_{d_q/3<p<n_q}\log p
 &=\vartheta(20q)-\vartheta((48q+11)/3)\\
 &=4q+o(q).                                              \tag{48}
\end{aligned}
$$



Together with (31), this proves (9).  In particular,



$$
\log\gcd\!\left(D_q,\prod_{d_q/3<p<n_q}p\right)
 \leq\log K_q=O(\log q),                                 \tag{49}
$$



which is exponentially smaller than the full window product.

## 10. Finite exact replay instance

The replay uses $q=10$.  Then



$$
\begin{gathered}
 n=200,\qquad d=491,\qquad K=4445,\\
 {\cal P}=\{167,173,179,181,191,193,197,199\},\\
 P=1352708312947727201,\\
 c=898906612637494089.                                   \tag{50}
\end{gathered}
$$



No prime in the natural window divides $K$, so all eight window primes
are cancelled.

The exact coefficient data are



$$
\begin{array}{c|r|r|r}
p&t&g_p\bmod p&c\bmod p\\ \hline
167&3&7&48\\
173&6&139&112\\
179&9&83&41\\
181&10&140&106\\
191&15&39&98\\
193&16&76&66\\
197&18&88&94\\
199&19&129&108
\end{array}                                               \tag{51}
$$



Every last entry equals $2\varepsilon_pg_p^{-1}\bmod p$.

The positivity inequality is replayed without floating point:



$$
4c\,3^{30}4^{40}
 <7^{70}.                                                \tag{52}
$$



Exact expansion verifies (46)--(47), and exact rational reduction
verifies that the common moment denominator is coprime to $P$.
This finite instance checks normalization only; the asymptotic theorem
is the proof above.

## 11. Scope and replay

This theorem shows that the two-moment prime-window denominator
obstruction can be reduced from exponential window mass to at most a
quadratic integer $K_q$, despite integrality, positivity, and exact
Robin congruence.  Any successful common-kernel argument must therefore
use a further channel or a constraint absent from $I_0,I_1$.

The theorem does not prove that primes dividing $K_q$ actually occur
in the moment denominator, and does not treat the full correction
output.

From the research directory run

    python3 scripts/common_kernel_positive_crt_asymptotic_full_window_certificate.py
    sha256sum -c results/common_kernel_positive_crt_asymptotic_full_window_hashes.sha256

The deterministic replay verifies all polynomial identities, support
and ITEM96 orientation, the closed coefficient formula, the degeneracy
criterion, CRT reconstruction, exact beta-type maximum data, positivity
inequality, degree/order, all window residues, and reduced rational
denominators for $q=10$.  The PNT and capacity asymptotics are proved
above and are not extrapolated from finite data.

The replay uses exact CPU arithmetic, no hardware accelerator, and only
a negligible fraction of the available Colab RAM.  No conclusion about
$e+\pi$ is claimed.
