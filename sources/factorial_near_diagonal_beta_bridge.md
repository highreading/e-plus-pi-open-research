> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Near-diagonal factorial digits: centered residuals and the beta bridge

Date: 2026-08-28

## 1. Status and theorem boundary

This note treats the regime $b/a\to1$ left open by the archived
cross-order factorial support theorem.  Its principal exact identity is



$$
\boxed{D_{n,n}=q_n,}
$$



where $q_n$ is the denominator in the archive's diagonal Padé
approximation to $e$.  The corresponding $e$-numerator is $n!p_n$.
Consequently, the diagonal factorial-digit form is an exact match between
the archived beta pair $(p_n,q_n)$ and one integral finite difference
formed from the factorial floors of $\pi$.

The note proves:

1. an exact centered residual $T_{a,b}$, including the complete-collapse
   branch and an exact same-base repeat determinant;
2. the identities $D_{n,n}=q_n$ and
   $\Delta^n\lfloor m!e\rfloor|_{m=n}=n!p_n$;
3. a numerator-free Bezout formula for the diagonal selected content;
4. an all-ray harmonic-support inequality that remains nontrivial at
   $b/a\to1$;
5. a short-block support alternative with explicit constants and an exact
   statement of the primitive-pair deduplication caveat.

None of these statements proves that $e+\pi$ is irrational or
transcendental.  The surviving issues are main-scale matched content,
residual factorial content, quantitative distinctness of primitive points,
and highly lacunary bases.

Sections 2--10 are symbolic theorems.  Section 11 is a logically separate
finite replay through $n=265$ and is not used in any proof.

## 2. Archived factorial family and notation

Put



$$
\alpha=e+\pi,\qquad
 C_n=\lfloor n!e\rfloor+\lfloor n!\pi\rfloor,\qquad
 x_n=n!\alpha-C_n.
$$



For integers $a\ge1$ and $1\le b\le a+1$, write



$$
\Delta^b f_a=\sum_{r=0}^b(-1)^{b-r}\binom br f_{a+r}.
$$



The archive proves



$$
\begin{aligned}
 W_{a,b}&=\Delta^b(a!)=a!D_{a,b},\\
 Z_{a,b}&=\Delta^b C_a=D_{a,b}C_a+K_{a,b},\\
 X_{a,b}&=\Delta^b x_a=D_{a,b}x_a-K_{a,b}.
 \end{aligned}                                      \tag{2.1}
$$



If $c_n=d_n(\pi)+1$, then $1\le c_n\le n$ and



$$
K_{a,b}=\sum_{j=1}^b E_{a,b,j}c_{a+j},
 \qquad E_{a,b,j}>0.                                 \tag{2.2}
$$



Define



$$
g_{a,b}=\gcd(D_{a,b},K_{a,b}),\qquad
 \bar D_{a,b}=D_{a,b}/g_{a,b}.                       \tag{2.3}
$$



The remaining factorial content after division by $g_{a,b}$ will be
denoted $J_{a,b}$.

## 3. Exact centering and the collapse branch

### Theorem 3.1 (centered residual)

Define



$$
\boxed{T_{a,b}=K_{a,b}-D_{a,b}.}                    \tag{3.1}
$$



Then



$$
\boxed{
 T_{a,b}
 =\sum_{j=1}^bE_{a,b,j}
   \bigl(c_{a+j}-(a+j-1)\bigr),}                     \tag{3.2}
$$





$$
\boxed{
 Z_{a,b}=D_{a,b}(C_a+1)+T_{a,b},\qquad
 X_{a,b}=D_{a,b}(x_a-1)-T_{a,b},}                   \tag{3.3}
$$



and



$$
\boxed{g_{a,b}=\gcd(D_{a,b},T_{a,b}).}              \tag{3.4}
$$



If



$$
S_{a,b}=\sum_{j=1}^bE_{a,b,j},                     \tag{3.5}
$$



then



$$
\frac{D_{a,b}}{a+b-1}\le S_{a,b}\le\frac{D_{a,b}}a, \tag{3.6}
$$





$$
S_{a,b}\le K_{a,b}\le D_{a,b}+S_{a,b},\qquad
 S_{a,b}-D_{a,b}\le T_{a,b}\le S_{a,b}.             \tag{3.7}
$$



#### Proof

The reference future block



