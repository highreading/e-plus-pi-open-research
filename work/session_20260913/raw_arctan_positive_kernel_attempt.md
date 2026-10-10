> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A positive kernel for the whole raw-arctangent remainder, and its exact cancellation obstruction

Date: 2026-09-13. Bounded analytic continuation after the all-degree
dyadic denominator theorem. No new degree scan was performed.

## 1. What was already known and what is new

The canonical raw family is



$$
R_n=A_n+B_ne^z+C_n\arctan z=O(z^{3n+1}),\quad
 \deg A_n,\deg B_n,\deg C_n\le n,\quad C_n(1)=4B_n(1).
\tag{1}
$$



The projection and whole-integral construction below are for n>=1.
The separate n=0 triple is (-1,1,4); it has no high moment rows and must
not be inserted into (8). This restriction has no effect on any
asymptotic statement.

The archive's `sources/raw_arctan_endpoint_remainder.md` already gives
the whole endpoint as the sum of an exponential integral with an
(1-x)^(2n) factor and an arctangent integral with an x^(2n) factor. It
also gives a Taylor integral and an exact contour formula. Those formulas
contain varying polynomial factors with no proved sign. The old
unnormalized height bound cannot be compared directly with their tails.

I also revisited the research-log derivation and the Chebyshev and
Wronskian obstruction notes. Their explicit counterexamples concern
Machin or Möbius pullbacks, not the raw family; they must not be promoted
to counterexamples for (1). They do rule out importing those proposed
uniform-positive-kernel arguments unchanged. The failure of a first-free-
coefficient sign test likewise provides no whole-remainder asymptotic.

The new dyadic theorem `raw_arctan_endpoint_dyadic_attempt.md` proves
uniqueness, nonzero B_n(1), and pairwise distinct endpoint rationals. At
most one evaluated form can vanish. The present task is therefore
quantitative, not merely a nonvanishing test.

This note proves a new **single real integral for the entire remainder**,



$$
\boxed{R_n(1)=\int_0^1 P_{B_n}(x)G_n(x)\,dx,\qquad G_n(x)>0,}
\tag{2}
$$



where the kernel is explicit, independent of the chosen matched B_n, and
satisfies the uniform exponential asymptotic



$$
\boxed{\sup_{0\le x\le1}\left|
    \frac1n\log G_n(x)-\log(\sqrt2-1)\right|\longrightarrow0.}
\tag{3}
$$



There is an exact obstruction to interpreting (2) as a positive integral:
the multiplying polynomial P_B must change sign on (0,1) for every n>=2.
Its signed cancellation against G_n is not controlled by (3).
Consequently this note does not obtain a whole-remainder asymptotic or
primitive shrinking. Section7 isolates the remaining quantitative term.

## 2. Raw Legendre projection and the exact remainder

Use the raw moment functional and its monic orthogonal polynomials



$$
\mathcal L(P)=\frac12\int_{-1}^1P(iu)\,du,
 \qquad Q_k(t)=\frac{2^ki^k}{\binom{2k}{k}}P_k(-it),
\tag{4}
$$



where P_k on the right is the ordinary Legendre polynomial. Write



$$
h_k=\mathcal L(Q_k^2)
 =\frac{(-1)^k2^{2k}}{(2k+1)\binom{2k}{k}^2},
 \qquad
 K_n(t,s)=\sum_{k=0}^n\frac{Q_k(t)Q_k(s)}{h_k}.
\tag{5}
$$



Then arctan(z)=z L((1-tz)^(-1)), and



$$
Q_{k+1}=tQ_k+\beta_kQ_{k-1},\qquad
 \beta_k=\frac{k^2}{4k^2-1}\in(1/4,1/3].
\tag{6}
$$



Every nonzero coefficient of Q_k is positive, and its powers have the
parity of k. This follows immediately by induction in (6).

Define the rational factorial functionals



$$
\ell_{n,j}(t^d)=\frac1{(n+d+1-j)!},\quad0\le j\le n,
 \qquad\ell_B=\sum_{j=0}^nB_j\ell_{n,j}.
