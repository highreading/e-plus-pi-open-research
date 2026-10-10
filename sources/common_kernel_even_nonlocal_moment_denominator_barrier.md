> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Even nonlocal Robin localizers force a one-third prime window

Checked: 2026-08-27 UTC.

## 1. Verdict

Put



$$
u=1+x^2.
$$



Let



$$
h\in\mathbb Z[x],\qquad h\equiv1\pmod {u^2},\qquad
 h(0)=0,
$$



and write



$$
n=\operatorname {ord}_0h,\qquad d=\deg h,
 \qquad r=\frac{h-1}{u}\in\mathbb Z[x].                 \tag{1}
$$



The preceding high-order-localizer theorem isolated primes in
$d/2<p\leq n$.  This note proves a strictly larger all-parameter
window when $h$ is even:



$$
\boxed{
 \prod_{\substack{d/3<p\leq n\\p>2}}p
 \ \bigg|\ 
 \operatorname {den}\!\left(\int_0^1r(x)\,dx\right).}   \tag{2}
$$



Every displayed prime occurs in the reduced denominator to
exact exponent one.  If



$$
I_0(h)=\int_0^1r(x)\,dx,
 \qquad I_1(h)=\int_0^1xr(x)\,dx,                         \tag{3}
$$



and $D(h)$ is the least positive integer which clears both moments,
then the product in (2) also divides $D(h)$.

If in addition



$$
0\leq h(x)\leq1\quad(0\leq x\leq1),        \tag{4}
$$



then the attainable moment pair obeys the denominator-cleared lower
bound



$$
\boxed{
 D(h)\max\{|I_0(h)|,|I_1(h)|\}
 \geq \frac1{16d^2}
          \prod_{\substack{d/3<p\leq n\\p>2}}p.} \tag{5}
$$



Consequently, for every fixed $\varepsilon>0$, along any even family
with



$$
n\geq\left(\frac13+\varepsilon\right)d,                 \tag{6}
$$



the logarithm of the denominator and of the right side of (5) is at
least



$$
\varepsilon d+o(d).              \tag{7}
$$



This includes genuinely nonlocal degree/order ratios which the
one-half-window theorem did not cover.  In particular, the explicit
positive family



$$
h_k(x)=(2x^4-x^8)^k              \tag{8}
$$



has



$$
\operatorname {ord}_0h_k=4k,qquad \deg h_k=8k.          \tag{9}
$$



For this boundary family,



$$
\prod_{8k/3<p\leq4k}p\mid D(h_k),                       \tag{10}
$$



and



$$
\int_0^1h_k(x)\,dx\sim\frac{\sqrt\pi}{8\sqrt k}.       \tag{11}
$$



Thus



$$
\log\left(D(h_k)\int_0^1h_k\right)
 \geq\frac43k+o(k),                                     \tag{12}
$$



so clearing the two defect moments overwhelms the localization gain.

Evenness is used in an essential and completely explicit place: it
kills the coefficient paired with the denominator $2p$.  Without
evenness that coefficient is free once $2p\geq n$.  The theorem does
not cover arbitrary non-even localizers, even localizers with
$d\geq(3-o(1))n$, or cancellations with the other correction
channels.  Section 6 gives the exact residue that would have to be
controlled to extend the result to the full Robin output.

This package proves neither irrationality nor transcendence of
$e+\pi$.

## 2. The forced prefix and parity

Write



$$
r(x)=\sum_{j=0}^{d-2}r_jx^j.
$$



The degree is exactly $d-2$: the nonconstant polynomial $h$ has
positive degree, so $h-1$ has degree $d$, and $u$ is monic of
degree two.  Coefficient comparison in



$$
ur=h-1
$$



gives



$$
r_j+r_{j-2}=h_j-\delta_{j0},qquad r_{-1}=r_{-2}=0.      \tag{13}
$$



Because $h_0=\cdots=h_{n-1}=0$, induction gives the forced prefix