$$
c_{a+j}=a+j-1\qquad(1\le j\le b)                   \tag{3.8}
$$



is admissible.  In the recurrence $x_n=nx_{n-1}-c_n$, the initial value
$x_a=1$ and (3.8) produce
$x_a=x_{a+1}=\cdots=x_{a+b}=1$.  Its $b$-th difference is zero.
Applying the algebraic identity (2.1), which is valid for every admissible
digit block, gives



$$
\boxed{
 \sum_{j=1}^b(a+j-1)E_{a,b,j}=D_{a,b}.}              \tag{3.9}
$$



Subtracting (3.9) from (2.2) proves (3.2).  Equations (3.3)--(3.4)
follow from (2.1).  Every coefficient in (3.9) is between $a$ and
$a+b-1$, which proves (3.6).  Finally,
$1\le c_{a+j}\le a+j$ in (2.2) gives (3.7).
$\square$

### Corollary 3.2 (primitive coordinates)

Put



$$
\bar T_{a,b}=T_{a,b}/g_{a,b},
$$





$$
J_{a,b}
 =\gcd\!\left(
   a!,\,\bar D_{a,b}(C_a+1)+\bar T_{a,b}
 \right).                                           \tag{3.10}
$$



The primitive pair is



$$
\boxed{
 P_{a,b}
 =\frac{\bar D_{a,b}(C_a+1)+\bar T_{a,b}}{J_{a,b}},
 \qquad
 Q_{a,b}
 =\frac{a!\bar D_{a,b}}{J_{a,b}},}                  \tag{3.11}
$$



and



$$
\boxed{\gcd(J_{a,b},\bar D_{a,b})=1.}               \tag{3.12}
$$



Moreover,



$$
\boxed{
 T_{a,b}=0
 \iff
 \frac{Z_{a,b}}{W_{a,b}}=\frac{C_a+1}{a!}.}          \tag{3.13}
$$



On this branch $g_{a,b}=D_{a,b}$, and the high-order form reduces
exactly to the primitive reduction of $(C_a+1)/a!$.  Away from it,



$$
T_{a,b}>0\Longrightarrow\bar D_{a,b}\ge a,          \tag{3.14}
$$





$$
T_{a,b}<0\Longrightarrow\bar D_{a,b}\ge2.           \tag{3.15}
$$



#### Proof

Divide (3.3) by $g_{a,b}$.  Since
$\gcd(\bar D_{a,b},\bar T_{a,b})=1$, any common divisor of
$J_{a,b}$ and $\bar D_{a,b}$ would divide $\bar T_{a,b}$;
this proves (3.12).  Equation (3.13) is immediate after division by
$a!D_{a,b}$.

If $T_{a,b}>0$, then
$g_{a,b}\le T_{a,b}\le S_{a,b}\le D_{a,b}/a$.
If $T_{a,b}<0$, (3.7) gives
$-D_{a,b}<T_{a,b}<0$, so $g_{a,b}$ is a proper divisor of
$D_{a,b}$.  This proves (3.14)--(3.15). $\square$

The reference block (3.8) realizes $T_{a,b}=0$ for every admissible
$(a,b)$.  Therefore digit ranges alone cannot prove that any part of
$D_{a,b}$ survives.  This is an adversarial range statement, not a
claim about the actual digits of $\pi$.

## 4. Same-base determinant and exact repeats

Fix $a$, and take positive orders $b,c$.  Use the barred quantities
and $J$'s from Corollary 3.2.

### Theorem 4.1



$$
\boxed{
 P_{a,b}Q_{a,c}-P_{a,c}Q_{a,b}
 =
 \frac{a!
  \bigl(
   \bar T_{a,b}\bar D_{a,c}
   -\bar T_{a,c}\bar D_{a,b}
  \bigr)}
 {J_{a,b}J_{a,c}}.}                                  \tag{4.1}
$$



Thus the two primitive points repeat if and only if



$$
\boxed{
 \frac{\bar T_{a,b}}{\bar D_{a,b}}
 =
 \frac{\bar T_{a,c}}{\bar D_{a,c}}.}                 \tag{4.2}
$$



Also,



$$
\left|
 \frac{T_{a,b}}{D_{a,b}}-(x_a-1)
 \right|
 =\frac{|X_{a,b}|}{D_{a,b}},                         \tag{4.3}