\tag{7}
$$



The same exact moment reduction as in the Möbius note, now with (4), gives



$$
C^*(t)=-\ell_B^{(s)}K_n(t,s),\quad C^*(t)=t^nC(1/t),
\tag{8}
$$





$$
\ell_B(Q_k)=0\quad(k=n+1,\ldots,2n-1),\qquad
 4B(1)+\ell_B(K_n(1,t))=0.
\tag{9}
$$



Let h(t)=1/(1-t), H_n=L_s(K_n(t,s)h(s)), and Psi_n=h-H_n. Then



$$
\boxed{R_n(1)=\ell_B(\Psi_n).}
\tag{10}
$$



Indeed the exponential tail after degree n is ell_B(h). The logarithmic
tail is L(C^*h), which is -ell_B(H_n) by (8). For the raw arctangent,
the endpoint power series can be justified by an Abel limit, while the
moment integral itself is regular because 1-iu never vanishes. The
factorial-weighted sums in (10) converge absolutely.

Put



$$
v_k=\mathcal L\left(\frac{Q_k(t)}{1-t}\right),\qquad a_n=v_{n+1}/v_n.
$$



The ordinary Legendre-square identity gives sign(v_k)=(-1)^k. For example,
orthogonality gives



$$
v_k=\frac1{Q_k(1)}\mathcal L\left(\frac{Q_k(t)^2}{1-t}\right),
$$



and after t=iu the real part of the integrand has the strict sign (-1)^k.
In particular a_n<0 and v_n/h_n>0. Christoffel–Darboux gives exactly



$$
\Psi_n(t)=\frac{v_n}{h_n}
 \frac{S_n(t)}{1-t},\qquad S_n(t)=Q_{n+1}(t)-a_nQ_n(t).
\tag{11}
$$



Here S_n has positive coefficients in both parities, including a strictly
positive constant term. This S_n is unrelated to the factorial-valuation
sum denoted S in the arithmetic note.

## 3. Beta integration gives a single real integral

For a polynomial B of degree at most n, define



$$
P_B(x)=\sum_{j=0}^n B_j\frac{(1-x)^{n-j}}{(n-j)!}.
\tag{12}
$$



This is an invertible rational change of polynomial coordinates. Its
inverse is B_(n-k)=(-1)^k P_B^(k)(1).

Let the Borel transform of a power series f=sum f_dt^d be



$$
\mathcal Bf(x)=\sum_{d\ge0}f_d\frac{x^d}{d!}.
$$



The beta integral proves the exact identity



$$
\ell_B(f)=\int_0^1P_B(x)\mathcal Bf(x)\,dx,
\tag{13}
$$



whenever the displayed series is absolutely integrable, because



$$
\frac1{d!(n-j)!}\int_0^1x^d(1-x)^{n-j}\,dx
  =\frac1{(n+d+1-j)!}.
$$



Apply this to f=Psi_n and set G_n=B(Psi_n). Equations (10) and (13) prove
the whole-remainder identity (2). This is not an identity for just the
first unconstrained coefficient or for one part of the old two-integral
formula.

## 4. The kernel is a positive convex mixture of exponential tails

Write S_n(t)=sum_(d=0)^(n+1)s_dt^d. Define



$$
w_{n,d}=\frac{v_n}{h_n}s_d>0,
 \quad
 \mathcal T_d(x)=\sum_{r=d}^{\infty}\frac{x^r}{r!},
 \quad\mathcal T_0(x)=e^x.
$$



Then (11) gives



$$
\boxed{G_n(x)=\sum_{d=0}^{n+1}w_{n,d}\mathcal T_d(x),
       \qquad\sum_{d=0}^{n+1}w_{n,d}=1.}
\tag{14}
$$



To verify the normalization, integrate the Christoffel–Darboux kernel
against the constant polynomial: L(K_n(t,1))=1. It gives
v_n Q_(n+1)(1)-v_(n+1)Q_n(1)=h_n, which is exactly sum_d w_(n,d)=1.
Equivalently, Psi_n=h-H_n has the same pole coefficient at t=1 as h.

