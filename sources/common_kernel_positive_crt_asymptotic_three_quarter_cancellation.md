> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Positive integer CRT localizers can cancel three quarters of the prime-window mass

Checked: 2026-08-27 UTC.

## 1. Verdict

Put



$$
u=1+x^2,\qquad
 \lambda_0=\frac{2}{2+\log4}=0.5906161091\ldots.          \tag{1}
$$



Fix once and for all



$$
\lambda_0<\lambda<1,             \tag{2}
$$



and, for every positive integer $m$, put



$$
L=L_m=\lfloor\lambda m\rfloor.   \tag{3}
$$



For all sufficiently large $m$, this note constructs explicitly an
integer polynomial $h_m$ satisfying



$$
\boxed{
 h_m\equiv1\pmod {(1+x^2)^2},\qquad h_m(0)=0,\qquad
 0\leq h_m(x)\leq1\quad(0\leq x\leq1).}                  \tag{4}
$$



Its localization order and degree are



$$
\boxed{
 n_m=\operatorname {ord}_0h_m=4m,\qquad
 d_m=\deg h_m=4m+8L_m+11.}                               \tag{5}
$$



Write



$$
r_m=\frac{h_m-1}{1+x^2},\qquad
 I_{0,m}=\int_0^1r_m(x)\,dx,\qquad
 I_{1,m}=\int_0^1xr_m(x)\,dx.                            \tag{6}
$$



There is a set ${\cal P}_m$ of primes inside



$$
d_m/3<p<n_m                    \tag{7}
$$



such that both moments are $p$-integral for every
$p\in{\cal P}_m$, and



$$
\boxed{
 \sum_{p\in{\cal P}_m}\log p
 =2(1-\lambda)m+o(m).}                                   \tag{8}
$$



The full interval (7) has Chebyshev mass



$$
\sum_{d_m/3<p<n_m}\log p
 =\frac83(1-\lambda)m+o(m).                              \tag{9}
$$



Consequently the construction cancels asymptotically



$$
\boxed{\frac34}
$$



of the complete one-third-window Chebyshev mass.

Equivalently, if $D_m$ is the least common clearing denominator of
$(I_{0,m},I_{1,m})$, then



$$
\gcd\!\left(D_m,\prod_{p\in{\cal P}_m}p\right)=1,
 \qquad
 \log\prod_{p\in{\cal P}_m}p
 =2(1-\lambda)m+o(m).                                    \tag{10}
$$



This is an unconditional, arbitrarily growing, positive integral
family.  The large CRT residue is damped by an integral endpoint factor;
there is no rational scaling and $h_m(0)=0$ is preserved exactly.

The theorem rules out any aggregate claim that positivity and the
congruence alone force more than one quarter of this natural window mass
to survive in the two isolated moment denominators.  It does not show
that the remaining quarter cancels, and it does not address a third
moment or the full correction output.

This package proves neither irrationality nor transcendence of
$e+\pi$.

## 2. The sparse positive base

Define



$$
B_m(x)=x^{4m}(m+1-mx^4).          \tag{11}
$$



With $y=x^4$, the identity



$$
y^m(m+1-my)-1
 =-(y-1)^2\sum_{j=0}^{m-1}(j+1)y^j                      \tag{12}
$$



and



$$
x^4-1=(x^2-1)(1+x^2)
$$



give



$$
B_m\equiv1\pmod {u^2}.           \tag{13}
$$



On $0\leq y\leq1$,



$$
\frac{d}{dy}\left(y^m(m+1-my)\right)
 =m(m+1)y^{m-1}(1-y)\geq0.                               \tag{14}
$$



The endpoint values are zero and one, so



$$
0\leq B_m(x)\leq1
                         \quad(0\leq x\leq1).             \tag{15}
$$



Moreover,



$$
\operatorname {ord}_0B_m=4m,\qquad \deg B_m=4m+4.       \tag{16}
$$



Put



$$
R_m=\frac{B_m-1}{u}\in\mathbb Z[x].
                                                                    \tag{17}
$$



It is even and has degree $4m+2$.

## 3. Padding which diagonalizes the residue system

Set



$$
w_{m}(x)=x^{4L}(1-x^4)^L(1-x^2),                        \tag{18}
$$



and



$$
G_m(x)=B_m(x)u\,w_m(x).           \tag{19}
$$



