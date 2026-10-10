> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 250 — fixed-$r$ localization of the ordinary $j=2$ $p^2$ gate

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Retain the normalized Item 219 cell



$$
p=2r+6s+3,\qquad r\ge1\text{ odd},\qquad Q=2s,
 \tag{1.1}
$$



and, for $\nu=0,1$, put



$$
q_\nu=Q-\nu,\qquad \epsilon_\nu=1+3\nu,\qquad
 P_\nu=(1-z)^r(1+z)^{\epsilon_\nu}(1+z^2)^{q_\nu}. \tag{1.2}
$$



This item concerns the **ordinary $p^2$ common-log gate**. It does not
assume the stronger $p^3\mid C_\nu$ hypothesis of Items 235/239.

> **PROVED — exact fixed-$r$ affine localization.** Under
> 

$$
>                         \bar Q=-\frac{2r+3}{3},    \tag{1.3}
>
$$


> the two moving beta tails become
> 

$$
>                         X_\nu=\mathsf a_\nu e+\mathsf b_\nu c+\mathsf d_\nu,
>                         \qquad c=2^Q,
>                                                               \tag{1.4}
>
$$


> with one common period $e$. The first resonance is inhomogeneous:
> 

$$
>                         J_{2r+3}=\frac{c-1}{Q+2r+3}\pmod p.   \tag{1.5}
>
$$


> The $-1$ is the unique $z^p$ coefficient.

> **PROVED — exact rank-one cancellation.** The two upper $B$-tails
> have a common factorial period $\mathfrak f$ and fixed-$r$
> coefficients $f_0,f_1$. Coefficient reversal proves
> 

$$
>                         \mathsf a_\nu=\kappa_r f_\nu\quad(\nu=0,1).   \tag{1.6}
>
$$


> Hence
> 

$$
> G_\nu=f_\nu Z+P_\nu^\flat c+H_\nu^\flat,\qquad
> Z=9\kappa_re-\mathfrak f.                           \tag{1.7}
>
$$



> **PROVED — fixed-$r$ necessary resultant.** Define
> 

$$
> \begin{aligned}
> L_r&=f_0P_1^\flat-f_1P_0^\flat,\\
> M_r&=f_0H_1^\flat-f_1H_0^\flat,\\
> \mathcal R_r&=L_r^3+2^{2r+2}M_r^3.
> \end{aligned}                                      \tag{1.8}
>
$$


> Every simultaneous ordinary collision satisfies
> 

$$
>             L_rc+M_r=0\pmod p,\qquad
>             \boxed{\mathcal R_r=0\pmod p}.          \tag{1.9}
>
$$


> Every denominator is a $p$-unit on every actual row.

> **PROVED — neither eliminant is sufficient.** For example,
> 

$$
> (p,s,r)=(367,39,65),\qquad(G_0,G_1)=(238,354),     \tag{1.10}
>
$$


> yet $L_rc+M_r=\mathcal R_r=0\pmod p$. There are also
> cubic-only false positives, including $(67,7,11)$.

> **OPEN.** No all-prime nonvanishing or weighted zero theorem for
> $\mathcal R_r$ is proved. The common period $Z$ remains genuine on
> exceptional rows. Item 250 books no capacity reduction.

## 2. Reflected ordinary gate

Set



$$
A_p=-\sum_{k=1}^{p-1}\frac{z^k}{k},\qquad
 B_p=\sum_{k=1}^{p-1}\frac{(-1)^{k-1}z^{2k}}{k}.     \tag{2.1}
$$



Direct reindexing gives



$$
A_p(z)=-z^pA_p(1/z),\qquad B_p(z)=z^{2p}B_p(1/z).  \tag{2.2}
$$



Since $r$ is odd, $P_\nu(z)=-z^{\deg P_\nu}P_\nu(1/z)$. With



$$
\tau_\nu=p-q_\nu-1,\qquad T=p-r-1,
$$