Every weight is strictly positive because the two consecutive Q's cover
both parities, and a_n is strictly negative. In particular



$$
0<w_{n,0}e^x\le G_n(x)\le e^x\quad(0\le x\le1).
\tag{15}
$$



This representation also makes all interchanges in (13) immediate:
G_n is entire, and on [0,1] its positive Taylor series is bounded by e.

## 5. A uniform exponential estimate for the actual kernel

The sharper comparison needed for (3) is



$$
\boxed{w_{n,0}\le G_n(x)
 \le3e\,w_{n,0}\exp(2\sqrt{2(n+1)})
       \quad(0\le x\le1,\ n\ge1).}
\tag{16}
$$



Here are coefficient details ensuring that the estimate does not assume
uniformity from pointwise asymptotics.

The second-kind recurrence obtained from (6), shifted once, gives



$$
|a_n|=\frac{\beta_{n+1}}{1+|a_{n+1}|},\qquad
 3/16<|a_n|<1/3.
\tag{17}
$$



The upper bound follows first because the denominator exceeds1. The lower
bound then uses beta>1/4 and the same upper bound at n+1.

Rodrigues' formula is



$$
Q_k(t)=\frac{k!}{(2k)!}\frac{d^k}{dt^k}(1+t^2)^k.
\tag{18}
$$



For even k, comparison of its coefficient of t^d, d even, with its
constant coefficient gives



$$
\frac{[t^d]Q_k}{Q_k(0)}
 =\frac{\binom{k}{(k+d)/2}}{\binom{k}{k/2}}
   \frac{(k+d)!}{k!d!}
 \le\frac{(2k)^d}{d!}.
\tag{19}
$$



For odd k, the analogous comparison with its linear coefficient is



$$
\frac{[t^d]Q_k}{[t]Q_k}\le\frac{(2k)^{d-1}}{d!}
 \quad(d\text{ odd},\ d\ge1).
\tag{20}
$$



The neighboring lowest coefficients obey the exact identities, for odd k,



