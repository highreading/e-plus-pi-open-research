> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 288 — exact large-moving-prime redundancy of the $j=1$ endpoint scalar

Date: 2026-08-31

## 1. Result

Put



$$
r=2h,\qquad s_h=-\frac{4h+3}{6},\qquad h\geq1,
$$



and retain the lower and upper Gosper data of Items 229, 231, and 236.
Their common phase residual is denoted by $c_h$.  Let 

$$
L_h,d_h,U_h,F_h,
\eta_h
$$

 be Item 231's four endpoint quantities and endpoint ratio, so that
Item 280's rational endpoint scalar is



$$
K_h=2d_h\eta_hU_h-L_h(F_h-3d_h).                 \tag{1.1}
$$



Define the two finite rational sums



$$
\begin{aligned}
X_h&=-\sum_{j=0}^{2h-1}(-1)^j
       \binom{2s_h+j-1}{j},\\
Y_h&=\sum_{k=0}^{h}(-1)^k
       \frac{(3s_h+1)_k}{(s_h+2)_k}.
\end{aligned}                                      \tag{1.2}
$$



The main exact identities are



$$
\boxed{F_h-d_h=c_hX_h,\qquad
        \eta_hU_h+L_h=c_hY_h}                     \tag{1.3}
$$



for every $h\geq1$.  Consequently



$$
\boxed{K_h=c_hZ_h,\qquad Z_h=2d_hY_h-L_hX_h.}    \tag{1.4}
$$



Let



$$
\mathscr A_h=\mathbb Z\left[\frac1\ell:
       \ell\text{ prime},\ \ell\leq4h+3\right].  \tag{1.5}
$$



The proof below shows $c_h,X_h,Y_h,L_h,d_h,Z_h,K_h\in\mathscr A_h$.
For $3\nmid h$, Item 243 gives



$$
c_h=\mathcal G_hE_h^*,\qquad
 \mathcal G_h\in\mathscr A_h^\times.              \tag{1.6}
$$



If $N_E(h)$ and $N_K(h)$ are the reduced integer numerators of
$E_h^*$ and $K_h$, respectively, then (1.4)--(1.6) prove the
large-prime implication



$$
\boxed{q>4h+3,\ q\text{ prime},\ q\mid N_E(h)
        \quad\Longrightarrow\quad q\mid N_K(h).}  \tag{1.7}
$$



No converse is claimed.  Equivalently, whenever the quotient is defined,
every prime divisor of



$$
\frac{|N_E(h)|}{\gcd(|N_E(h)|,|N_K(h)|)}          \tag{1.8}
$$



is at most $4h+3$.  Every actual row prime has
$p=4h+6s_0+3\geq4h+9$, with $s_0\geq1$, so (1.7) covers every actual
moving prime.  Thus $K_h$ creates no additional large-moving-prime
codimension after the Item 222 condition $E_h^*=0\pmod p$.

## 2. Reflected Gosper antidifferences

For this section write $s=s_h$, and put



$$
A=2r+4s-1,\qquad B=r+1,\qquad C=-(r+8s).          \tag{2.1}
$$



Items 229 and 231 use



$$
\begin{aligned}
P^-(j)={}&A\binom{r+2s+4-2j}{r}
 +B\binom{r+2s+3-2j}{r}
 +C\binom{r+2s+2-2j}{r},\\
P^+(j)={}&C\binom{2j-r-1}{r}
 +B\binom{2j-r}{r}
 +A\binom{2j-r+1}{r}.
\end{aligned}                                      \tag{2.2}
$$



At the phase $2r+6s+3=0$, direct substitution gives



$$
P^+(j)=P^-(-2s-j).         \tag{2.3}
$$



Let



$$
\mathcal L_sR(j)=-(2s+j)R(j+1)-jR(j).             \tag{2.4}
$$



The lower and upper decompositions are



$$
P^\pm(j)=c_h+\mathcal L_sR^\pm(j),
 \qquad\deg R^\pm\leq r-1.                        \tag{2.5}
$$