the Item 219 coordinate is exactly



$$
\boxed{
 G_\nu=9[z^T]A_pP_\nu
       -10[z^{\tau_\nu}]B_pP_\nu-[z^T]B_pP_\nu.}       \tag{2.3}
$$



All contributing logarithm indices lie in $1,\ldots,p-1$, so
$A_p,B_p$ may be replaced coefficientwise by
$\log(1-z),\log(1+z^2)$. No analytic continuation is used.

## 3. Affine $A$-period and Frobenius terminal

Write



$$
K_0=(1-z)^r(1+z),\qquad K_1=(1-z)^r(1+z)^4,\qquad
 K_\nu=\sum_\ell k_{\nu,\ell}z^\ell.                \tag{3.1}
$$



Define



$$
J_k=\sum_{t=0}^{Q-1}\binom{Q-1}{t}\frac1{Q+k+2t},
 \qquad c=2^Q.                                      \tag{3.2}
$$



Expanding only the fixed-degree $K_\nu$ factors gives



$$
\begin{aligned}
 X_0&=\sum_\ell k_{0,\ell}(J_{\ell+1}+J_{\ell+3}),\\
 X_1&=\sum_\ell k_{1,\ell}J_\ell.
 \end{aligned}                                      \tag{3.3}
$$



Equivalently, these are the finite beta sums



$$
X_\nu=\int_0^1t^{q_\nu}(1-t)^r(1+t)^{\epsilon_\nu}
                         (1+t^2)^{q_\nu}\,dt.        \tag{3.4}
$$



Differentiating $t^{Q+k}(1+t^2)^Q$ gives



$$
(3Q+k)J_{k+2}=c-(Q+k)J_k.  \tag{3.5}
$$



At $k_*=2r+3$, $3Q+k_*=p$. The term $t=Q-1$ of
$J_{k_*+2}$ has denominator $p$ and coefficient $1$. Thus
$pJ_{k_*+2}\equiv1\pmod p$, proving (1.5). Starting from



$$
J_0=e,\qquad J_1=\alpha_rc+\beta_r,                \tag{3.6}
$$



backward propagation from (1.5), followed by (3.5), yields
$J_k=u_ke+v_kc+w_k$ through $k=r+4$. Every coefficient here is a
rational function of $Q$. On an actual row $Q\equiv\bar Q\pmod p$,
and Section 7 proves that every denominator remains a unit. Substitution
of (1.3) therefore proves (1.4) row by row with fixed-$r$ arithmetic.

The resonance is essential. At $r=1$,



$$
\alpha_1=-\frac{87}{10},\quad\beta_1=\frac{27}{10},
 \quad X_0=-9c+3,\quad G_0=-81c-33.                 \tag{3.7}
$$



For $(p,s)=(23,3)$, $c=18$, so $G_0=4\pmod{23}$, exactly
the frozen Item 219 value. Dropping the $1$ in the resonant term gives
the wrong row.

## 4. Fixed-$r$ $B$-tails

For $K=\sum k_\ell z^\ell$, write $\ell=\ell_0+2t$ and set



$$
N_0=\frac{n-\ell_0}{2},\qquad D_0=N_0-q.
$$



The terminating-binomial derivative gives



$$
\begin{aligned}
 &[z^n]K(z)(1+z^2)^q\log(1+z^2)\\
 &\quad=(-1)^{D_0-1}\frac{q!(D_0-1)!}{N_0!}
 \sum_t k_{\ell_0+2t}(-1)^t
       \frac{(-N_0)_t}{(1-D_0)_t}.                 \tag{4.1}
 \end{aligned}
$$



Every sum has length at most $r+4$. For the lower targets $\tau_\nu$,
the prefactors before phase specialization are



$$
C_{a,0}=(-1)^r\frac{Q!r!}{(Q+r+1)!},\qquad
 C_{a,1}=(-1)^{r+1}\frac{(Q-1)!(r+1)!}{(Q+r+1)!}.  \tag{4.2}