$$
\frac{Q_k'(0)}{Q_{k-1}(0)}=\frac{k^2}{2k-1},\qquad
 \frac{Q_k'(0)}{Q_{k+1}(0)}=2k+1.
\tag{21}
$$



These follow by the same factorial comparison in (18); the second also
follows from Q_(k+1)(0)=beta_k Q_(k-1)(0).
Combining (17)–(21), separately according to n's parity, yields the safe
single bound



$$
\frac{s_d}{s_0}\le3\frac{(2(n+1))^d}{d!}
 \quad(0\le d\le n+1).
\tag{22}
$$



For instance the ratio of the linear coefficient to the constant is at
most 6(n+1); the even coefficients use (19), and the odd coefficients
then use (20).

For 0<=x<=1, the elementary factorial inequality (d+r)!>=d!r! gives
T_d(x)<=e^x x^d/d!. Also



$$
\sum_{d\ge0}\frac{z^d}{(d!)^2}\le e^{2\sqrt z}\quad(z\ge0),
$$



since binom(2d,d)<=4^d bounds this series by cosh(2sqrt(z)). Equations
(14) and (22) prove (16).

Finally put eta=sqrt2-1. The contractive backward recurrence (17), with
beta_k->1/4, proves |a_n|->eta/2. To see this without assuming a terminal
condition, iterate any fixed number of steps, use the uniform derivative
bound 1/3 and (17), then let the number of steps tend to infinity.
Consequently |v_n|^(1/n)->eta/2. The norm recurrence or (5) gives
|h_n|^(1/n)->1/4. The positive even constants
Q_(2m)(0)=product_(j=1)^m beta_(2j-1) have (2m)-th root tending to1/2.
The constant coefficient s_0 is either one such constant or |a_n| times
one, so s_0^(1/n)->1/2. Therefore



$$
w_{n,0}^{1/n}\longrightarrow\eta.
\tag{23}
$$



The uniform O(sqrt(n)) logarithmic loss in (16) proves (3).

## 6. A forced sign change and an exact positivity obstruction

When n>=2, equation (9) includes ell_B(Q_(n+1))=0. By (13),



$$
\int_0^1P_B(x)\mathcal BQ_{n+1}(x)\,dx=0.
\tag{24}
$$



The weight BQ_(n+1)(x) is strictly positive on (0,1), since its nonzero
coefficients are positive. The polynomial P_B is nonzero because
B(1) is nonzero. Thus P_B takes both positive and negative values in
(0,1). This is an all-degree obstruction to treating (2) as an integral
of one sign; it is not a sign pattern inferred from a finite example.

The factorial functional itself also cannot be silently replaced by a
positive measure on a real interval. Already



$$
\det\begin{pmatrix}\ell_{n,0}(1)&\ell_{n,0}(t)\\
 \ell_{n,0}(t)&\ell_{n,0}(t^2)\end{pmatrix}
 =-\frac1{(n+3)((n+2)!)^2}<0.
\tag{25}
$$



A positive real measure must have a positive semidefinite moment matrix.
Thus a proposed common-positive-measure proof for these factorial moments
violates an exact two-by-two test. The Borel-beta representation avoids
that error by leaving the sign-changing polynomial factor explicit.

## 7. The remaining analytic term, with primitive normalization retained

Normalize the actual matched solution by B_n(1)=1 and hence C_n(1)=4.
Let P_n be (12) in this fixed scale, let q_n be the fully reduced endpoint
denominator, and define



$$
M_n=\int_0^1|P_n(x)|\,dx>0,
 \qquad
 \theta_n=
 \frac{\left|\int_0^1P_n(x)G_n(x)\,dx\right|}
      {\int_0^1|P_n(x)|G_n(x)\,dx}\in[0,1].
\tag{26}
$$



At most one theta_n is zero by the already proved distinctness theorem.
But that theorem supplies no quantitative lower bound on positive theta_n.
The exact norm ledger supplied by (16) is



$$
w_{n,0}M_n\le\int_0^1|P_n|G_n
 \le3e\,e^{2\sqrt{2(n+1)}}w_{n,0}M_n.
\tag{27}
$$



Thus, away from the possible single zero, the primitive endpoint form
L_n=q_n R_n(1) satisfies the rigorous decomposition



$$
\boxed{\log|L_n|
  =\log q_n+n\log\eta+\log M_n+\log\theta_n+o(n).}
\tag{28}
$$



The o(n) term here is proved and comes only from (16) and (23). The two
quantities M_n and theta_n are deliberately retained, not estimated by
heuristics. The system determining them is concrete: P_n has degree n,
is orthogonal to BQ_(n+1),...,BQ_(2n-1), and satisfies the exact endpoint
condition in (9), with
B(1)=sum_(k=0)^n(-1)^kP_n^(k)(1)=1.

The next useful analytic lemma would control the signed integral in (26)
for this particular polynomial system, or equivalently its cancellation
relative to M_n. A uniform kernel asymptotic alone cannot freeze P_n
inside the integral: its degree grows, its sign changes are forced, and
no uniform slow-variation bound has been proved. Likewise
v_2(q_n)=n+2floor((n+2)/4) determines only the dyadic factor, not the full
q_n in (28).

Accordingly, the positive kernel and its exponent are rigorous progress,
but the whole-remainder asymptotic and primitive shrinking remain open.
No irrationality conclusion is drawn from (2), (3), or eventual
nonvanishing alone.

Selected exact algebraic controls are saved in
`raw_arctan_positive_kernel_checks.py` and its JSON output. They verify
the convex-weight normalization, the projection coefficients, beta/Borel
moments, and the constant/e/pi components of the whole integral at three
selected degrees with arbitrary test B. They do not solve new matched
matrices and do not establish the asymptotic claims; Sections4–5 do that.