$$



and hence



$$
\left|
 T_{a,b}D_{a,c}-T_{a,c}D_{a,b}
 \right|
 \le
 D_{a,c}|X_{a,b}|+D_{a,b}|X_{a,c}|.                 \tag{4.4}
$$



#### Proof

Substitute (3.11).  The two terms containing $C_a+1$ cancel, leaving
(4.1).  The remaining claims follow from (3.3). $\square$

Equation (4.2) classifies repetition exactly, but does not bound the
selected gcd when $T_{a,b}<0$: that gcd can still have the logarithmic
scale of $D_{a,b}$.

## 5. Exact diagonal beta identification

Define the archived beta/Padé coefficients



$$
q_n
 =\sum_{k=0}^n(-1)^k
   \frac{(2n-k)!}{k!(n-k)!},
\qquad
 p_n
 =\sum_{k=0}^n
   \frac{(2n-k)!}{k!(n-k)!}.                         \tag{5.1}
$$



They satisfy



$$
q_0=q_1=1,\qquad p_0=1,\quad p_1=3,
$$





$$
Y_n=(4n-2)Y_{n-1}+Y_{n-2}\qquad(n\ge2).             \tag{5.2}
$$



### Theorem 5.1 (beta bridge)

For every $n\ge0$,



$$
\boxed{D_{n,n}=q_n.}                                \tag{5.3}
$$



For $n\ge1$, if $A_m=\lfloor m!e\rfloor$, then



$$
\boxed{\Delta^n A_n=n!p_n.}                         \tag{5.4}
$$



Consequently,



$$
\boxed{W_{n,n}=n!q_n.}                              \tag{5.5}
$$



#### Proof

Changing variables $k=n-r$ in the defining finite difference gives



$$
\begin{aligned}
 D_{n,n}
 &=\sum_{r=0}^n(-1)^{n-r}\binom nr\frac{(n+r)!}{n!}\\
 &=\sum_{k=0}^n(-1)^k
   \frac{(2n-k)!}{k!(n-k)!}
 =q_n.
 \end{aligned}
$$



For the numerator identity, put $x_m^{(e)}=m!e-A_m$.  Taylor's
integral remainder gives



$$
x_m^{(e)}
 =\int_0^1e^t(1-t)^m\,dt.                            \tag{5.6}
$$



Taking the $n$-th difference at $m=n$ gives



$$
\Delta^n x_n^{(e)}
 =(-1)^n\int_0^1e^t t^n(1-t)^n\,dt.                 \tag{5.7}
$$



The diagonal Padé identity is



$$
q_ne-p_n
 =\frac{(-1)^n}{n!}
  \int_0^1e^t t^n(1-t)^n\,dt.                       \tag{5.8}
$$



On the other hand,



$$
\Delta^n x_n^{(e)}
 =W_{n,n}e-\Delta^nA_n
 =n!(q_ne-p_n).
$$



Using (5.3) and cancelling $n!q_ne$ proves (5.4). $\square$

For completeness, the whole fixed-offset diagonal has the exponential
generating function below.  For fixed $h\ge0$, let
$d_n^{(h)}=D_{n+h,n}$, and put



$$
w=w(t)=\frac{1-\sqrt{1-4t}}2.
$$



Then



$$
\boxed{
 \sum_{n\ge0}d_n^{(h)}\frac{t^n}{n!}
 =\frac{e^{-w}(1-w)^{-h}}{1-2w}.}                    \tag{5.9}
$$



Indeed,



$$
\frac{D_{a,b}}{b!}
 =[z^b]e^{-z}(1-z)^{-a-1}.                           \tag{5.10}
$$



Apply the formal diagonal lemma