Item 236 proves that the two residuals in (2.5) are equal.  Moreover,



$$
\widetilde R(j)=-R^-(-2s-j+1)                     \tag{2.6}
$$



satisfies



$$
\mathcal L_s\widetilde R(j)
   =(\mathcal L_sR^-)(-2s-j).                      \tag{2.7}
$$



The leading term of $\mathcal L_s(j^m)$ is $-2j^{m+1}$, so the
degree-$(r-1)$ antidifference in (2.5) is unique.  Equations
(2.3), (2.5), and (2.7) therefore prove



$$
\boxed{R^+(j)=-R^-(-2s-j+1).}                     \tag{2.8}
$$



This is an all-$h$ polynomial identity, not a finite interpolation.

## 3. The lower-to-upper endpoint telescoping

Put



$$
a=s+1,\qquad J=3h+3s+1=h-\frac12,
 \qquad b=a+h+1=-2s-J.                             \tag{3.1}
$$



At the phase, $2J-r+1=0$.  Hence the explicit binomial endpoint in
Item 231's definition of $U_h$ vanishes, and (2.8) gives



$$
U_h=-bR^-(b).              \tag{3.2}
$$



Define



$$
\mu_k=(-1)^k\frac{(3s+1)_k}{(s+2)_k},
 \qquad0\leq k\leq h+1.                           \tag{3.3}
$$



Then $\mu_0=1$, $\mu_{h+1}=\eta_h$, and



$$
\mu_{k+1}=-\mu_k\frac{3s+1+k}{s+2+k}.            \tag{3.4}
$$



Set $w_k=(a+k)R^-(a+k)$.  Multiplying (2.5) by $\mu_k$ at
$j=a+k$ and using (3.4) gives the exact one-step telescoping identity



$$
\mu_k\bigl(P^-(a+k)-c_h\bigr)
       =\mu_{k+1}w_{k+1}-\mu_kw_k.                 \tag{3.5}
$$



The three upper arguments in $P^-(a+k)$ are



$$
r+2-2k,\qquad r+1-2k,\qquad r-2k.                \tag{3.6}
$$



They are nonnegative on $0\leq k\leq h$.  Therefore



$$
P^-(a+k)=0\quad(k\geq2),                          \tag{3.7}
$$



while $P^-(a)$ is Item 229's first tail and $P^-(a+1)=A$.  Item
229's lower boundary can thus be written exactly as



$$
L_h=aR^-(a)+P^-(a)+\mu_1P^-(a+1).                \tag{3.8}
$$



Summing (3.5) for $0\leq k\leq h$, and then using
(3.2), (3.7), and (3.8), gives



$$
\eta_hU_h+L_h
 =c_h\sum_{k=0}^{h}\mu_k=c_hY_h.                 \tag{3.9}
$$



This proves the second identity in (1.3).

## 4. The fixed lower endpoint telescoping

Let



$$
t_j=(-1)^j\binom{2s+j-1}{j},\qquad
 D_n=[x^n](1-x)^{-r-1}(1+x^2)^{-2s}.               \tag{4.1}
$$



The logarithmic derivative of the generating function in (4.1) gives



$$
\begin{aligned}
0={}&(n+1)D_{n+1}-(n+r+1)D_n\\
   &+(n-1+4s)D_{n-1}-(n+r-1+4s)D_{n-2}.           \tag{4.2}
\end{aligned}
$$



Take minus (4.2) at $n=r+2$, plus (4.2) at $n=r+1$, plus (4.2) at
$n=r$.  Comparing with Item 231's definition of $d_h$ gives



$$
d_h=CD_r+BD_{r-1}+AD_{r-2}.                       \tag{4.3}
$$



Because $r=2h$ is even,



$$
\binom{m}{r}=\binom{r-m-1}{r}                    \tag{4.4}
$$



for every integer (m).  Expanding the three coefficients in (4.3) by
(4.1), using (4.4), and noting the ordinary binomial support gives



$$
\boxed{d_h=\sum_{j=0}^{r-1}t_jP^+(j).}           \tag{4.5}
$$



