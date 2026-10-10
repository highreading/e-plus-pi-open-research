> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Optimal integer Robin localizers and the unavoidable harmonic denominator

Checked: 2026-08-27 UTC.

## 1. Verdict

Put



$$
u=1+x^2,\qquad t=1-x,\qquad
 {\cal T}P=(1-x)P'(x)-xP(x).
\tag{1}
$$



The congruence needed to preserve both Robin jets is



$$
h\equiv1\pmod {u^2}.              \tag{2}
$$



There is a particularly simple, sup-norm-optimal integer family:



$$
\boxed{h_m(x)=x^{4m}(m+1-mx^4),\qquad m\geq1.}            \tag{3}
$$



It satisfies



$$
h_m\equiv1\pmod {u^2},\qquad h_m(0)=0,\qquad h_m(1)=1,
 \qquad 0\leq h_m\leq1\quad(0\leq x\leq1),               \tag{4}
$$



and



$$
I_m:=\int_0^1h_m(x)\,dx
 =\frac{8m+5}{(4m+1)(4m+5)}\sim\frac1{2m}.                \tag{5}
$$



No admissible integer polynomial can have smaller sup norm: every
integer $h$ satisfying (2) obeys $h(1)\equiv1\pmod4$, and hence
$\|h\|_{[0,1]}\geq1$.  Thus (3) is an exact integer boundary layer,
not a numerical approximation to one.

For every fixed polynomial $K$, the product rule gives the useful
$L^1$ localization



$$
\|{\cal T}(h_mK)\|_{L^1(0,1)}
 \leq I_m\bigl(\|{\cal T}K\|_\infty+\|K\|_\infty\bigr)
 =O_K(m^{-1}).                                             \tag{6}
$$



The hoped application to the Taylor near-solution nevertheless fails in
two independent, exact ways.

First, let



$$
a_N=N!,\qquad
 P_N^{(0)}=N!\sum_{j=0}^{N-1}\frac{t^j}{(j+1)!},\qquad
 a_N+{\cal T}P_N^{(0)}=t^N.                               \tag{7}
$$



If an integer correction $K$ makes $P_N^{(0)}+K$ Robin, then



$$
\operatorname{ord}_{x=1}K<N.        \tag{8}
$$



This is proved below for every $N\geq1$, using only arithmetic in
$\mathbb Z[i]$.  If $r=\operatorname{ord}_{x=1}K$, the exact boundary
scaling then has a sign-changing limit:



$$
\begin{split}
 &m^r\left\{t^N+{\cal T}(h_mK)\right\}
       \left(1-\frac y{4m}\right)\\
 &\hspace{12mm}\longrightarrow
 -\frac{c\,y^r}{4^r}e^{-y}
       \left((r+1)(1+y)-y^2\right),                       \tag{9}
 \end{split}
$$



where $K(1-t)=ct^r+O(t^{r+1})$ and $c\ne0$.  Consequently, for each
fixed $N$ and each fixed admissible $K$, the localized residual in
(9) is negative somewhere on $[0,1]$ for every sufficiently large
$m$.  Large $m$ destroys positivity.

Second, the rational output has an unavoidable dense harmonic channel.
If



$$
{\cal T}K=uG+(A+Bx),                                     \tag{10}
$$



then the correction condition forces



$$
A=N!-\Re(1-i)^N,\qquad B=-\Im(1-i)^N.                    \tag{11}
$$



In particular $A>0$ for $N\geq2$, independently of the chosen
representative $K$.  If $q_{N,K}(m)$ is the reduced denominator of
the rational coordinate



$$
4\int_0^1\frac{{\cal T}(P_N^{(0)}+h_mK)}{1+x^2}\,dx,     \tag{12}
$$



then, for fixed $N,K$,



$$
\log q_{N,K}(m)\geq
                    \left(\frac12+o(1)\right)m.           \tag{13}
$$