$$



Let their specialized complete values be $u_0,u_1$.

For the upper target $T$, set



$$
D=\frac{r+Q+1}{2},\qquad R=Q+D,\qquad
 \mathfrak f=(-1)^{D-1}\frac{Q!(D-1)!}{R!}.         \tag{4.3}
$$



Then



$$
[z^T]P_0\log(1+z^2)=\mathfrak f f_0,\qquad
 [z^T]P_1\log(1+z^2)=\mathfrak f f_1.              \tag{4.4}
$$



At the phase,



$$
\bar D=\frac r6,\qquad \bar R=-\frac{r+2}{2},\qquad
 \rho=-\frac{\bar D}{\bar Q}=\frac{r}{2(2r+3)},     \tag{4.5}
$$



and



$$
\begin{aligned}
 f_0&=\sum_t k_{0,2t+1}(-1)^t
              \frac{(-\bar R)_t}{(1-\bar D)_t},\\
 f_1&=\rho\sum_t k_{1,2t+1}(-1)^t
              \frac{(-\bar R)_t}{(-\bar D)_t}.
 \end{aligned}                                      \tag{4.6}
$$



The factor $\rho$ is the exact prefactor ratio
$C_{T,1}/C_{T,0}=-D/Q$; the common factorial period was not divided
out.

## 5. Exact reciprocal rank one

Write $r=2h+1$ and define



$$
H_t=(-1)^t\frac{(\bar Q/2)_t}{(3\bar Q/2)_t},      \tag{5.1}
$$





$$
\kappa_r=
 \frac{2(4h+5)}{9(4h+3)}(-1)^h
 \frac{((5-2h)/6)_h}{(h+3/2)_h}.                   \tag{5.2}
$$



The $e$-coefficients $\mathsf a_\nu$ in (3.3) are



$$
\begin{aligned}
 \mathsf a_0&=\sum_{t=0}^{h}k_{0,2t+1}(H_{t+1}+H_{t+2}),\\
 \mathsf a_1&=\sum_{t=0}^{h+2}k_{1,2t}H_t.         \tag{5.3}
 \end{aligned}
$$



Reciprocity gives



$$
z^{r+1}K_0(1/z)=-K_0(z),\qquad
 z^{r+4}K_1(1/z)=-K_1(z).                          \tag{5.4}
$$



Using



$$
(x)_{n-t}=(x)_n\frac{(-1)^t}{(1-x-n)_t},          \tag{5.5}
$$



the definitions (1.3), (4.5), and (5.1)--(5.2) give termwise



$$
\begin{aligned}
 &k_{0,2t+1}(H_{t+1}+H_{t+2})\\
 &\quad=\kappa_r k_{0,2(h-t)+1}(-1)^{h-t}
       \frac{(-\bar R)_{h-t}}{(1-\bar D)_{h-t}},    \tag{5.6}\\
 &k_{1,2t}H_t\\
 &\quad=\kappa_r\rho k_{1,2(h+2-t)+1}(-1)^{h+2-t}
       \frac{(-\bar R)_{h+2-t}}{(-\bar D)_{h+2-t}}. \tag{5.7}
 \end{aligned}
$$



Clearing the displayed Pochhammer denominators makes these polynomial
identities, so zero coefficient terms require no division. Summation
proves $\mathsf a_\nu=\kappa_rf_\nu$. The proof includes $r=1$:
$\mathsf a_0=f_0=0$ and $\mathsf a_1=\kappa_1f_1$.

## 6. Gate compression and resultant

With



$$
X_\nu=\mathsf a_\nu e+\mathsf b_\nu c+\mathsf d_\nu,\qquad
 Y_\nu=u_\nu,\qquad
 [z^T]P_\nu\log(1+z^2)=\mathfrak f f_\nu,           \tag{6.1}
