> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Positive common-kernel polynomials: an endpoint bootstrap and an unnormalized exponent-one barrier

Checked: 2026-08-27 UTC.

## 1. Verdict

Put



$$
A(g)=\sum_{k\geq0}(-1)^k g^{(k)}(1)
$$



and let $f\in\mathbb Z[x]$, of exact degree $n\geq1$, satisfy



$$
A(f)=f(i)=f(-i)=a\in\mathbb Z.
 \tag{1}
$$



There is an all-degree lower bound for every such polynomial with
$a\ne0$. Define



$$
z=-1+2i,
 \qquad
 R=\left|z-\sqrt{z^2-1}\right|=4.6115817893\ldots,
 \tag{2}
$$



where the square-root branch is chosen so that the displayed modulus is
greater than one, and put $C_R=R/(R-1)$. For $1\leq r\leq n$, set



$$
\mathcal D_{n,r}
 =\max\left\{1,
 \max_{1\leq k<r}
 \frac{2^{k+1}(n+1)n^{2k}}{(2k-1)!!}
 \right\}.
\tag{3}
$$



For $r=1$, the inner maximum in (3) is absent, so
$\mathcal D_{n,1}=1$.

Then



$$
\boxed{
 \|f\|_{[0,1]}
 \geq
 \max_{1\leq r\leq n}
 \min\left\{
 \mathcal D_{n,r}^{-1},
 \frac{r!}{C_RR^n}
 \right\}.}
 \tag{4}
$$



In particular, for every sequence of nonzero-target polynomials satisfying
(1), with degrees tending to infinity,



$$
\boxed{
 \liminf_{n\to\infty}
 \|f_n\|_{[0,1]}^{1/n}\geq R^{-1/2}
 =0.4656665496\ldots .}
 \tag{5}
$$



Now impose the denominator-free common-kernel structure