The proof is prime by prime: apart from primes dividing $A$, every
prime in $(5m/2,3m)$ occurs in the reduced denominator.  The sparse
shape of (3) therefore does *not* make the actual Robin output have a
polynomial denominator.  Polynomial denominator growth occurs only when
${\cal T}K$ is already divisible by $u$, a case which cannot repair
the nonzero Taylor defect.

Finally, even conditional positivity cannot turn this denominator into
a small primitive form.  The residual in (9) has value $1$ at $x=0$.
If it is nonnegative and has degree $d$, its weighted integral is at
least $3/(d+1)^2$.  Exact primitive normalization can cancel the output
denominator against at most $N!$.  Thus the primitive positive value is
at least



$$
\frac{3q_{N,K}(m)}{N!(d+1)^2}.           \tag{14}
$$



For example, on any diagonal with
$\deg K=o(m)$ and $N\log N=o(m)$, the right side grows
exponentially rather than tending to zero.

These results close this particular integer-localizer mechanism.  They
do not prove irrationality or transcendence of $e+\pi$.

## 2. Exact endpoint arithmetic

Suppose $h\in\mathbb Z[x]$ has the two complex jets



$$
h(i)=1,\qquad h'(i)=0.                 \tag{15}
$$



Conjugation supplies the same jets at $-i$.  Therefore $h-1$ has
double zeros at both $i$ and $-i$, so $u^2\mid h-1$ in
$\mathbb Q[x]$.  Division by the monic integer polynomial $u^2$
shows that the quotient is in $\mathbb Z[x]$.  Hence



$$
h=1+u^2q,\qquad q\in\mathbb Z[x]. \tag{16}
$$



At the right endpoint this gives



$$
h(1)=1+4q(1)\equiv1\pmod4.        \tag{17}
$$



Thus $h(1)=0$ and $h(1)=-1$ are impossible.  In particular, asking
for both endpoints to vanish is arithmetically inconsistent, and every
admissible $h$ has sup norm at least $1$.  There is no analogous
restriction at zero beyond $h(0)=1+q(0)$, which can be any integer.

If two nonzero endpoint layers are desired, one may set



$$
H_{m,\epsilon}=h_m+\epsilon u^2(1-x)^{4m},
 \qquad \epsilon\in\{-1,1\}.                              \tag{18}
$$



Then $H_{m,\epsilon}\equiv1\pmod {u^2}$, its endpoints are
$(\epsilon,1)$,



$$
\|H_{m,\epsilon}\|_\infty\leq5,\qquad
 \int_0^1|H_{m,\epsilon}|\,dx
 \leq I_m+\frac4{4m+1}=O(m^{-1}).                         \tag{19}
$$



This two-sided variant is included only to settle the endpoint
construction question.  Its left layer is not useful for Stein
localization, because the factor $1-x$ in ${\cal T}$ does not
suppress a derivative layer at $x=0$.

## 3. Construction and optimality of the boundary layer

Let



$$
f_m(z)=(m+1)z^m-mz^{m+1}.                                \tag{20}
$$



Since $f_m(1)=1$ and $f_m'(1)=0$, the polynomial $f_m(z)-1$ is
divisible by $(z-1)^2$.  More exactly,



$$
f_m(z)-1=-(z-1)^2\sum_{j=0}^{m-1}(j+1)z^j.              \tag{21}
$$



Substitution $z=x^4$ gives both (2) and the identity



$$
h_m-1=-u^2(1-x^2)^2
             \sum_{j=0}^{m-1}(j+1)x^{4j}.                \tag{22}
$$



Moreover,



$$
h_m'(x)=4m(m+1)x^{4m-1}(1-x^4)\geq0                    \tag{23}
$$



on $[0,1]$.  The endpoint values in (4) therefore prove
$0\leq h_m\leq1$.  Together with (17), this proves exact sup-norm
optimality.  Direct integration gives



