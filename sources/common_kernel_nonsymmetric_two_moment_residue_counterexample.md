> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A positive nonsymmetric localizer can cancel both one-third-window moments

Checked: 2026-08-27 UTC.

## 1. Verdict

Put



$$
u=1+x^2.
$$



Let



$$
h\in\mathbb Z[x],\qquad h\equiv1\pmod {u^2},\qquad h(0)=0,
$$



and write



$$
n=\operatorname {ord}_0h,\qquad d=\deg h,\qquad
 r=\frac{h-1}{u}\in\mathbb Z[x].                         \tag{1}
$$



The two defect moments are



$$
I_0(h)=\int_0^1r(x)\,dx,\qquad
 I_1(h)=\int_0^1xr(x)\,dx.                               \tag{2}
$$



For every odd prime



$$
\frac d3<p<n,                   \tag{3}
$$



simultaneous $p$-integrality has the exact coefficient criterion



$$
\boxed{
\begin{aligned}
 I_0(h)\in\mathbb Z_{(p)}
 &\iff 2r_{p-1}+r_{2p-1}\equiv0\pmod p,\\
 I_1(h)\in\mathbb Z_{(p)}
 &\iff r_{2p-2}\equiv0\pmod p.
\end{aligned}}                                           \tag{4}
$$



Here $\mathbb Z_{(p)}$ is the localization of $\mathbb Z$ at $p$.
Any coefficient whose index exceeds $\deg r$ is read as zero.
The first low coefficient is the forced unit



$$
r_{p-1}=(-1)^{(p+1)/2},                                 \tag{5}
$$



while $r_{p-2}=0$.  Thus both moments are $p$-integral exactly when



$$
\boxed{
 r_{2p-1}\equiv-2(-1)^{(p+1)/2},\qquad
 r_{2p-2}\equiv0\pmod p.}                                \tag{6}
$$



Neither divisibility by $u^2$ nor sign control forbids (6).  The exact
positive polynomial



$$
\boxed{
 h(x)=(2x^4-x^8)^6
 \left(1-(1+x^2)^2x^3(1-x)^2\right)^2}                  \tag{7}
$$



satisfies



$$
\begin{gathered}
 h\in\mathbb Z[x],\qquad h\equiv1\pmod {u^2},\qquad
 0\leq h\leq1\quad(0\leq x\leq1),\\
 n=24,\qquad d=66.
\end{gathered}                                            \tag{8}
$$



For the prime $p=23$, which obeys



$$
d/3=22<23<n,                    \tag{9}
$$



the relevant exact coefficients are



$$
r_{22}=1,\qquad
 r_{44}=3887=23\cdot169,\qquad
 r_{45}=-1520.                                           \tag{10}
$$



Consequently



$$
2r_{22}+r_{45}=-1518=-66\cdot23,\qquad
 r_{44}=169\cdot23,                                      \tag{11}
$$



and both moments are $23$-integral.

This is a rigorous counterexample to the proposed prime-by-prime
extension of the even-localizer theorem: for arbitrary positive $h$,
one cannot assert that every prime $d/3<p<n$ divides the common moment
denominator.  It does **not** disprove a weaker aggregate product bound
which permits exceptional primes, and it says nothing by itself about
the full correction channel.

The previously identified ratio-four family $H^k$ has
$\operatorname {ord}_0H^k=2k$ and $\deg H^k=8k$, so its interval
$d/3<p<n$ is identically empty.  It neither supports nor contradicts
an aggregate theorem beyond degree/order ratio three.

This package proves neither irrationality nor transcendence of
$e+\pi$.

## 2. The forced coefficients

Write



$$
r(x)=\sum_{j=0}^{d-2}r_jx^j.
$$



Coefficient comparison in



$$
(1+x^2)r=h-1
$$



gives



$$
r_j+r_{j-2}=h_j-\delta_{j0},\qquad r_{-1}=r_{-2}=0.      \tag{12}
$$



Because $h_0=\cdots=h_{n-1}=0$, induction gives



$$
\boxed{
 r_{2a}=(-1)^{a+1},\qquad r_{2a+1}=0
 \quad(2a,2a+1<n).}                                      \tag{13}
$$



For odd $p<n$, substitution of $p-1$ and $p-2$ in (13) proves
(5) and



$$
r_{p-2}=0.                  \tag{14}
$$



No parity assumption is made on the coefficients at degrees near
$2p$.

## 3. Proof of the simultaneous residue criterion

The monomial expansions of the two moments are



$$
\begin{aligned}
 I_0(h)&=\sum_{j=0}^{d-2}\frac{r_j}{j+1},\\
 I_1(h)&=\sum_{j=0}^{d-2}\frac{r_j}{j+2}.                 \tag{15}
\end{aligned}
$$



Condition (3) gives $3p>d$.  Therefore the only denominators in either
line of (15) which are divisible by $p$ are $p$ and $2p$.
Moreover,



$$
d<3p\leq p^2                    \tag{16}
$$



for odd $p$, so none of the displayed denominators is divisible by
$p^2$.

Multiplying the first line of (15) by $p$ and reducing in
$\mathbb Z_{(p)}/p\mathbb Z_{(p)}$ gives



$$
pI_0(h)\equiv r_{p-1}+\frac12r_{2p-1}\pmod p.            \tag{17}
$$



Thus $I_0$ is $p$-integral precisely when the first congruence in
(4) holds.  Similarly,



$$
pI_1(h)\equiv r_{p-2}+\frac12r_{2p-2}
              \equiv\frac12r_{2p-2}\pmod p,              \tag{18}
$$



where (14) was used in the second step.  This proves the second
congruence in (4), and (5) then gives (6).