$$
\boxed{
 r_{2a}=(-1)^{a+1},\qquad r_{2a+1}=0
 \quad(2a,2a+1<n).}                                      \tag{14}
$$



If $h$ is even, then $r$ is even.  One quick proof is to split
$r=r_{\rm ev}+r_{\rm odd}$.  Since $u$ is even and
$ur=h-1$ is even, the odd polynomial $ur_{\rm odd}$ vanishes;
hence $r_{\rm odd}=0$.  Thus



$$
r_{2a+1}=0                  \tag{15}
$$



at every degree, not merely in the forced prefix.

## 3. Proof of the one-third-window theorem

Let $p$ be a prime with



$$
\frac d3<p\leq n.           \tag{16}
$$



Here $n$ is even, so an odd $p\leq n$ actually satisfies $p<n$.
The possible denominators in



$$
I_0(h)=\sum_{j=0}^{d-2}\frac{r_j}{j+1}       \tag{17}
$$



range from one through $d-1$.  Since $3p>d$, the only multiples of
$p$ in that range are $p$ and, when it is at most $d-1$, $2p$.
Also $d<3p\leq p^2$ for odd $p$, so none of these denominators is
divisible by $p^2$.

The numerator paired with $p$ is forced by (14):



$$
r_{p-1}=(-1)^{(p+1)/2}\in\{1,-1\}.                     \tag{18}
$$



The numerator paired with $2p$ is zero by global parity:



$$
r_{2p-1}=0.                 \tag{19}
$$



Every remaining term in (17) is $p$-integral.  It follows that



$$
v_p(I_0(h))=-1.             \tag{20}
$$



Distinct primes multiply, proving (2).  This is an all-parameter proof;
no distributional or independence assumption about the coefficients of
$h$ is being made.

Let $\vartheta(y)=\sum_{p\leq y}\log p$.  The prime number theorem
$\vartheta(y)=y+o(y)$, together with $n\leq d$, gives from (2)



$$
\log D(h)\geq\vartheta(n)-\vartheta(d/3)-\log2
             \geq\varepsilon d+o(d)                     \tag{21}
$$



under (6).  The finitely many endpoint conventions do not affect the
asymptotic statement.

## 4. A denominator-cleared moment lower bound

Assume (4), and put $f=1-h$.  Then



$$
0\leq f\leq1,qquad f(0)=1,qquad \deg f=d.              \tag{22}
$$



The shifted Markov inequality on $[0,1]$ gives



$$
\lVert f'\rVert_\infty\leq2d^2. \tag{23}
$$



Therefore $f(x)\geq1/2$ for
$0\leq x\leq1/(4d^2)$.  As $u\leq2$ on $[0,1]$,



$$
\begin{aligned}
 -I_0(h)
 &=\int_0^1\frac{1-h(x)}{1+x^2}\,dx\\
 &\geq\int_0^{1/(4d^2)}\frac{f(x)}{1+x^2}\,dx
 \geq\frac1{16d^2}.                                     \tag{24}
\end{aligned}
$$



Combine (24) with the divisibility (2) of the common clearing
denominator $D(h)$ to obtain (5).  In the regime (6), the polynomial
factor $16d^2$ costs only $O(\log d)=o(d)$, proving (7).

For comparison, the exact identities



$$
\begin{aligned}
 I_0(h)&=-\frac\pi4+\int_0^1\frac{h(x)}{1+x^2}\,dx,\\
 I_1(h)&=-\frac{\log2}{2}
          +\int_0^1\frac{xh(x)}{1+x^2}\,dx              \tag{25}
\end{aligned}
$$



show that both moments are negative for every nontrivial $h$ satisfying
(4).  Equation (24), unlike a Diophantine approximation bound extracted
only from (25), is uniform in the attainable denominator.

## 5. A positive family exactly on the old boundary

Let



$$
a(x)=2x^4-x^8.
$$



The factorization