Since



$$
u(1-x^2)=1-x^4,
$$



one has the exact simplification



$$
\boxed{
 G_m(x)=x^{4(m+L)}
        (m+1-mx^4)(1-x^4)^{L+1}.}                        \tag{20}
$$



Thus $G_m$ is supported only in degrees divisible by four.

Let $p$ be an odd prime, and put



$$
E_p=2p-2,\qquad O_p=2p-1.        \tag{21}
$$



For both residue classes $p\equiv1,3\pmod4$, the even number $E_p$
is divisible by four:



$$
\begin{array}{c|c|c|c}
p\bmod4&E_p\bmod4&E_p-1\bmod4&O_p\bmod4\\ \hline
1&0&3&1\\
3&0&3&1.
\end{array}                                               \tag{22}
$$



It follows from (20) that the ITEM96 coefficient matrix is exactly



$$
\begin{pmatrix}
 [x^{E_p}]G_m &[x^{E_p-1}]G_m\\
 [x^{O_p}]G_m &[x^{O_p-1}]G_m
 \end{pmatrix}
 =
 \begin{pmatrix}g_p&0\\0&g_p\end{pmatrix},
 \qquad g_p=[x^{E_p}]G_m.                                \tag{23}
$$



This checks the orientation explicitly.  The first row controls
$r_{2p-2}$, the ITEM96 $I_1$ residue.  The second controls
$r_{2p-1}$, which enters the ITEM96 $I_0$ residue
$2r_{p-1}+r_{2p-1}$.

## 4. Exact nonvanishing of the diagonal coefficient

Consider primes in the top interval



$$
2m+2L<p<4m.                     \tag{24}
$$



Define



$$
t=t_{m,L}(p)
 =\frac{p-1}{2}-m-L.                                     \tag{25}
$$



Since the left endpoint of (24) is even and $p$ is odd,



$$
t\geq0.                    \tag{26}
$$



The upper endpoint gives



$$
t\leq m-L-1.               \tag{27}
$$



Because the fixed $\lambda$ in (2) is greater than $1/2$, for all
sufficiently large $m$,



$$
m-L-1\leq L+1.                  \tag{28}
$$



Thus $0\leq t\leq L+1$.

Writing $y=x^4$ in (20) gives



$$
\begin{aligned}
 g_p
 &=(-1)^t\left\{
 (m+1)\binom{L+1}{t}
 +m\binom{L+1}{t-1}\right\}\\
 &=(-1)^t\binom{L+1}{t}
 \frac{(m+1)(L+2)-t}{L+2-t},                             \tag{29}
\end{aligned}
$$



where the second binomial in the first line is read as zero at $t=0$.

Every prime in (24) is larger than $L+2$ for all sufficiently large
$m$.  Therefore the binomial coefficient and the denominator in the
second line of (29) are units modulo $p$.  Put



$$
K_{m,L}=2mL+6m+4L+5.             \tag{30}
$$



Substitution of (25) gives the exact identity



$$
2\bigl((m+1)(L+2)-t\bigr)=K_{m,L}-p.                    \tag{31}
$$



Since $p$ is odd, equations (29)--(31) prove



$$
\boxed{
 g_p\equiv0\pmod p
 \quad\Longleftrightarrow\quad
 p\mid K_{m,L}.}                                         \tag{32}
$$



The determinant in (23) is $g_p^2$.  Thus (32) is the exact
determinant/nonvanishing condition requested by the CRT construction.

## 5. The target prime set and its mass

Define



$$
\boxed{
 {\cal P}_m=
 \left\{p\ {\rm prime}:
 2m+2L<p<4m,\quad p\nmid K_{m,L}\right\}.}                \tag{33}
$$



The excluded primes are distinct prime divisors of the one integer
$K_{m,L}$.  Hence



$$
\sum_{\substack{2m+2L<p<4m\\p\mid K_{m,L}}}\log p
 \leq\log K_{m,L}=O(\log m),                              \tag{34}
$$



because $L=O(m)$ and $K_{m,L}=O(m^2)$.

Let $\vartheta(x)=\sum_{p\leq x}\log p$.  The prime number theorem and
$L=\lambda m+O(1)$ give