The hypothesis $h\equiv1\pmod {u^2}$ says that



$$
r=uq
$$



for some $q\in\mathbb Z[x]$.  It couples coefficients two degrees
apart within each parity branch, but it supplies no contradiction
between the odd condition on $r_{2p-1}$ and the even condition on
$r_{2p-2}$.  The positive example below proves that a hidden
coefficientwise incompatibility cannot be recovered merely from
$0\leq h\leq1$.

## 4. Proof that the counterexample is admissible

Define



$$
\begin{aligned}
 A(x)&=2x^4-x^8,\\
 B(x)&=1-(1+x^2)^2x^3(1-x)^2.                            \tag{19}
\end{aligned}
$$



Then $h=A^6B^2$.  The exact factorizations



$$
\begin{aligned}
 A-1&=-(1+x^2)^2(1-x^2)^2,\\
 B-1&=-(1+x^2)^2x^3(1-x)^2                              \tag{20}
\end{aligned}
$$



show that both factors, and hence their powers and product, are
congruent to one modulo $u^2$.

For $0\leq x\leq1$,



$$
A(x)=1-(1-x^4)^2\in[0,1].                               \tag{21}
$$



Also,



$$
0\leq x^3(1-x)^2\leq x(1-x)\leq\frac14,\qquad
 (1+x^2)^2\leq4.                                         \tag{22}
$$



Therefore



$$
0\leq (1+x^2)^2x^3(1-x)^2\leq1,
$$



and hence $B(x)\in[0,1]$.  This proves the sign control in (8).

The lowest term of $A$ is $2x^4$, whereas $B(0)=1$.  Thus



$$
\operatorname {ord}_0(A^6B^2)=24.             \tag{23}
$$



The degrees of $A$ and $B$ are eight and nine, with nonzero leading
coefficients.  Consequently



$$
\deg(A^6B^2)=6\cdot8+2\cdot9=66,              \tag{24}
$$



proving the remaining assertions in (8).

## 5. Exact arithmetic at $p=23$

Expanding (19) gives



$$
B=1-x^3+2x^4-3x^5+4x^6-3x^7+2x^8-x^9.                 \tag{25}
$$



Exact division of $A^6B^2-1$ by $1+x^2$ gives the three
coefficients in (10).  Equations (4) and (11) then prove simultaneous
$23$-integrality without requiring the full moment fractions.

For an independent reduced-fraction check, the two moments are



$$
\begin{aligned}
 I_0(h)
 &=-\frac{9392594521692168961341691}
          {12850727001117633342514800},\\
 I_1(h)
 &=-\frac{1690320846078465619890203}
          {5711434222718948152228800}.                   \tag{26}
\end{aligned}
$$



Their reduced denominators are congruent to $22$ and $20$,
respectively, modulo $23$.  Thus $23$ is absent from the least common
clearing denominator of the pair.

The role of positivity in this example is exact: it follows from
(21)--(22), not from a grid evaluation, floating-point optimization, or
an extrapolation from finite data.

## 6. The ratio-four family has no one-third window

For completeness, let



$$
\begin{aligned}
 H(x)={}&2x^8-4x^7+7x^6-8x^5+7x^4-4x^3+x^2.
                                                               \tag{27}
\end{aligned}
$$



The preceding package proved exactly that



$$
H\in\mathbb Z[x],\quad H\equiv1\pmod {u^2},\quad
 0\leq H\leq1,\quad \operatorname {ord}_0H=2,\quad\deg H=8.
                                                               \tag{28}
$$



Since $H$ has nonzero lowest and highest coefficients, for every
$k\geq1$,



$$
\operatorname {ord}_0H^k=2k,\qquad\deg H^k=8k.           \tag{29}
$$



It follows identically that



$$
\frac{\deg H^k}{3}=\frac{8k}{3}>2k
                         =\operatorname {ord}_0H^k.       \tag{30}
$$



Thus there is no prime, or even a real number, in the interval tested by
(3).  Finite denominator scans of $H^k$ cannot repair this structural
absence.

## 7. Exact scope of the barrier

The counterexample proves that the even-localizer prime-window theorem
cannot be extended to arbitrary positive localizers simply by replacing
the isolated $I_0$ argument with the pair $(I_0,I_1)$.  At $p=23$,
the odd high coefficient cancels the forced $I_0$ residue and the even
high coefficient cancels the $I_1$ residue simultaneously.

It does not prove any of the following:

* that many primes in $d/3<p<n$ can cancel for one $h$;
* that the product of the surviving primes lacks an exponential lower
  bound;
* that a third moment or the full correction channel cannot recover the
  missing prime;
* that positive localizers with degree/order ratio at least three evade
  every denominator obstruction; or
* any arithmetic classification of $e+\pi$.

A stronger result now needs an aggregate restriction on the exceptional
congruences (6), or a new channel which couples the even and odd high
coefficients.  Prime-by-prime survival from positivity and $u^2$
divisibility alone is false.

## 8. Replay and status

From the research directory run

    python3 scripts/common_kernel_nonsymmetric_two_moment_residue_certificate.py
    sha256sum -c results/common_kernel_nonsymmetric_two_moment_residue_hashes.sha256

The deterministic replay constructs (7) by exact polynomial arithmetic,
checks both $u^2$-congruences, verifies (10)--(11), recomputes the
reduced fractions (26), and checks the exact degree/order identities for
$H^k$.  Finite auxiliary instances only check normalization; the
general criterion (4) and positivity statements are proved above.

The computation uses exact integer/rational CPU arithmetic, no hardware
accelerator, and only a negligible fraction of the available Colab RAM.
No claim about $e+\pi$ is made.