$$
a(x)=1-(1-x^4)^2,qquad
 a(x)-1=-(1+x^2)^2(1-x^2)^2                              \tag{26}
$$



shows both



$$
0\leq a(x)\leq1\quad(0\leq x\leq1)
$$



and $a\equiv1\pmod {u^2}$.  Powers preserve both properties.  The
lowest and highest terms of $a^k=x^{4k}(2-x^4)^k$ prove (9), and the
one-third-window theorem proves (10).

It remains to justify the analytic scale (11) without extrapolating
finite data.  Set $t=1-x$ and



$$
A(t)=a(1-t).
$$



Taylor expansion at zero gives



$$
A(t)=1-16t^2+O(t^3).             \tag{27}
$$



For $0\leq t\leq1$,



$$
1-A(t)=\bigl(1-(1-t)^4\bigr)^2\geq t^2,                 \tag{28}
$$



because $(1-t)^4\leq1-t$.  Hence



$$
0\leq A(t)^k\leq e^{-kt^2}.      \tag{29}
$$



After the substitution $y=\sqrt k\,t$, (27) gives pointwise
convergence



$$
A(y/\sqrt k)^k\longrightarrow e^{-16y^2}, \tag{30}
$$



while (29) supplies the integrable majorant $e^{-y^2}$ on
$[0,\infty)$ after extending the integrand by zero past $\sqrt k$.
Dominated convergence proves



$$
\sqrt k\int_0^1h_k(x)\,dx
 =\int_0^{\sqrt k}A(y/\sqrt k)^k\,dy
 \longrightarrow\int_0^\infty e^{-16y^2}\,dy
 =\frac{\sqrt\pi}{8},                                   \tag{31}
$$



which is (11).

Finally,



$$
\log\prod_{8k/3<p\leq4k}p
 =\vartheta(4k)-\vartheta(8k/3)
 =\frac43k+o(k).                                         \tag{32}
$$



Equations (10), (11), and (32) prove (12).  Thus raising a positive
congruence-preserving factor to high powers is not a way around the
denominator loss at degree $d=2n$.

## 6. What happens in the full correction channel

For reference, let



$$
{\cal T}P=(1-x)P'-xP,\qquad
 {\cal T}K=uG+(\alpha+\beta x),                          \tag{33}
$$



and define