The Gosper identity



$$
t_j\mathcal L_sR(j)
  =(j+1)t_{j+1}R(j+1)-jt_jR(j)                    \tag{4.6}
$$



telescopes (2.5) over $0\leq j\leq r-1$.  Since
$F_h=rt_rR^+(r)$, equations (4.5) and (4.6) yield



$$
d_h=c_h\sum_{j=0}^{r-1}t_j+F_h,
 \qquad F_h-d_h=c_hX_h.                            \tag{4.7}
$$



This proves the first identity in (1.3).

## 5. Fraction-free endpoint factorization

Rewrite (1.1) without dividing by any endpoint quantity:



$$
\begin{aligned}
K_h
 &=2d_h(\eta_hU_h+L_h)-L_h(F_h-d_h)\\
 &=c_h\bigl(2d_hY_h-L_hX_h\bigr).
\end{aligned}                                      \tag{5.1}
$$



Thus (1.4) is a division-free consequence of the two telescopings.  In
particular, the proof never divides by $c_h,L_h,U_h,d_h$, or a reduced
numerator.  This is the requested fraction-free localized identity.

## 6. Complete denominator and unit audit

All localization claims are now checked explicitly.

First,



$$
t_j=(-1)^j\frac{(2s)_j}{j!}
 =(-1)^j\frac{\prod_{e=0}^{j-1}(3e-4h-3)}{3^j j!}. \tag{6.1}
$$



For $0\leq j\leq2h-1$, every prime in the denominator of (6.1) is at
most $\max(3,2h-1)\leq4h+3$.  Hence $X_h\in\mathscr A_h$.  Next,



$$
\mu_k=(-1)^k3^k
 \frac{\prod_{e=0}^{k-1}(2e-4h-1)}
      {\prod_{e=0}^{k-1}(6e-4h+9)}.                \tag{6.2}
$$



For $0\leq e\leq h-1$, the denominator factors in (6.2) are nonzero:
the left side of $6e=4h-9$ is even and the right side is odd.  Moreover,



$$
|6e-4h+9|\leq\max(|9-4h|,2h+3)\leq4h+3.          \tag{6.3}
$$



Thus $Y_h\in\mathscr A_h$.  Notice that the individual ratio
$\eta_h=\mu_{h+1}$ need not lie in $\mathscr A_h$ for the first small
values of $h$.  Identity (3.9) is exactly the cancellation that proves
the product combination $\eta_hU_h+L_h$ is localized; no unsupported
claim about $\eta_h$ alone is used.

The coefficients of $P^-$ and $P^+$ have denominators dividing a
product of $(2h)!$ and powers of $2$ and $3$.  Solving (2.5) from
the highest power of $j$ downward divides only by the leading
coefficient $-2$ of $\mathcal L_s(j^m)$.  Hence



$$
c_h\in\mathscr A_h,\qquad R^\pm(j)\in\mathscr A_h[j].        \tag{6.4}
$$



The endpoint arguments $a,b$ have denominator $6$.  Equations
(3.8), (4.1)--(4.3), and (6.1) therefore give



$$
L_h,d_h\in\mathscr A_h.                            \tag{6.5}
$$



Equations (1.4), (6.4), and (6.5) now give



$$
Z_h,K_h\in\mathscr A_h.                            \tag{6.6}
$$



For completeness, Item 222's integer clearing is



$$
E_h^*=\frac{A_h}{2(4h+3)D_xD_yD_uD_v},             \tag{6.7}
$$



where



$$
\begin{aligned}
D_x&=3^h\prod_{i=0}^{h-1}(2i+1-4h),\\
D_y&=\prod_{i=0}^{h-1}(3i+3-h),\\
D_u&=3^{h+2}\prod_{i=0}^{h+1}(2i-4h-3),\\
D_v&=\prod_{i=0}^{h}(3i-h).
\end{aligned}                                      \tag{6.8}
$$