$$
\int_0^1h_m
 =\frac{m+1}{4m+1}-\frac m{4m+5}
 =\frac{8m+5}{(4m+1)(4m+5)}.                              \tag{24}
$$



Integration by parts, using $h_m(0)=0$ and $h_m(1)=1$, also gives



$$
\int_0^1(1-x)h_m'(x)\,dx=I_m.           \tag{25}
$$



There is a general degree barrier behind this construction.  If $p$
is a real polynomial of degree at most $d$, expansion in shifted
Legendre polynomials gives



$$
|p(0)|,|p(1)|\leq(d+1)^2\int_0^1|p(x)|\,dx.              \tag{26}
$$



Indeed, for $L_k(x)=P_k(2x-1)$, one has
$|L_k|\leq1$,
$\int_0^1L_jL_k=\delta_{jk}/(2k+1)$, and
$|L_k(0)|=|L_k(1)|=1$.  Summing the absolute values of the
Legendre coefficients yields (26).  Thus any degree-$d$ admissible
integer $h$ has $\int|h|\geq(d+1)^{-2}$.  Formula (24) is of order
$1/d$; it is optimal in sup norm, though no claim of $L^1$-optimality
is made.

## 4. Stein localization and its sup-norm dichotomy

The product rule is



$$
{\cal T}(h_mK)=h_m{\cal T}K+(1-x)h_m'K.                  \tag{27}
$$



Equations (4), (24), and (25) prove (6).  Since
$e^x+4/(1+x^2)<7$ on $[0,1]$, the same estimate, multiplied by
$7$, controls the absolute weighted integral.

There is no analogous sup localization unless $K(1)=0$, because



$$
{\cal T}(h_mK)(1)=-K(1).            \tag{28}
$$



If $K=(1-x)J$, then ${\cal T}K=(1-x)L$ for another polynomial
$L$, and



$$
\|{\cal T}(h_mK)\|_\infty
 \leq\|L\|_\infty A_m+\|J\|_\infty B_m,                 \tag{29}
$$



where elementary one-variable maximization gives



$$
A_m:=\sup(1-x)h_m\leq\frac5{4m},\qquad
 B_m:=\sup(1-x)^2h_m'\leq\frac7m.                         \tag{30}
$$



For the first bound use
$h_m\leq x^{4m}(1+4m(1-x))$ and maximize the two terms.
For the second use $1-x^4\leq4(1-x)$ and



$$
\max_{0\leq x\leq1}(1-x)^3x^{4m-1}
 \leq \frac{27}{(4m+2)^3},
$$



which yields
$B_m\leq54m(m+1)/(2m+1)^3\leq7/m$.

Within one fixed class modulo $u^2$, the value at $1$ can change
only by a multiple of $4$.  Thus a representative with $K(1)=0$
exists only if the original value is divisible by $4$.

## 5. No Taylor correction can vanish to order $N$

Let $w=1-i$, a Gaussian prime above $2$.  Suppose that an integer
correction $K$ makes $P_N^{(0)}+K$ Robin and, contrary to (8), that



$$
K=t^NS(t),\qquad S\in\mathbb Z[t]. \tag{31}
$$



In the $t$-coordinate,



$$
{\cal T}C=-tC'(t)-(1-t)C(t).             \tag{32}
$$



The equation
${\cal T}K(i)=N!-w^N$, divided by $w^N$, becomes



$$
(w-N-1)S(w)-wS'(w)=U_N:=\frac{N!}{w^N}-1.               \tag{33}
$$



Write $\nu_w$ for the $w$-adic valuation.  For rational integers,



$$
\nu_w(N!)=2\nu_2(N!).             \tag{34}
$$



For $N=1,3$, this valuation is smaller than $N$, so the right side
of (33) is not even a Gaussian integer, whereas the left side is.

For odd $N\geq5$, the elementary estimate



$$
2\nu_2(N!)-N
 \geq2\left(\left\lfloor\frac N2\right\rfloor+
                 \left\lfloor\frac N4\right\rfloor\right)-N
 \geq1                                                       \tag{35}