$$
\begin{aligned}
 \log P_m
 :=\sum_{p\in{\cal P}_m}\log p
 &=\vartheta(4m)-\vartheta(2m+2L)+O(\log m)\\
 &=2(m-L)+o(m)\\
 &=2(1-\lambda)m+o(m).                                   \tag{35}
\end{aligned}
$$



Endpoint conventions change (35) by at most $O(\log m)$.  In
particular, ${\cal P}_m$ is nonempty for every sufficiently large
$m$.

## 6. One-variable CRT and the positivity capacity

For $p\in{\cal P}_m$, let



$$
\varepsilon_p=(-1)^{(p+1)/2}.
$$



Since $g_p$ is a unit modulo $p$, impose the single residue



$$
c\equiv2\varepsilon_p g_p^{-1}
                         \pmod p.                         \tag{36}
$$



Let



$$
P_m=\prod_{p\in{\cal P}_m}p,
$$



and take the ordinary least nonnegative CRT representative:



$$
0\leq c_m<P_m.                  \tag{37}
$$



Every residue in (36) is nonzero.  Since ${\cal P}_m\ne\varnothing$
for large $m$,



$$
0<c_m<P_m.                      \tag{38}
$$



There is no rational normalization in (36)--(38).

The strict inequality defining $\lambda_0$ is exactly



$$
\delta_\lambda
 :=\lambda\log4-2(1-\lambda)>0.                           \tag{39}
$$



Equations (3) and (35) give



$$
(L-1)\log4-\log P_m
 =\delta_\lambda m+o(m).                                 \tag{40}
$$



Consequently, for all sufficiently large $m$,



$$
\frac{4^{L-1}}{P_m}
 \geq\exp\!\left(\frac{\delta_\lambda}{2}m\right),        \tag{41}
$$



and in particular even the stronger bookkeeping inequality



$$
2P_m\leq4^{L-1}                 \tag{42}
$$



holds.  Combining (37) with (42) gives



$$
c_m\leq4^{L-1}.                 \tag{43}
$$



Thus least-representative size is not the asymptotic obstruction.  The
padding has an explicit exponential capacity margin.

## 7. Construction and exact moment cancellation

Define



$$
\boxed{
 h_m(x)=B_m(x)
 \left(1-c_m u^2x\,w_m(x)\right).}                       \tag{44}
$$



All coefficients are integers.  Both factors are congruent to one
modulo $u^2$.  Since $xw_m$ has positive order at zero, the second
factor has constant term one; hence



$$
\operatorname {ord}_0h_m=4m.     \tag{45}
$$



On $[0,1]$,



$$
x^{4L}(1-x^4)^L
 =\bigl(x^4(1-x^4)\bigr)^L\leq4^{-L},                   \tag{46}
$$



while $0\leq x(1-x^2)\leq1$ and $u^2\leq4$.  Therefore



$$
0\leq c_mu^2xw_m
 \leq4c_m4^{-L}\leq1                                    \tag{47}
$$



by (43).  The second factor in (44) lies in $[0,1]$, and so does
$B_m$.  This proves (4).

Because $c_m>0$, the degrees of the padding, second factor, and product
are exactly



$$
\begin{aligned}
 \deg w_m&=8L+2,\\
 \deg(1-c_mu^2xw_m)&=8L+7,\\
 \deg h_m&=4m+8L+11,                                    \tag{48}
\end{aligned}
$$



which proves (5).  If the finite set ${\cal P}_m$ were empty, one
would only use the corresponding degree upper bound; (35) shows this
case never occurs once $m$ is sufficiently large.

Division of (44) by $u$ gives



$$
\boxed{
 r_m=R_m-c_mxG_m.}                                       \tag{49}
$$



For $p\in{\cal P}_m$, condition (24) gives



$$
E_p=2p-2>4m+2=\deg R_m.                                 \tag{50}
$$



Thus $[x^{E_p}]R_m=0$.  Equations (20), (23), and (49) give



$$
\begin{aligned}
 r_{2p-2}&=0,\\
 r_{2p-1}&=-c_mg_p\equiv-2\varepsilon_p\pmod p.           \tag{51}
\end{aligned}
$$



Since $p<n_m$, the forced low coefficient is
$r_{p-1}=\varepsilon_p$.  Therefore



$$
r_{2p-2}\equiv0,\qquad
 2r_{p-1}+r_{2p-1}\equiv0\pmod p,                        \tag{52}