$$



the reflected gate becomes



$$
G_\nu=f_\nu(9\kappa_re-\mathfrak f)
       +9\mathsf b_\nu c+(9\mathsf d_\nu-10u_\nu). \tag{6.2}
$$



Thus $P_\nu^\flat=9\mathsf b_\nu$,
$H_\nu^\flat=9\mathsf d_\nu-10u_\nu$, and



$$
f_0G_1-f_1G_0=L_rc+M_r.    \tag{6.3}
$$



No division by $f_\nu,\mathsf a_\nu$, or a determinant occurs. Also,



$$
3Q+2r+2=p-1,\qquad 2^{2r+2}c^3=2^{p-1}=1\pmod p. \tag{6.4}
$$



Cubing $L_rc=-M_r$ proves (1.9).

Equation (6.3) is only formal compatibility for the common period $Z$.
If $(f_0,f_1)\ne(0,0)$, it asserts that some formal $Z$ solves both
rows, not that it is the actual period. If $f_0=f_1=0$, the two
scalar right sides must separately vanish. The checker preserves this
rank distinction.

## 7. Unit audit

Since $p\equiv2r\pmod3$ and $p>3$, every actual row has
$3\nmid r$. Thus the apparent $3\mid r$ phase singularity has no
prime row.

For every $J_k$ used in (3.3),



$$
1\le Q+k+2t\le3Q+r+2=p-r-1<p.                     \tag{7.1}
$$



The forward pivots used satisfy



$$
1\le3Q+k\le3Q+r+2=p-r-1<p,                       \tag{7.2}
$$



and the descending odd pivots satisfy



$$
1\le Q+k\le Q+2r+3=p-2Q<p.                       \tag{7.3}
$$



At the sole resonant pivot $3Q+(2r+3)=p$, no inverse is taken.
In $J_{2r+5}$, exactly its final summand has denominator $p$, and
its coefficient is $\binom{Q-1}{Q-1}=1$. Hence the contribution is
retained as $pJ_{2r+5}\equiv1$, before reduction.

The two $B$-tail ranges must be audited separately.  For both lower
tails,



$$
N_a=r+Q+1<p.                                      \tag{7.4}
$$



The $\nu=0$ factorials are $Q!,r!,N_a!$, and the $\nu=1$
factorials are $(Q-1)!,(r+1)!,N_a!$.  With $r=2h+1$, their
hypergeometric indices end at $h+1<r+1$ and $h+2<r+2$, respectively,
strictly before the first zero of $(-r)_t$ or $(-r-1)_t$.

For the upper tails,



$$
D=\frac{r+Q+1}{2}=h+s+1,\qquad
 R=Q+D=\frac{p-r-2}{2}<p.                          \tag{7.5}
$$



Their factorials are $Q!,(D-1)!,R!$ and
$(Q-1)!,D!,R!$.  The two hypergeometric ranges satisfy
$t\le h<D$ and $t\le h+2\le D$, so the factors
$(1-D)_t$ and $(-D)_t$ do not reach zero.

Finally, the phase substitutions are reductions of these actual unit
representatives:



$$
Q-\bar Q=\frac p3,\quad
 N_a-(r+\bar Q+1)=\frac p3,\quad
 D-\bar D=\frac p6,\quad R-\bar R=\frac p2.        \tag{7.6}
$$



The factors in $(h+3/2)_h$ have odd numerators at most
$4h+1=2r-1<p$; the remaining explicit denominator of $\kappa_r$
contains $2r+1<p$, and that of $\rho$ contains $2r+3<p$.
The $H_t$ denominators are the already audited even forward pivots.
Constants $2,3$, and $c$ are units.  Numerator zeros are allowed and
are never inverted.

Consequently the reduced denominator of $\mathcal R_r$ is a $p$-unit.
No primitive-content division of $(L_r,M_r)$ is used, so a possible
prime in their common numerator is never discarded.