$$



shows $U_N\equiv-1\pmod w$.  On the other hand, reduction of the
left side of (33) modulo $w$ gives
$-(N+1)S(0)\equiv0\pmod w$, because $N+1$ is even.  This is a
contradiction.

For even $N\geq4$, the same estimate gives



$$
2\nu_2(N!)-N\geq2.                \tag{36}
$$



Write $S(w)\equiv s_0+s_1w\pmod {w^2}$.  Since the terms of degree
at least two in $S$, and their contribution to $wS'$, vanish modulo
$w^2$, the left side of (33) is



$$
-(N+1)s_0+w\{s_0-(N+2)s_1\}\pmod {w^2}.                 \tag{37}
$$



Now $(w^2)=(2)$, and $1,w$ form a basis modulo $2$.  Since
$U_N\equiv-1\pmod {w^2}$, comparison of the constant coefficient
forces $s_0$ odd, while comparison of the $w$-coefficient forces
$s_0-(N+2)s_1$ even.  The latter is impossible because $N+2$ is
even.

It remains only $N=2$.  Here $U_2=-w$.  Formula (37) modulo
$w^2$ would require $s_0$ to be simultaneously even from the
constant coefficient and odd from the $w$-coefficient.  This is again
impossible.  The four cases prove (8) for every $N\geq1$.

## 6. The boundary profile forces a sign change

Fix $N$ and an admissible correction $K$.  By (8), write



$$
K(1-t)=ct^r+O(t^{r+1}),
                  \qquad c\ne0,\quad 0\leq r<N.           \tag{38}
$$



For fixed $y>0$, set $x=1-y/(4m)$.  Directly from (3),



$$
h_m\left(1-\frac y{4m}\right)\longrightarrow
 \phi(y):=e^{-y}(1+y),                                    \tag{39}
$$



and



$$
(1-x)h_m'(x)\longrightarrow-y\phi'(y)=y^2e^{-y}.         \tag{40}
$$



Also



$$
{\cal T}K=-(r+1)ct^r+O(t^{r+1}).                         \tag{41}
$$



Substitution in (27) proves (9), since
$m^rt^N\to0$.  The bracket in (9) is positive at $y=1$ and
negative at $y=2r+3$.  The two limiting values therefore have
opposite signs.  For all sufficiently large $m$, the actual residual
has opposite signs at the corresponding two points of $[0,1]$, so it
cannot be nonnegative.

The threshold is effective for each specified polynomial.  If
$K(1-t)=\sum_{s=r}^dc_st^s$, the error after multiplication by
$m^r$ is bounded by elementary expressions involving



$$
\frac1m\sum_{s>r}|c_s|
          \left(\frac{2r+3}{4}\right)^{s-r}.              \tag{42}
$$



Thus a varying family $K_N$ requires coefficient-height control before
one obtains a uniform threshold in $N$.  The theorem rules out taking
$m\to\infty$ for each fixed correction; it does not assert negativity
for every possible moderate diagonal choice $m=m(N)$.

## 7. Exact rational output and the dense defect channel

Assume $P_N^{(0)}+K$ is Robin.  Define integer polynomials $G_0,G$
and integers $A,B$ by



$$
\frac{{\cal T}(P_N^{(0)}+K)}u=G_0,
 \qquad {\cal T}K=uG+(A+Bx).                              \tag{43}
$$



Because $h_m\equiv1\pmod {u^2}$, the polynomial
$P_N^{(0)}+h_mK$ is also Robin.  The product rule and (43) give the
exact polynomial identity