$$
S_h=\frac{{\cal T}(hK)-{\cal T}K}{u}
 =(h-1)G+r(\alpha+\beta x)
 +(1-x)\frac{h'}uK.                                      \tag{34}
$$



Write $S_h=\sum_{j=0}^{e}s_jx^j$.  For any odd prime



$$
p>\frac{e+1}{3},                                        \tag{35}
$$



only the denominators $p$ and $2p$ can contribute a negative
$p$-adic valuation to $\int_0^1S_h$.  Consequently the exact
criterion is



$$
\boxed{
 v_p\!\left(\int_0^1S_h\right)=-1
 \quad\Longleftrightarrow\quad
 2s_{p-1}+s_{2p-1}\not\equiv0\pmod p,}                   \tag{36}
$$



where a coefficient beyond the degree is read as zero.  If also



$$
p<n,qquad p-1>\deg G,qquad p\nmid\alpha,               \tag{37}
$$



then the forced prefix gives



$$
s_{p-1}=(-1)^{(p+1)/2}\alpha.    \tag{38}
$$



Thus the expanded-window prime survives precisely when



$$
s_{2p-1}\not\equiv
 -2(-1)^{(p+1)/2}\alpha\pmod p.                          \tag{39}
$$



This gives both a conditional extension and the exact obstruction.  If
$S_h$ itself is even, (39) is automatic for $p\nmid\alpha$, and the
one-third window extends to the full output.  Evenness of $h$ alone,
however, does not make $S_h$ even: the $\beta x$ term and the
derivative channel in (34) can produce $s_{2p-1}$.

For a linear correction $K=k_0+k_1x$, this freedom can be displayed
explicitly.  Put



$$
q=\frac{h-1}{u^2}.
$$



Then $G=-k_1$, $\alpha=2k_1$,
$\beta=-(k_0+k_1)$, and an exact coefficient calculation gives



$$
s_{2p-1}\equiv
 (k_0+k_1)\bigl(q_{2p-2}-q_{2p-4}\bigr)\pmod p.          \tag{40}
$$



Indeed, if $a=h'/u=4xq+uq'$, then



$$
a_{2p-1}\equiv2q_{2p-2},\qquad
 a_{2p-3}\equiv-2q_{2p-2}\pmod p.
$$



The odd coefficient in (34) is



$$
\beta r_{2p-2}+k_0a_{2p-1}-k_1a_{2p-3},
 \qquad r_{2p-2}=q_{2p-2}+q_{2p-4},
$$



which reduces to (40).

The two displayed coefficients of $q$ lie outside the forced prefix
in the genuinely new range and are not controlled by parity or by
$0\leq h\leq1$ through a coefficientwise congruence.  Therefore (36)
does not yield an unconditional product bound for the full channel.  This
is a precise residue obstruction, not an impossibility theorem for every
possible coupling.

## 7. Exact scope beyond the theorem

Positive, congruence-preserving polynomials exist far beyond the
one-third-window regime.  One explicit example is



$$
\begin{aligned}
 H(x)={}&2x^8-4x^7+7x^6-8x^5+7x^4-4x^3+x^2\\
       ={}&x^2(x^2-x+1)(2x^4-2x^3+3x^2-3x+1),            \tag{41}
\end{aligned}
$$



with



$$
\begin{aligned}
 H-1&=(1+x^2)^2(-1+3x^2-4x^3+2x^4),\\
 1-H&=(1-x)(1+x^2)^2(2x^3-2x^2+x+1).                    \tag{42}
\end{aligned}
$$



Both factors in the first line of (41) are positive on $[0,1]$.  For
the quartic factor, on $[1/2,1]$ use



$$
2x^4-2x^3+3x^2-3x+1=(1-x)^3+x^3(2x-1)\geq0,
$$



while on $[0,1/2]$,



$$
2x^4-2x^3+3x^2-3x+1
 =(1-3x+3x^2)-2x^3(1-x)\geq\frac14-\frac18>0.
$$



The last cubic in (42) is at least $1-8/27>0$ on $[0,1]$.
Therefore



$$
0\leq H\leq1,qquad
 \operatorname {ord}_0H=2,qquad \deg H=8.               \tag{43}
$$



Its powers have degree/order ratio four.  This exact construction shows
that positivity does not collapse every admissible family back into the
window of the theorem.  No claim is made here about the asymptotic
denominators of $H^k$.

The unresolved cases are therefore concrete:

* non-even positive localizers once $d\geq2n$;
* even positive localizers once $d\geq3n$;
* the congruence (39) in the full output when $S_h$ is not even; and
* cancellation between several varying correction channels.

Finite searches cannot settle any of these cases, and none is classified
in this note.

## 8. Replay and status

From the research directory run

    python3 scripts/common_kernel_even_nonlocal_moment_denominator_certificate.py
    sha256sum -c results/common_kernel_even_nonlocal_moment_denominator_hashes.sha256

The deterministic replay checks the quotient/parity identities, the
exact prime valuations through $k=120$, the positive family (8), the
linear-channel residue (40), and all polynomial identities and positivity
reductions for (41).  The finite instances certify normalization only;
the all-parameter claims are proved above.

The computation is exact integer/rational arithmetic, uses no hardware
accelerator, and has a 40-GiB resident-memory guard.  Its actual peak is
reported in the JSON certificate and is tiny relative to the available
Colab RAM.

This source is a rigorous partial obstruction in the nonlocal regime.  It
does not give a denominator bound for every admissible $h$, does not
close the common-kernel construction, and does not classify $e+\pi$.