## 8. Exact finite replay

Through $p\le401$, the checker finds



$$
\begin{array}{lr}
\text{admissible rows}&1153\\
\text{direct phase-coordinate equalities}&6918\\
G_0=G_1=0&0\\
L_rc+M_r=0&3\\
\mathcal R_r=0&9.
\end{array}                                         \tag{8.1}
$$



On the same 1,153 rows, the checker executes 563,818 denominator and
resonance assertions.  These include all 50,814 summands of the first
resonant $J_{2r+5}$ strings, each with exactly one terminal denominator
$p$.  This is a bounded replay of the all-row inequalities in Section 7,
not a substitute for their proof.

The three linear false positives are



$$
\begin{array}{c|r|r|r|r}
 p&s&r&G_0&G_1\\ \hline
 271&7&113&173&136\\
 367&39&65&238&354\\
 383&27&109&382&152.
 \end{array}                                        \tag{8.2}
$$



The nine resultant zeros, written $(p,s,r)$, are



$$
\begin{gathered}
 (67,7,11),(109,12,17),(127,3,53),(241,34,17),
 (271,7,113),\\
 (307,23,83),(367,39,65),(373,18,131),(383,27,109).
 \end{gathered}                                     \tag{8.3}
$$



Selected larger exact linear false positives are



$$
\begin{gathered}
 (953,158,1),(2281,378,5),(5711,941,31),
 (1279,199,41),\\
 (3929,636,55),(1657,256,59),(367,39,65).
 \end{gathered}                                     \tag{8.4}
$$



The first has $G_0=0$ but $G_1=374\pmod{953}$. Rows
$(67,7,11)$ and $(127,3,53)$ are separately replayed as
cubic-only false positives.

The termwise identities are replayed for all 67 admissible odd
$r\le199$, totaling 6,934 exact rational equalities. This checks the
implementation; the all-$r$ proof is (5.4)--(5.7).

## 9. Arithmetic ceiling and rate

For fixed $r$, a nonzero numerator of $\mathcal R_r$ has only
finitely many prime divisors. This gives no global rate theorem because
$r$ ranges with the main parameter. The construction has individual
logarithmic height $O(r\log r)$; summing individual bounds over
linearly many $r$ is superlinear. Exact characteristic-zero zeros
have not been excluded.

Even complete control of the resultant would still require control of
the actual common period $Z$ on its zero rows. Therefore



$$
\boxed{\text{new booked rate from Item 250}=0}.  \tag{9.1}
$$



The $j=2$ capacity remains $2/35$ per $m$. This item makes no
claim about $e+\pi$.

## 10. Reproduction and labels

From the portable archive root:

~~~
python scripts/item250_j2_ordinary_phase_certificate.py \
  --output results/item250_j2_ordinary_phase_certificate.json
python scripts/item250_j2_ordinary_phase_certificate.py \
  --output results/item250_j2_ordinary_phase_certificate_replay.json
~~~

The checker uses only Python's standard library and frozen Item 219.

**PROVED**

- reflected gate (2.3);
- affine fixed-$r$ $A$-state and resonant terminal (1.5);
- both $B$-tail transformations, retaining their factorial period;
- termwise rank-one identity (1.6);
- collision implies both conditions (1.9);
- complete all-row denominator/unit audit, with the lower and upper
  factorial ranges treated separately and the sole Frobenius denominator
  retained rather than inverted.

**EXACT FINITE**

- direct agreement with all three Item 219 coordinates through
  $p\le401$;
- false-positive censuses (8.2)--(8.4);
- termwise rational replay through $r\le199$.

**OPEN**

- all-prime nonvanishing or weighted control of $\mathcal R_r$;
- exact characteristic-zero zero classification for $\mathcal R_r$;
- control of the actual period $Z$ on resultant-zero rows;
- any capacity reduction, Route-1 gain, or conclusion about $e+\pi$.