$$
\begin{split}
 D_{m,K}
 &:=\frac{{\cal T}(P_N^{(0)}+h_mK)-
             {\cal T}(P_N^{(0)}+K)}{u}\\
 &=(h_m-1)G+\frac{h_m-1}{u}(A+Bx)
       +(1-x)\frac{h_m'}uK.                               \tag{44}
 \end{split}
$$



Here



$$
\frac{h_m'}u=4m(m+1)x^{4m-1}(1-x^2).                    \tag{45}
$$



Write $G=\sum g_jx^j$, $K=\sum k_jx^j$, and set



$$
d_j=\frac1{4j+1}-\frac1{4j+3},\qquad
 e_j=\frac1{4j+2}-\frac1{4j+4},                           \tag{46}
$$





$$
S_A(m)=\sum_{j=0}^{m-1}d_j-md_m,\qquad
 S_B(m)=\sum_{j=0}^{m-1}e_j-me_m.                         \tag{47}
$$



The rational coordinate $C_{N,K}(m)$ in (12) is exactly



$$
\begin{split}
 C_{N,K}(m)
 &=4\int_0^1G_0\,dx\\
 &\quad+4(m+1)\sum_j\frac{g_j}{4m+j+1}
       -4m\sum_j\frac{g_j}{4m+j+5}
       -4\sum_j\frac{g_j}{j+1}\\
 &\quad-4A S_A(m)-4B S_B(m)\\
 &\quad+16m(m+1)\sum_jk_j
 \left(\frac1{4m+j}-\frac1{4m+j+1}
       -\frac1{4m+j+2}+\frac1{4m+j+3}\right).            \tag{48}
\end{split}
$$



To verify the third line, use (22) and



$$
u(1-x^2)^2=1-x^2-x^4+x^6.                               \tag{49}
$$



The coefficient of $A$, before the minus sign, is



$$
\sum_{j=0}^{m-1}(j+1)(d_j-d_{j+1})
 =\sum_{j=0}^{m-1}d_j-md_m,                               \tag{50}
$$



and the $B$-identity is identical with $e_j$.

There is a small but important logical point.  The integral
$4\int {\cal T}(h_mK)/u$ by itself need not be rational when
${\cal T}K\not\equiv0\pmod u$; it can contain arctangent and logarithm
terms.  The rational object is (12), where the Taylor defect cancels the
remainder.  Formula (48) computes that object without any transcendental
terms.

If $K$ is already Robin, then $A=B=0$, and (48) has only finitely
many linear denominators in $m$.  In particular its reduced
denominator divides a fixed integer times



$$
\prod_{g_j\ne0}(4m+j+1)(4m+j+5)
 \prod_{k_j\ne0}\prod_{c=0}^3(4m+j+c),                   \tag{51}
$$



so it grows polynomially for fixed $K$.  But such a $K$ does not
change the Taylor Robin defect and therefore cannot be the required
correction.

For an actual correction, reduction of
${\cal T}K=N!-t^N\pmod u$ gives exactly (11).  For $N\geq2$,
$A>0$: the case $N=2$ is direct, and for $N\geq3$,
$N!>|1-i|^N=2^{N/2}$.

## 8. Exponential denominator theorem

Let $q_{N,K}(m)$ be the positive reduced denominator of (48), and put



$$
D=\max\{\deg G_0+1,\deg G+5,\deg K+3,5\}.                \tag{52}
$$



Assume $m>D$, and let $p$ be a prime satisfying



$$
\frac{5m}{2}<p<3m,\qquad p\nmid A.     \tag{53}
$$



Among all denominators in $S_A(m)$, exactly one is divisible by $p$,
namely the denominator $p$ itself.  Its coefficient is $+1$ or
$-1$.  The terminal denominators $4m+1,4m+3$ are not divisible by
$p$, and no other odd multiple of $p$ is in range.

Every denominator in $S_B(m)$ is even.  It cannot be divisible by
$p$: the first possible multiple is $2p>5m$, beyond its range.
The fixed low denominators and the denominators from $G_0$ are smaller
than $p$.  Every sparse high denominator in the other two lines of
(48) lies between $4m$ and $5m$; it is too large to equal $p$ and
too small to equal $2p$.  Therefore every term of (48) except the
single $\mp4A/p$ is $p$-integral.  Since $p\nmid A$,



$$
v_p(C_{N,K}(m))=-1.               \tag{54}
$$



Consequently



$$
q_{N,K}(m)\ \text{is divisible by}
 \prod_{\substack{5m/2<p<3m\\p\nmid A}}p,                \tag{55}
$$



and, with $\vartheta$ denoting Chebyshev's function,



$$
\log q_{N,K}(m)
 \geq\vartheta(3m)-\vartheta(5m/2)-\log|A|.              \tag{56}
$$



The prime number theorem proves (13).  More generally, for a varying
family, if



$$
\deg K=o(m),\qquad N=o(m),\qquad \log|A|=o(m),            \tag{57}
$$



then the same $(1/2+o(1))m$ lower bound holds.  Since
$\log A=N\log N+O(N)$, it is enough here to require
$N\log N=o(m)$ and $\deg K=o(m)$.

For fixed $K$, (48) also gives an exponential upper bound: the dense
denominator divides $\operatorname{lcm}(1,\ldots,4m+4)$, while all
remaining $m$-dependent factors form the fixed finite product (51).
Thus $\log q_{N,K}(m)=\Theta(m)$ whenever $A\ne0$.  This is a
genuine lcm-scale obstruction, not merely a large numerator in a
nonreduced expression.

## 9. Primitive positivity barrier

Set



$$
F_{N,K,m}=t^N+{\cal T}(h_mK).                            \tag{58}
$$



Since $h_mK$ and its derivative vanish at $x=0$,



$$
F_{N,K,m}(0)=1.              \tag{59}
$$



If $F_{N,K,m}\geq0$ and $d=\deg F_{N,K,m}$, (26) gives



$$
\int_0^1F_{N,K,m}\,dx\geq\frac1{(d+1)^2}.               \tag{60}
$$



The common-kernel weight



$$
W(x)=e^x+\frac4{1+x^2}            \tag{61}
$$



is at least $3$ on $[0,1]$, so the positive weighted integral
$L_{N,K,m}$ is at least $3/(d+1)^2$.

Write its exact output as



$$
L_{N,K,m}=N!(e+\pi)+\frac pq,
                 \qquad (p,q)=1,\quad q>0.                \tag{62}
$$



Adding the integer terms $-N!-P(0)$ to (12) does not change its
denominator, so this $q$ is exactly $q_{N,K}(m)$.  After clearing
the denominator, the two integer coefficients are $qN!$ and $p$.
Their content is



$$
g=\gcd(qN!,p)=\gcd(N!,p)\mid N!,  \tag{63}
$$



because $(p,q)=1$.  The fully primitive positive value is therefore



$$
\frac qgL_{N,K,m}
 \geq\frac{3q}{N!(d+1)^2},                                \tag{64}
$$



which is (14).  Under the diagonal assumptions following (14),
$d=O(m)$, and equations (56) and (64) show that this lower bound tends
to infinity exponentially.

## 10. Replay and exact scope

From the research directory run

    python3 scripts/common_kernel_integer_robin_localizer_certificate.py
    sha256sum -c results/common_kernel_integer_robin_localizer_hashes.sha256

The replay checks (21)--(25), the product-rule quotient (44), the full
rational formula (48), the Gaussian order obstruction through a finite
audit grid, and every predicted prime valuation in selected exact
examples.  It also records the maximal attainable endpoint order through
$N=30$ as a finite Smith-lattice diagnostic only.  The all-$N$
statements are the proofs above, not extrapolations from that table.

The machine's hardware accelerator is not used: these are small exact
integer and rational operations, for which GPU floating-point throughput
does not help.  The replay has a memory failure guard but does not cap or
reserve the approximately $50$ GiB of Colab RAM.

This package proves an optimal integer localizer and a rigorous barrier
to its proposed Taylor--Robin use.  It proves no arithmetic classification
of $e+\pi$.