$$
f=a+(1+x^2)H',
 \qquad H\in\mathbb Z[x],
 \qquad A((1+x^2)H')=0,
 \tag{6}
$$



and suppose that $f\geq0$ on $[0,1]$ and $f\not\equiv0$. The exact
positive integral



$$
L(f)=\int_0^1 f(x)
 \left(e^x+\frac4{1+x^2}\right)dx
 =a(e+\pi)+b,
 \qquad b\in\mathbb Z,
 \tag{7}
$$



satisfies



$$
\boxed{
 L(f)\geq
 \min\left\{1,
 \frac{3}{8n^2}
 \max_{1\leq r\leq n}
 \min\left\{
 \mathcal D_{n,r}^{-1},
 \frac{r!}{C_RR^n}
 \right\}
 \right\}.}
 \tag{8}
$$



Consequently



$$
\boxed{
 \liminf_{n\to\infty}L(f_n)^{1/n}\geq R^{-1/2}.}
 \tag{9}
$$



There is also a height consequence. Along any subsequence for which



$$
-\frac1n\log L(f_n)\longrightarrow\gamma>0,
 \tag{10}
$$



one necessarily has



$$
\gamma\leq\frac12\log R,
 \qquad
 \liminf\frac1n\log|a_n|\geq\gamma,
 \qquad
 \limsup\frac{-\log L(f_n)}{\log|a_n|}\leq1.
 \tag{11}
$$



The last statement concerns the **unnormalized** output pair $(a_n,b_n)$.
This distinction is essential. If



$$
g_n=\gcd(a_n,b_n),
 \qquad
 (a_n^*,b_n^*)=(a_n/g_n,b_n/g_n),
 \qquad
 L_n^*=L(f_n)/g_n,
 \tag{12}
$$



then the factorial divisibility used below applies to $a_n$, not
automatically to $a_n^*$. Without an upper bound for $g_n$, (11) gives
no Roth-exponent bound for the primitive form. Thus (4)--(11) establish a
square-root-capacity barrier for the unnormalized positive construction,
not a closed no-go theorem after primitive normalization.

This does **not** rule out a positive family with $L(f_n)\to0$, which
would already prove irrationality by positivity. It also does not rule out
a family for which $L_n^*\to0$, or a primitive Roth-breaking family
created by unexpectedly large output gcds. No such all-degree integer family
or output-gcd theorem is constructed here, and nothing in this note proves
irrationality or transcendence of $e+\pi$.

## 2. Chebyshev coefficients and endpoint derivatives

Let



$$
E=\|f\|_{[0,1]},
 \qquad
 F(y)=f\left(\frac{y+1}{2}\right)
 =\sum_{j=0}^n c_jT_j(y).
 \tag{13}
$$



The Fourier formulas for Chebyshev coefficients give



$$
|c_0|\leq E,
 \qquad
 |c_j|\leq2E\quad(j\geq1).
 \tag{14}
$$



For $j\geq k\geq1$,



$$
T_j^{(k)}(1)
 =\frac{j^2(j^2-1^2)\cdots(j^2-(k-1)^2)}{(2k-1)!!}
 \leq\frac{n^{2k}}{(2k-1)!!}.
 \tag{15}
$$



Since $f^{(k)}(1)=2^kF^{(k)}(1)$, (14)--(15) imply



$$
|f^{(k)}(1)|
 \leq
 \frac{2^{k+1}(n+1)n^{2k}}{(2k-1)!!}\,E.
 \tag{16}
$$



The harmless factor $n+1$ makes this a direct consequence of the finite
Chebyshev expansion; no sharp higher-order Markov inequality is needed.

Every derivative $f^{(k)}(1)$ is an integer. Therefore, if



$$
E\mathcal D_{n,r}<1,
 \tag{17}
$$



then



$$
f(1)=f'(1)=\cdots=f^{(r-1)}(1)=0.
 \tag{18}
$$



It follows that $(1-x)^r\mid f$.

## 3. Factorial divisibility and exterior evaluation

For an integer polynomial,



$$
\frac{f^{(k)}(1)}{k!}\in\mathbb Z.
 \tag{19}
$$



Under (18), every surviving term in



$$
A(f)=\sum_{k=r}^n(-1)^kf^{(k)}(1)
 \tag{20}
$$



is divisible by $r!$. Hence



$$
r!\mid A(f)=a.
 \tag{21}
$$



If $a\ne0$, this gives $|a|\geq r!$.

At $y=z=-1+2i$, write



$$
T_j(z)=\frac{\omega^j+\omega^{-j}}2,
 \qquad |\omega|=R.
 \tag{22}
$$



Equations (13)--(14) give the geometric-series bound



$$
\begin{aligned}
 |f(i)|
 &\leq E\left(1+\sum_{j=1}^n(R^j+R^{-j})\right)\\
 &=E\frac{R^{n+1}-R^{-n}}{R-1}
 \leq C_RR^nE.
 \end{aligned}
 \tag{23}
$$



Combining (21) and (23), condition (17) forces



$$
E\geq\frac{r!}{C_RR^n}.
 \tag{24}
$$



If (17) fails, then $E\geq\mathcal D_{n,r}^{-1}$. Taking the smaller of
these two alternatives and then the maximum over $r$ proves (4).

## 4. Asymptotic optimization

For



$$
r=\left\lfloor\frac{c n}{\log n}\right\rfloor,
 \qquad c>0\ \hbox{fixed},
 \tag{25}
$$



Stirling's formula and the odd-double-factorial identity give



$$
\log(r!)=(c+o(1))n,
 \tag{26}
$$



and



$$
\begin{aligned}
 \log\mathcal D_{n,r}
 &\leq
 (r+1)\log2+\log(n+1)+2r\log n-\log(2r-1)!!\\
 &=(c+o(1))n.
 \end{aligned}
 \tag{27}
$$



Here the displayed upper bound also uses the fact that the elementary
majorants in (16) increase with $k<n$. Taking
$c=\tfrac12\log R$ in (4) makes both alternatives have exponential scale
$R^{-n/2}$, proving (5).

Equivalently, suppose on a subsequence that
$E\leq\exp(-\gamma n)$, with
$\gamma>\tfrac12\log R$. Choose



$$
\log R-\gamma<c<\gamma.
 \tag{28}
$$



Equations (16), (25), and (27) force the first $r$ endpoint derivatives
to vanish, so (21) gives



$$
|a|\geq\exp((c+o(1))n).
 \tag{29}
$$



But (23) gives



$$
|a|\leq\exp((\log R-\gamma+o(1))n),
 \tag{30}
$$



contradicting (28). This is the endpoint bootstrap behind the
square-root-capacity exponent.

## 5. Passing from sup norm to a positive integral

Let $f\geq0$ on $[0,1]$, $f\not\equiv0$, and $n\geq1$. The shifted
Markov inequality gives



$$
\|f'\|_{[0,1]}\leq2n^2E.
 \tag{31}
$$



At a point where $f$ attains $E$, an interval of length at least
$1/(4n^2)$ remains inside $[0,1]$ on one side, and (31) keeps
$f\geq E/2$ there. Hence



$$
\int_0^1f(x)\,dx\geq\frac{E}{8n^2}.
 \tag{32}
$$



The weight in (7) is at least $3$ on $[0,1]$, so



$$
L(f)\geq\frac{3E}{8n^2},
 \qquad
 E\leq\frac{8n^2}{3}L(f).
 \tag{33}
$$



If $a=0$, (7) and positivity give
$L(f)=b\in\mathbb Z_{>0}$, hence $L(f)\geq1$. If $a\ne0$, insert
(4) into (33). This proves (8), and the polynomial factor in (33) does not
change the $n$-th-root limit, so (9) follows.

For the height assertion, assume (10). Then (33) gives



$$
E_n\leq\exp((-\gamma+o(1))n).
 \tag{34}
$$



For every fixed $c<\gamma$, take $r$ as in (25). The endpoint bootstrap
gives



$$
\log|a_n|\geq\log(r!)=(c+o(1))n.
 \tag{35}
$$



Letting $c\uparrow\gamma$ proves the second assertion of (11), and the
unnormalized exponent-one statement follows. The first assertion of (11)
is (9).

After primitive normalization the exact consequence is only



$$
L_n^*\geq \frac{1}{g_n}
 \min\left\{1,
 \frac{3}{8n^2}
 \max_{1\leq r\leq n}
 \min\left\{
 \mathcal D_{n,r}^{-1},
 \frac{r!}{C_RR^n}
 \right\}\right\},
 \tag{36}
$$



which is ineffective without an independent upper bound for $g_n$.

## 6. Why Markov--Lukacs does not give a stronger blanket theorem

The Markov--Lukacs representations are



$$
f=p^2+x(1-x)q^2\quad(\deg f\ \hbox{even})
 \tag{37}
$$



and



$$
f=x p^2+(1-x)q^2\quad(\deg f\ \hbox{odd}),
 \tag{38}
$$



with real polynomials of the appropriate half-degrees. They certify every
polynomial nonnegative on $[0,1]$, but they do not turn $A$ into a
positive quadratic form. Indeed, after $x=1-t$,



$$
A\bigl(x(1-x)q^2\bigr)
 =\int_0^\infty e^{-t}t(1-t)q(1-t)^2\,dt,
 \tag{39}
$$



whose factor $t(1-t)$ changes sign. Likewise, one of the two terms in
(38) has a signed moment. Moreover, an integral $f$ does not provide
integer $p,q$, or a useful uniform bound for their denominators. Thus the
Laguerre lower bound for a single global square cannot be extended to the
whole interval-positive cone by (37)--(38).

The endpoint bootstrap avoids this problem: it uses only integrality of
the original polynomial, smallness on the interval, and the common-kernel
equalities.

## 7. The positive cone is genuinely nonempty

There is no qualitative impossibility theorem for positivity. An exact
endpoint-zero example is



$$
\begin{aligned}
 f(x)
 &=-4x(x-1)^2(3x^2-31)\\
 &=4x(1-x)^2(31-3x^2),
 \end{aligned}
 \tag{40}
$$



which is strictly positive on $0<x<1$. Put



$$
a=272,
 \qquad
 H(x)=-3x^4+8x^3+62x^2-272x.
 \tag{41}
$$



Direct calculation gives



$$
f=a+(1+x^2)H',
 \qquad
 A(f)=f(i)=f(-i)=272,
 \qquad
 f(0)=f(1)=0.
 \tag{42}
$$



Its second coordinate and positive form are



$$
b=-1544,
 \qquad
 L(f)=272(e+\pi)-1544>0.
 \tag{43}
$$



This finite example is not small. Its purpose is to show that a claimed
separation of the entire positive cone from the common-kernel plane would
be false.

## 8. Exact finite beta-cone diagnostic

For



$$
g_{n,k}(x)=x^{n+k}(1-x)^n,
 \tag{44}
$$



positivity is automatic. The two common-kernel discrepancy coordinates are



$$
\begin{aligned}
 C_{n,k}
 &=\bigl(A(g_{n,k})-\Re g_{n,k}(i),-\Im g_{n,k}(i)\bigr),\\
 A(g_{n,k})
 &=\sum_{j=0}^{n+k}(-1)^j
 \binom{n+k}{j}(n+j)!,\\
 g_{n,k}(i)&=(1+i)^ni^k.
 \end{aligned}
 \tag{45}
$$



The exact certificate scans every $1\leq n\leq40$. It finds a primitive
strictly positive three-column dependence among adjacent $k$'s:



$$
\begin{cases}
 k=(1,2,3),&n\equiv0,1\pmod4,\\
 k=(0,1,2),&n\equiv2,3\pmod4.
 \end{cases}
 \tag{46}
$$



For example, the primitive weights for $n=1,2,3,4$ are respectively



$$
(31,28,3),\quad
 (31,188,31),\quad
 (6007,5415,592),\quad
 (491405,5272908,491405).
 \tag{47}
$$



The scan in (46) is an exact **finite diagnostic**, not an asserted all-$n$
theorem. For every recorded relation the certificate checks the two
integer equations, nonzero real target, positivity of all weights, and
$n!\mid a$. It also divides $f-a$ by $1+x^2$, clears exactly the
coefficient denominators introduced by integration, and thereby verifies
that an integer multiple has the full form (6) with $H\in\mathbb Z[x]$.
For that scaled form it records $b$, the exact output gcd
$g=\gcd(a,b)$, the primitive pair, and the certified positive lower bound



$$
\frac{L(f)}g\geq\frac3g\int_0^1f(x)\,dx.
 \tag{48}
$$



All forty recorded primitive lower bounds exceed $5$, and they grow very
rapidly in this finite range. This is exact finite evidence only; it is not
an all-degree output-gcd theorem.

These feasible positive relations nevertheless fail asymptotically for an
immediate all-$n$ reason. Every combination in (44) retains



$$
x^n(1-x)^n\mid f.
 \tag{49}
$$



For any common-kernel combination with nonzero target and $k\leq3$,



$$
\|f\|_{[0,1]}
 \geq\frac{n!}{C_RR^{2n+3}},
 \tag{50}
$$



which tends to infinity. If the target is zero, denominator clearing makes
the positive integral a positive integer. Thus the beta cone is feasible,
but its fixed endpoint multiplicities make it unusable as a shrinking
unnormalized family. The finite gcd data show that primitive normalization
does not rescue the first forty adjacent relations, but no all-$n$ claim
about their output gcds is made.

## 9. Certificate and scope

The deterministic standard-library verifier is

    scripts/common_kernel_positive_cone_endpoint_bootstrap_certificate.py

and its frozen output is

    results/common_kernel_positive_cone_endpoint_bootstrap_certificate.json

It checks the exact positive witness (40)--(43), a rational enclosure of its
linear form, the algebraic enclosure used to display $R$, and every finite
beta-cone assertion in Section 8. The all-degree theorem (4) is the proof in
Sections 2--4; a finite computation is not used as a substitute for it.

The result is a rigorous no-go theorem for super-$R^{-n/2}$ decay of the
unnormalized positive integral, and an exponent-one constraint for the
unnormalized coefficient pair along exponentially shrinking positive
families. Without an output-gcd bound it is not a no-go theorem for the
primitive pair. It does not exclude exponent-one, subexponential, or
gcd-amplified positive families, and it does not decide the arithmetic
nature of $e+\pi$.