When $3\nmid h$, none of the factors in (6.8) is zero, and every one
has absolute value at most $4h+3$.  Thus $E_h^*\in\mathscr A_h$.

Finally, Item 243's gauge starts with



$$
\mathcal G_1=-\frac{49}{18},\qquad
 \mathcal G_2=\frac{4235}{1944},                   \tag{6.9}
$$



and advances, within each nonzero residue class modulo $3$, by



$$
\frac{\mathcal G_{a+3}}{\mathcal G_a}=
\frac{a(4a+1)(4a+5)(4a+7)(4a+9)(4a+11)(4a+15)^2}
{864(a+1)(a+2)(2a+1)^2(2a+3)(2a+5)^2(4a+3)}.       \tag{6.10}
$$



For every step $a\leq h-3$, each displayed nonzero linear factor is at
most $4h+3$; the remaining constants have only prime factors at most
$4h+3$.  The same is true of the prime factors in the two bases (6.9).
Explicitly, $49=7^2$, $18=2\cdot3^2$,
$4235=5\cdot7\cdot11^2$, $1944=2^3\cdot3^5$, and
$864=2^5\cdot3^3$.
Therefore both the numerator and denominator of $\mathcal G_h$ are
units in $\mathscr A_h$, proving (1.6) with
$\mathcal G_h\in\mathscr A_h^\times$.

Now let $q>4h+3$ be prime.  Reduction
$\mathscr A_h\to\mathbb F_q$ is defined.  A reduced rational in
$\mathscr A_h$ vanishes under this map exactly when $q$ divides its
reduced numerator.  If $q\mid N_E(h)$, equations (1.6) and (1.4) give



$$
E_h^*=0\ \Longrightarrow\ c_h=0\ \Longrightarrow\ K_h=0
 \qquad\text{in }\mathbb F_q,                     \tag{6.11}
$$



which proves (1.7).

## 7. Actual-family and capacity consequences

An actual row has



$$
p=4h+6s_0+3,\qquad h,s_0\geq1.                   \tag{7.1}
$$



If $p$ is prime, then $p>3$ and $p\equiv h\pmod3$, so
$3\nmid h$.  Also $p\geq4h+9>4h+3$.  Hence every actual prime falls
under (1.7).

This settles Item 280's redundancy question in the large-moving-prime
range: $K_h$ merely rephrases a consequence of $E_h^*$ and supplies
no second arithmetic codimension there.  The theorem does not prove
$E_h^*\ne0\pmod p$, does not bound how often $p\mid N_E(h)$, and does
not produce a weighted prime-log-mass saving.  The small-prime support in
(1.8) is an exact support statement, but those primes cannot equal the
actual row prime for the same $h$; no separate weighted summation claim
is made from it.

Accordingly,



$$
\boxed{\text{new linear log rate}=0,\quad
        \text{new divisibility exponent}=0,\quad
        \text{capacity booked}=0.}                 \tag{7.2}
$$



Route 1 and every conclusion about $e+\pi$ remain open.

## 8. Reproducibility and strict labels

From the archive root, run

```text
python scripts/item288_j1_large_prime_redundancy_certificate.py --output results/item288_j1_large_prime_redundancy_certificate.replay.json
```

The checker uses Python standard-library exact integer and `Fraction`
arithmetic.  It pins Items 222, 229, 231, 236, and 243; verifies the formal
$D_n$-recurrence combination and the division-free endpoint
factorization; and replays (1.3)--(1.6) exactly through $h\leq12$.  The
bounded replay is a check of identities proved above, not an extrapolation.

- **PROVED:** the reflected antidifference (2.8), both telescopings (1.3),
  the localized factorization (1.4), the complete unit audit, the
  large-prime implication (1.7), and redundancy on every actual row.
- **OPEN:** nonvanishing or sparsity of $E_h^*\pmod p$, any weighted
  prime-log-mass saving, Route 1, and any conclusion about $e+\pi$.
- **NOT CLAIMED:** the converse $q\mid N_K(h)\Rightarrow q\mid N_E(h)$,
  or any density inference from a bounded computation.