$$



in exactly the ITEM96 orientation.  The two-moment residue theorem proves
(10).

## 8. Inclusion in the natural window and the three-quarter ratio

The lower endpoint of the selected interval exceeds the lower endpoint
of the natural moment window once $m$ is large:



$$
\begin{aligned}
 2m+2L-\frac{d_m}{3}
 &=2m+2L-\frac{4m+8L+11}{3}\\
 &=\frac{2m-2L-11}{3}>0.                                \tag{53}
\end{aligned}
$$



The last inequality holds because the fixed $\lambda<1$ gives
$m-L\to\infty$.  The upper endpoint $4m$ is exactly $n_m$.
Thus every prime in (33) satisfies (7), including all constant
$+11$ bookkeeping.

Finally, the prime number theorem and (5) give



$$
\begin{aligned}
 \sum_{d_m/3<p<n_m}\log p
 &=\vartheta(4m)-\vartheta(d_m/3)+o(m)\\
 &=\frac83(m-L)+o(m)\\
 &=\frac83(1-\lambda)m+o(m).                             \tag{54}
\end{aligned}
$$



Divide (35) by (54) to obtain



$$
\frac{\sum_{p\in{\cal P}_m}\log p}
      {\sum_{d_m/3<p<n_m}\log p}
 \longrightarrow\frac34.                                \tag{55}
$$



This is a statement about Chebyshev mass, not necessarily the ratio of
the numbers of primes, although the prime number theorem also supplies
the corresponding interval-count asymptotics.

## 9. A finite replay instance

The certificate uses the representative choice



$$
m=100,\qquad L=75               \tag{56}
$$



corresponding to $\lambda=3/4$.  Then



$$
\begin{aligned}
 K_{m,L}&=15905,\\
 n&=400,\qquad d=1011,\\
 {\cal P}&=\{353,359,367,373,379,383,389,397\},\\
 P&=388885850766419537617,\\
 c&=53995197867219543727.                                \tag{57}
\end{aligned}
$$



The complete natural window $337<p<400$ also contains $347,349$;
the construction cancels all eight primes in the top subinterval and
leaves those two outside the claimed set.

For the eight target primes, the exact data are



$$
\begin{array}{c|r|r|r}
p&t&g_p\bmod p&c\bmod p\\ \hline
353&1&343&212\\
359&4&205&345\\
367&8&342&88\\
373&11&20&261\\
379&14&307&200\\
383&16&51&353\\
389&19&148&205\\
397&23&270&347
\end{array}                                               \tag{58}
$$



In every row the last entry is
$2\varepsilon_pg_p^{-1}\bmod p$.  Exact expansion of (44) verifies
both residues in (52), and exact rational reduction verifies that the
common denominator of the two moments is coprime to $P$.

This finite instance checks normalization only.  The arbitrarily growing
family is proved in Sections 2--8 and does not follow by extrapolating
(58).

## 10. Scope and replay

The theorem proves that positive integral CRT interpolation can erase a
fixed positive fraction—indeed three quarters—of the natural prime-window
mass from both isolated moment denominators.  The determinant failure
set is confined to prime divisors of one $O(m^2)$ integer, and the
least CRT representative fits with exponential room.

The theorem does not cancel the bottom quarter of the window.  The
support restriction in (20) begins influencing the coefficient
$2p-2$ only in the top interval (24).  Reaching lower primes while
retaining the same capacity and degree constants requires a different
padding or more output structure.  Nor does this theorem control the
full correction channel.

From the research directory run

    python3 scripts/common_kernel_positive_crt_asymptotic_three_quarter_certificate.py
    sha256sum -c results/common_kernel_positive_crt_asymptotic_three_quarter_hashes.sha256

The deterministic replay checks all polynomial identities, the
diagonal matrix orientation for both odd residue classes, formula
(29), the equivalence (32), the finite CRT reconstruction, positivity,
degree/order, all ITEM96 residues, and the reduced moment denominators.
The PNT asymptotics and quantified inequalities are the proofs above;
finite computations are not used to infer them.

All replay arithmetic is exact and CPU-suitable.  It uses no hardware
accelerator and only a negligible fraction of the available Colab RAM.
No conclusion about $e+\pi$ is claimed.