$$
\sum_{n\ge0}t^n[z^n]f(z)\phi(z)^n
 =\frac{f(w)}{1-t\phi'(w)},\qquad w=t\phi(w),        \tag{5.11}
$$



with $f(z)=e^{-z}(1-z)^{-h-1}$ and
$\phi(z)=(1-z)^{-1}$.  At $h=0$, the resulting generating
function $Y$ obeys



$$
(1-4t)Y''-6Y'-Y=0,                                  \tag{5.12}
$$



which recovers (5.2) for $q_n=D_{n,n}$.

## 6. Diagonal content: an exact beta--$\pi$ match

Define the integral $\pi$-floor difference



$$
R_n
 =\left.
   \Delta^n\lfloor m!\pi\rfloor
  \right|_{m=n}.                                     \tag{6.1}
$$



Theorem 5.1 gives



$$
\boxed{
 Z_{n,n}=n!p_n+R_n,\qquad W_{n,n}=n!q_n.}            \tag{6.2}
$$



Thus the raw target form is exactly



$$
n!(q_ne-p_n)+\bigl(n!q_n\pi-R_n\bigr).             \tag{6.3}
$$



Put $T_n=T_{n,n}$, $g_n=g_{n,n}$, and $J_n=J_{n,n}$.
Equations (2.1), (3.1), and (6.2) give the direct formulas



$$
\boxed{
 K_{n,n}=n!p_n+R_n-q_nC_n,\qquad
 T_n=n!p_n+R_n-q_n(C_n+1).}                         \tag{6.4}
$$



Consequently,



$$
\boxed{
 g_n
 =\gcd(q_n,T_n)
 =\gcd(q_n,n!p_n+R_n).}                              \tag{6.5}
$$



Equivalently, since $K_{n,n}=T_n+q_n$,



$$
g_n=\gcd(q_n,K_{n,n}).                              \tag{6.6}
$$



The final primitive coordinates are



$$
\boxed{
 \begin{aligned}
 J_n
 &=\gcd\!\left(
   n!,\,\frac{n!p_n+R_n}{g_n}
  \right),\\
 P_n^{\rm diag}
 &=\frac{n!p_n+R_n}{g_nJ_n},\\
 Q_n^{\rm diag}
 &=\frac{n!q_n}{g_nJ_n}
 =\frac{q_n}{g_n}\frac{n!}{J_n}.
 \end{aligned}}                                     \tag{6.7}
$$



Moreover,



$$
\boxed{
 \gcd\!\left(J_n,\frac{q_n}{g_n}\right)=1.}          \tag{6.8}
$$



### Theorem 6.1 (numerator-free Bezout identity)

The beta Wronskian is



$$
p_nq_{n-1}-p_{n-1}q_n=2(-1)^{n+1}.                 \tag{6.9}
$$



It follows that



$$
\boxed{
 g_n
 =\gcd\!\left(
   q_n,\,
   q_{n-1}R_n+2(-1)^{n+1}n!
  \right).}                                         \tag{6.10}
$$



#### Proof

For $n\ge1$, the recurrence (5.2) has determinant $-1$, which proves
(6.9) from
the initial values.  Consecutive $q$'s are coprime.  Therefore
multiplication by $q_{n-1}$ is invertible modulo $q_n$, and



$$
q_{n-1}(n!p_n+R_n)
 \equiv
 2(-1)^{n+1}n!+q_{n-1}R_n
 \pmod{q_n}.
$$



Apply (6.5). $\square$

This is the direct identity for $K/g/J$ supplied by
$D_{n,n}=q_n$: it removes $p_n$ from the selected gcd, but it does
not remove the dependence on the actual integral $\pi$-floor difference
$R_n$.

### Proposition 6.2 (prime-power cancellation and amplification)

Let $\ell^a\Vert q_n$, and put $t=v_\ell(n!)$.  Then



$$
v_\ell(g_n)
 =\min\{a,v_\ell(n!p_n+R_n)\}.                       \tag{6.11}
$$



The full $\ell^a$-part of $q_n$ is removed if and only if



$$
R_n\equiv-n!p_n\pmod{\ell^a}.                      \tag{6.12}
$$



All $q_n$ are odd, and (6.9) gives $\gcd(p_n,q_n)=1$.  Hence:

1. if $a\le t$, (6.12) is exactly
   $R_n\equiv0\pmod{\ell^a}$;
2. if $a>t$, the required residue in (6.12) has exact
   $\ell$-adic valuation $t$;
3. in particular, if $\ell>n$, the required residue is a nonzero
   unit modulo $\ell^a$.

If instead $\ell\mid q_n/g_n$, then (6.8) forces
$v_\ell(J_n)=0$, and



$$
\boxed{
 v_\ell(Q_n^{\rm diag})
 =v_\ell(q_n/g_n)+v_\ell(n!).}                       \tag{6.13}
$$



Thus every surviving beta prime brings its complete residual beta exponent
and, when $\ell\le n$, the entire factorial exponent into the final
denominator.

For a fixed finite prime set $\mathcal S$, (6.7)--(6.8) give the exact
support equivalence



$$
\boxed{
 Q_n^{\rm diag}\text{ is an }\mathcal S\text{-unit}
 \iff
 \begin{cases}
  (q_n)_{\mathcal S^c}\mid g_n,\\
  (n!)_{\mathcal S^c}\mid J_n.
 \end{cases}}                                       \tag{6.14}
$$



Neither line has been proved for infinitely many actual $\pi$-digit
blocks.

## 7. Harmonic-support law valid on the diagonal

For $Q>0$, define



$$
\boxed{
 \mathcal A(Q)
 =\sum_{p\mid Q}\frac{\log p}{p-1}.}                 \tag{7.1}
$$



This is a sum over distinct prime divisors.

### Theorem 7.1 (local-content refinement)

Let $(a_j,b_j)$ be an infinite sequence satisfying



$$
a_j\longrightarrow\infty,\qquad
 \frac{b_j}{a_j}\longrightarrow\lambda\in[0,1].      \tag{7.2}
$$



Let $(P_{a_j,b_j},Q_{a_j,b_j})$ be the coprime pair in (3.11), with
$Q_{a_j,b_j}>0$.  Assume exactly that



$$
\boxed{
 X_{a_j,b_j}\ne0,\qquad
 Q_{a_j,b_j}\longrightarrow\infty.}                 \tag{7.3}
$$



The second hypothesis automatically provides infinitely many distinct
primitive points; no separate distinctness assumption is needed here.
Put



$$
\rho_j
 =\frac{\log g_{a_j,b_j}}{a_j\log a_j}.              \tag{7.4}
$$



If $\alpha=e+\pi$ is algebraic irrational, then



$$
\boxed{
 \liminf_{j\to\infty}
 \left(
  \frac{\mathcal A(Q_{a_j,b_j})}{\log a_j}-\rho_j
 \right)
 \ge\frac{1-\lambda}{2}.}                            \tag{7.5}
$$



Consequently, if for some fixed $\varepsilon>0$,



$$
\mathcal A(Q_{a_j,b_j})
 \le
 \left(
  \frac{1-\lambda}{2}+\rho_j-\varepsilon
 \right)\log a_j                                    \tag{7.6}
$$



holds infinitely often under (7.2)--(7.3), then $e+\pi$ is
transcendental.

#### Proof

Set $F_{a,b}=a!/J_{a,b}$.  Formula (3.11) gives



$$
Q_{a,b}=\bar D_{a,b}F_{a,b},\qquad F_{a,b}\mid Q_{a,b}.
$$



Legendre's formula therefore yields



$$
\log F_{a,b}
 \le a\mathcal A(Q_{a,b}),
$$



and hence the exact refined height bound



$$
\boxed{
 \log Q_{a,b}
 \le
 a\mathcal A(Q_{a,b})
 +\log D_{a,b}-\log g_{a,b}.}                        \tag{7.7}
$$



For every fixed $\eta>0$, Roth's theorem and the archived digit bound
$|X_{a,b}|\le2^{b+1}$ give eventually



$$
\begin{aligned}
 Q_{a,b}^{-2-\eta}
 &\le
 \left|\alpha-\frac{P_{a,b}}{Q_{a,b}}\right|\\
 &=\frac{|X_{a,b}|}{W_{a,b}}
 \le\frac{2^{b+1}}{W_{a,b}}.
 \end{aligned}
$$



Thus



$$
(2+\eta)\log Q_{a,b}
 \ge\log W_{a,b}-(b+1)\log2.                         \tag{7.8}
$$



Along (7.2), the archived factorial asymptotics are



$$
\frac{\log W_{a,b}}{a\log a}\longrightarrow1+\lambda,
\qquad
 \frac{\log D_{a,b}}{a\log a}\longrightarrow\lambda,
\qquad
 \frac{b}{a\log a}\longrightarrow0.                 \tag{7.9}
$$



Insert (7.7) into (7.8), divide by $a\log a$, take the lower
limit, and let $\eta\downarrow0$.  This proves (7.5).

If $\alpha$ were rational, then $x_n=1$ for all sufficiently large
$n$, so every positive-order error with sufficiently large base would
vanish.  This contradicts (7.3).  Hence (7.6) excludes both the rational
and algebraic-irrational alternatives. $\square$

On the exact diagonal, $\lambda=1$ and $D_{n,n}=q_n$.  Therefore
(7.5) becomes



$$
\boxed{
 \liminf_{n\to\infty}
 \left(
  \frac{\mathcal A(Q_n^{\rm diag})}{\log n}
  -\frac{\log g_n}{n\log n}
 \right)\ge0}                                       \tag{7.10}
$$



along every subsequence satisfying the exact nonzero and unbounded-height
hypotheses (7.3).  Thus main-scale cancellation in $g_n$ is not free
under algebraicity: it must reappear as harmonic support in the final
denominator.

For example, if along such a subsequence



$$
\frac{\log g_n}{n\log n}\longrightarrow\rho>0,
$$



then algebraicity forces



$$
\boxed{
 \omega(Q_n^{\rm diag})\ge n^{\rho-o(1)}.}           \tag{7.11}
$$



Indeed, among sets of $s$ primes, $\mathcal A$ is maximized by the
first $s$ primes; Mertens' and the prime-number estimates give
$\max\mathcal A=(1+o(1))\log s$.

## 8. Diagonal short-block support dispersion

Set



$$
r_n=\frac{q_n}{g_n}.                                \tag{8.1}
$$



By (6.7), $r_n\mid Q_n^{\rm diag}$.  The archived continuant theorem
states that for $d\ge1$,



$$
\gcd(q_n,q_{n+d})
 =\gcd(q_n,\mathcal P_d(n)),                         \tag{8.2}
$$



where



$$
0<\mathcal P_d(n)\le\{4(n+d)\}^{d-1}.              \tag{8.3}
$$



Consequently,



$$
\boxed{
 \gcd(r_n,r_{n+d})
 \le\{4(n+d)\}^{d-1}.}                               \tag{8.4}
$$



### Theorem 8.1 (short-block support alternative)

Let $N\ge1$ and $L\ge2$ be integers.  Let



$$
\mathcal I\subseteq[N,N+L]\cap\mathbb Z
$$



be a set of $M\ge2$ distinct diagonal indices, and suppose



$$
R=\min_{n\in\mathcal I}r_n>1.                       \tag{8.5}
$$



Let



$$
s=\omega\!\left(
    \prod_{n\in\mathcal I}Q_n^{\rm diag}
   \right).                                         \tag{8.6}
$$



Then either



$$
s\ge M,                                             \tag{8.7}
$$



or



$$
\boxed{
 s\ge
 \frac{\log R}
 {(L-1)\log(4(N+L))}.}                               \tag{8.8}
$$



Equivalently,



$$
\boxed{
 s\ge
 \min\!\left\{
  M,\,
  \frac{\log R}{(L-1)\log(4(N+L))}
 \right\}.}                                         \tag{8.9}
$$



#### Proof

Since $R>1$, one has $s\ge1$.  Factor each $r_n$ into its
prime-power components.  All components use at most the $s$ denominator
primes in (8.6).  Since their product is $r_n\ge R$, at least one
component is at least $R^{1/s}$.  Select such a component for every
$n\in\mathcal I$.

If $M>s$, two distinct indices select the same prime.  The smaller of
the two selected powers divides their gcd, which is at least $R^{1/s}$.
Their gap is at most $L$, so (8.4) bounds the same gcd by



$$
B=\{4(N+L)\}^{L-1}.
$$



Thus $R^{1/s}\le B$, which is (8.8). $\square$

The recurrence (5.2) also gives the elementary bound



$$
q_n\ge n^n\qquad(n\ge1).                            \tag{8.10}
$$



Indeed, for $n\ge2$,
$(n/(n-1))^{n-1}<e<3$ and $4n-2\ge3n$, so
$(4n-2)(n-1)^{n-1}>n^n$, completing the induction.

### Corollary 8.2 (polynomial short blocks)

Fix $0<\theta<1$, and put $L_N=\lfloor N^\theta\rfloor$.
Assume uniformly that



$$
\max_{N\le n\le N+L_N}\log g_n=o(N\log N).          \tag{8.11}
$$



For every set
$\mathcal I_N\subseteq[N,N+L_N]$ of $M_N\ge2$ indices, let
$s_N$ be the support size in (8.6).  Then



$$
\boxed{
 s_N\ge
 \min\{M_N,N^{1-\theta-o(1)}\}.}                     \tag{8.12}
$$



#### Proof

Equations (8.10)--(8.11) give



$$
\log r_n\ge(1-o(1))N\log N
$$



uniformly in the block.  Therefore



$$
\frac{\log R}
 {(L_N-1)\log(4(N+L_N))}
 =N^{1-\theta-o(1)}.
$$



Apply (8.9). $\square$

For the full indexed block, $M_N=L_N+1$, so



$$
\boxed{
 s_N\ge
 N^{\min\{\theta,1-\theta\}-o(1)}.}                  \tag{8.13}
$$



More generally, a deduplicated set of at least $N^\mu$ distinct
primitive pairs in the block has



$$
s_N\ge N^{\min\{\mu,1-\theta\}-o(1)}.               \tag{8.14}
$$



### Exact deduplication caveat

Theorem 8.1 counts distinct indices and remains valid even if two of those
indices reduce to the same primitive pair.  A Subspace-Theorem block must,
however, be deduplicated: let $M_N^{\rm dist}$ be the number of distinct
primitive pairs, and keep one representative of each.

Deduplication does not change the union of denominator primes, because
repeated primitive pairs have the same $Q$.  For the full block,
$M_N^{\rm dist}\le L_N+1$, while the unchanged denominator-support union
still satisfies (8.13).  If $\mathcal S_N$ is the full set of numerator
and denominator primes used by the archived criterion and
$\sigma_N=1+|\mathcal S_N|$, then $\sigma_N\ge1+s_N$.  Hence the
archived moving-support hypothesis



$$
\sigma_N^6\log(\sigma_N+2)
 =o(\log M_N^{\rm dist})                             \tag{8.15}
$$



is impossible for these full blocks.  Indeed,
$\log M_N^{\rm dist}\le\theta\log N+O(1)$, whereas (8.13) makes
the left side a positive power of $N$.  If
$M_N^{\rm dist}$ does not tend to infinity, the family is not a
moving block in the first place.

For an arbitrary selected subblock rather than the full interval, (8.12)
is the relevant result.  Producing polynomially many distinct primitive
points is a separate prerequisite.  Irrationality would imply infinitely
many distinct diagonal points globally, but supplies no polynomial local
count.

Hypothesis (8.11) is not proved.  A chosen block may also contain
exceptional small cofactors $r_n$; if polynomially many indices with
sub-main-scale $g_n$ remain, one applies Corollary 8.2 to that good
subset.  Thus the precise local escape is main-scale matched cancellation
at all but too few usable points.  For highly lacunary indices, the gap
$d$ makes (8.3) too large to be useful, so lacunarity remains a separate
survivor.

## 9. Collapse, repetition, and height

The raw diagonal approximation satisfies



$$
\left|
 \alpha-\frac{Z_{n,n}}{W_{n,n}}
 \right|
 =\frac{|X_{n,n}|}{n!q_n}
 \le\frac{2^{n+1}}{n!q_n}
 \longrightarrow0.                                  \tag{9.1}
$$



Therefore:

1. If $\alpha$ is irrational, then
   $Q_n^{\rm diag}\to\infty$.  Otherwise a bounded-denominator
   subsequence of the convergent primitive rationals would contain a
   constant subsequence, forcing a rational limit.  In particular,
   infinitely many distinct diagonal primitive points occur.
2. If $\alpha=A/D$ is rational, then $n!\alpha$ is integral for all
   sufficiently large $n$, while
   

$$
x_n=\{n!e\}+\{n!\pi\}\in(0,2)\cap\mathbb Z=\{1\}.
$$


   Hence every sufficiently large positive-order difference has zero
   error.  Every large diagonal point equals $\alpha$, and its primitive
   pair repeats forever.

Thus eventual diagonal collapse is exactly what the rational alternative
predicts.  Proving noncollapse for the target is not a shortcut: a single
zero form already implies $\alpha=Z/W\in\mathbb Q$.  At one fixed base,
Theorem 4.1 supplies the sharper exact repeat test (4.2), but no theorem
here excludes equal slopes for the actual digits.

## 10. Why digit ranges cannot close the content problem

The admissible future block (3.8) forces $T_{a,b}=0$ and
$g_{a,b}=D_{a,b}$.  Independently, the past factorial digits can make
$C_a$ assume any residue modulo $a!$: replace $\pi$ by an
arbitrary $y\in[3,4)$, choose $\lfloor a!y\rfloor$, and extend by
any admissible future block.

Consequently one may force $J_{a,b}$ to contain any prescribed divisor
of $a!$ coprime to $\bar D_{a,b}$.  On $T_{a,b}=0$, for example,
one can arrange $J_{a,b}=a!$ and $Q_{a,b}=1$, or arrange
$a!/J_{a,b}$ to be a power of $2$.

This adversarial construction does not describe $\pi$.  It proves that
both cancellations in (6.14) require arithmetic information about the
actual factorial digits, not only their canonical ranges.

## 11. Frozen finite replay, $1\le n\le265$

Nothing in this section is used in Sections 2--10.

The companion replay program

    scripts/factorial_near_diagonal_beta_bridge_diagnostic.py

uses the archive's certified rational Machin interval only to construct the
factorial floors of $\pi$.  It then checks integer identities:

- (3.2)--(3.4), including the centered weights and digit residual;
- (5.2)--(5.5), including the beta recurrence and Wronskian;
- (6.2)--(6.13), including both gcd representations, the full endpoint
  content, and the primitive denominator split;
- exact deduplication of all primitive pairs in the finite range.

For the certified prefix $1\le n\le265$, it finds:

- $T_n<0$ at 258 indices;
- $T_n>0$ exactly at
  $n=3,5,6,34,163,229$;
- $T_n=0$ only at $n=1$;
- $g_n>1$ exactly at
  

$$
n=4,9,11,18,28,37,53,60,114,130,151,212,228,
   235,247,263;
$$


- the largest observed $\log g_n/\log q_n$ is
  $0.3470806750\ldots$, at $n=4$;
- no repeated primitive diagonal pair.

From the archive root, the frozen replay command is

    python scripts/factorial_near_diagonal_beta_bridge_diagnostic.py --max-n 265

It writes

    results/factorial_near_diagonal_beta_bridge_m265.json

with sorted keys, no timestamp, and no absolute path.  The JSON records the
SHA-256 hashes of this note, the replay script, and the inherited Machin
certificate dependency.  The noncircular package manifest is

    results/factorial_near_diagonal_beta_bridge_hashes.sha256

The finite scan does not prove $g_n=q_n^{o(1)}$, noncollapse,
short-block distinctness, support dispersion for all degrees,
irrationality, or transcendence.

## 12. Provenance and deterministic dependencies

The symbolic inputs used from the frozen archive are:

    sources/factorial_digit_entire_varying_b_regimes.md
    sources/factorial_cross_order_support_dispersion.md
    sources/bessel_denominator_high_tail_gap_singleton_barrier.md
    sources/bessel_rational_first_integral_darboux_exclusion.md

The finite replay imports:

    scripts/factorial_digit_entire_varying_b_probe.py

The new deductions in this note are the centered identity, the diagonal beta
bridge, the numerator-free formula (6.10), the prime-power amplification
(6.13), the local-content harmonic law (7.5), and the diagonal block
alternative (8.9).

## 13. Exact remaining gap

The selected local content is now either of the equal quantities



$$
\boxed{
 \gcd(q_n,n!p_n+R_n)
 =
 \gcd\!\left(
  q_n,\,
  q_{n-1}R_n+2(-1)^{n+1}n!
 \right).}                                          \tag{13.1}
$$



The residual factorial content is



$$
\boxed{
 \gcd\!\left(
  n!,\,\frac{n!p_n+R_n}{g_n}
 \right).}                                          \tag{13.2}
$$



If (13.1) is uniformly sub-main-scale on polynomially many points of a
short block, Theorem 8.1 forces too much denominator support for the
moving-support strategy.  If (13.1) is main-scale, one must still control
the surviving cofactor and (13.2), and verify a fixed- or moving-support
Subspace-Theorem inequality.  A moving block must also retain sufficiently
many distinct primitive points after exact deduplication.

No archived theorem and no theorem proved here establishes any of those
requirements for the actual factorial digits of $\pi$.  Hence this note
does not close irrationality or transcendence of $e+\pi$; it isolates the
near-diagonal obstruction more sharply.

