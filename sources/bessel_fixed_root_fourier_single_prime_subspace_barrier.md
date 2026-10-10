> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A fixed Bessel root, critical-Fourier matching, and the single-prime support barrier

Checked: 2026-08-27 UTC.

## 1. Verdict

Let $p$ be one fixed odd prime.  Suppose, conditionally, that an
ordinary $p$-adic Bessel-index root produces even integers $n\to\infty$
for which



$$
a_n=v_p(q_n),\qquad
 a_n\log p=n\log n-o(n\log n).
\tag{1}
$$



For the ordinary root $\rho_{p,r}$, the accepted index-interpolation
theorem gives $a_n=v_p(n-\rho_{p,r})$ exactly.  Thus (1) is precisely
the hypothetical main-scale digit-depth outcome of the live Bessel
survivor, not an unrelated support assumption.

Since $\log q_n=n\log n+O(n)$, this says exactly that



$$
q_n=p^{a_n}u_n,\qquad \log u_n=o(n\log n),
\tag{2}
$$



where $u_n=(q_n)_{\{p\}^c}$.  This is the strongest conceivable
fixed-root support outcome at the scale relevant to the archive.

It does **not** put the fully matched critical-Fourier forms into the
fixed-support Subspace criterion.  In fact, the exact matching algebra
and a fixed-prime bound for the Fourier denominator show that this
particular conversion cannot work.

Let



$$
\mathcal L_{n,k}=A_{n,k}+B_{n,k}\pi>0,
 \qquad \gcd(A_{n,k},B_{n,k})=1,\qquad B_{n,k}>0
\tag{3}
$$



be the primitive critical-Fourier $\pi$-form, and match it with



$$
E_n=q_ne-r_n>0,\qquad\gcd(r_n,q_n)=1.
\tag{4}
$$



Here $r_n$ denotes the beta-form numerator; it is not the fixed prime
$p$.  After minimal matching and complete primitive reduction, write



$$
\Lambda_{n,k}=Q_{n,k}(e+\pi)-P_{n,k}>0,
 \qquad \gcd(P_{n,k},Q_{n,k})=1.
\tag{5}
$$



In every critical window



$$
0<c_-\leq\frac{k}{n\log n}\leq c_+<\infty,
\tag{6}
$$



the following statements hold.

1. The fixed-prime valuation of the primitive Fourier coefficient obeys

   

$$
\boxed{
   v_p(B_{n,k})\log p
   \leq\frac n2\log(8(k-1))+O_p(\log k).}
   \tag{7}
$$



   In particular,

   

$$
v_p(B_{n,k})\log p
   \leq\left(\frac12+o(1)\right)n\log n.
   \tag{8}
$$


2. Equations (1) and (8) make the exponent resonance
   $v_p(B_{n,k})=a_n$ impossible.  The exact matching localization then
   gives $p\nmid g_{n,k}$, and positivity plus the Fourier lower bound
   gives

   

$$
\boxed{
   \Lambda_{n,k}\geq
   \frac{\mathcal L_{n,k}}{u_n}
   =\exp\bigl(k\log2-o(n\log n)\bigr)
   \longrightarrow+\infty.}
   \tag{9}
$$


3. A singleton fixed-support Subspace inequality for a primitive pair
   necessarily implies $\Lambda_{n,k}\ll Q_{n,k}^{-\eta}$ for some
   $\eta>0$.  Therefore (9) rules it out.

The accepted unconditional low- and very-high matching theorems cover
$k=o(n\log n)$ and $k$ above every fixed slope greater than
$(1/\log2)n\log n$, respectively.  Together with (7)--(9), they leave
no choice of $k>n$ through which a main-scale fixed ordinary root can
be converted into the required fixed-$\{p\}$ primitive approximants by
this fully matched critical-Fourier construction.

The outside-$p$ parts of both final coefficients are nevertheless
displayed exactly below.  They show why denominator concentration in
$q_n$, without the new fixed-prime Fourier bound (7), would not by
itself have verified the Subspace criterion.

This is a conditional no-go theorem for the stated construction.  It does
not prove that a main-scale root exists, does not cover a different
matching family, and does not prove any arithmetic classification of
$e+\pi$.

## 2. Exact primitive matching

Suppress $(n,k)$ temporarily and write



$$
q=q_n,\quad r=r_n,\quad A=A_{n,k},\quad B=B_{n,k}.
\tag{12}
$$



Put



$$
d=\gcd(q,B),\qquad q=dq_0,\qquad B=dB_0.
\tag{13}
$$



The same-sign minimal match is



$$
W=B_0E_n+q_0\mathcal L_{n,k}.
\tag{14}
$$



Its constant and common target coefficients are



$$
M=q_0A-B_0r,\qquad C=\frac{qB}{d}=dq_0B_0.
\tag{15}
$$



Reduction modulo every prime divisor of $q_0B_0$, using
$\gcd(r,q)=\gcd(A,B)=1$, gives



$$
\gcd(M,q_0B_0)=1.
\tag{16}
$$



Consequently the complete content is exactly



$$
\boxed{g=\gcd(M,C)=\gcd(M,d),}
\tag{17}
$$



and the final primitive pair is



$$
\boxed{
 Q=\frac{qB}{dg},\qquad P=-\frac M g.}
\tag{18}
$$



If $M=0$, equation (16) forces $q_0B_0=1$, after which primitive
reduction gives $Q=1$.  Such a case cannot occur in an unbounded-height
approximating sequence.  Hence all valuation formulas below may, and do,
assume $M\ne0$.

For a genuine approximation to $e+\pi>0$, one necessarily has
$M<0$ eventually, so $P>0$.  The value and projective error have the
content-invariant identities



$$
\begin{aligned}
 \Lambda
 &=\frac Wg
 =Q(e+\pi)-P,\\
 \frac\Lambda Q
 &=\frac{E_n}{q}+\frac{\mathcal L_{n,k}}B.
\end{aligned}
\tag{19}
$$



Both summands in (19) are positive.  There is no hidden cancellation
between the exponential and Fourier approximation errors.

## 3. Exact $p$-adic dichotomy and both outside parts

Write



$$
q=p^a u,\qquad B=p^b v,\qquad p\nmid uv,
\tag{20}
$$



and put



$$
\delta=\min(a,b),\qquad
 d=p^\delta d_0,\qquad d_0=\gcd(u,v).
\tag{21}
$$



Let



$$
m=v_p(M),\qquad t=\min(m,\delta),\qquad
 g=p^t g_0,\qquad p\nmid g_0.
\tag{22}
$$



Equation (17) gives



$$
g_0=\gcd\left(\frac{|M|}{p^m},d_0\right),
 \qquad g_0\mid d_0.
\tag{23}
$$



The final valuations are therefore



$$
\boxed{
 v_p(Q)=\max(a,b)-t,\qquad
 v_p(P)=m-t.}
\tag{24}
$$



If $a\ne b$, then in fact $m=t=0$.  Indeed, if $a>b$, then
$q_0$ is divisible by $p$ while $B_0r$ is a unit; if $b>a$,
then $B_0$ is divisible by $p$ while $q_0A$ is a unit.  Thus



$$
a\ne b
 \quad\Longrightarrow\quad
 v_p(Q)=\max(a,b),\qquad v_p(P)=0.
\tag{25}
$$



If $a=b$, there are exactly two branches:



$$
\begin{array}{c|c|c|c}
 \text{condition}&t&v_p(Q)&v_p(P)\\ \hline
 m<a&m&a-m&0\\
 m\geq a&a&0&m-a.
\end{array}
\tag{26}
$$



Thus the main $p$-power either remains in the denominator, or exact
exponent resonance plus a normalized congruence removes it completely;
only excess congruence beyond level $a$ can then put a $p$-power in
the numerator.

Most importantly, (18), (20)--(23) give both outside parts exactly:



$$
\boxed{
 (Q)_{\{p\}^c}=\frac{uv}{d_0g_0},
 \qquad
 (P)_{\{p\}^c}=\frac{|M|/p^m}{g_0}.}
\tag{27}
$$



Hence



$$
\boxed{
 (P)_{\{p\}^c}(Q)_{\{p\}^c}
 =\frac{(|M|/p^m)uv}{d_0g_0^2}.}
\tag{28}
$$



Condition (1) controls only $u$.  It supplies no bound for $v$ or
$|M|/p^m$.  Formula (28) is the exact reason denominator concentration
in $q_n$ cannot be substituted for a support theorem for the final
primitive pair.

## 4. A singleton-support lemma

The fixed-support criterion in

    sources/padic_subspace_prime_support_transcendence_criterion.md

requires, for some fixed $\eta>0$,



$$
|\Lambda|
 (P)_{\{p\}^c}(Q)_{\{p\}^c}
 \leq Q^{1-\eta}.
\tag{29}
$$



For a primitive pair, at least one of $P,Q$ is a $p$-adic unit.  If
(29) holds along $Q\to\infty$, its outside factors are at least one,
so



$$
\left|e+\pi-\frac PQ\right|
 =\frac{|\Lambda|}{Q}\leq Q^{-\eta}.
\tag{30}
$$



Thus $P/Q\to e+\pi$, and eventually $|P|\geq(e+\pi)Q/2$.  If
$p\nmid P$, the first outside factor is $|P|$; if $p\nmid Q$, the
second outside factor is $Q$.  In either case



$$
(P)_{\{p\}^c}(Q)_{\{p\}^c}\gg Q.
\tag{31}
$$



Combining (29) and (31) proves the necessary decay



$$
\boxed{|\Lambda|\ll Q^{-\eta}.}
\tag{32}
$$



This point is special to support supplied by one prime.  Primitivity
prevents that same prime from carrying large powers in both coefficients.
Therefore a divergent or bounded-away-from-zero primitive matched form
cannot be rescued by a main-scale fixed $p$-power in $q_n$.

Positivity in (19) makes the requirement still more explicit:



$$
\boxed{
 \frac{E_n}{q}\ll Q^{-1-\eta},
 \qquad
 \frac{\mathcal L_{n,k}}B\ll Q^{-1-\eta}.}
\tag{33}
$$



Both component approximations must be sufficiently strong relative to
the *final* matched height.

## 5. Nonresonance forces divergence

Assume (1)--(2) and the critical window (6).  The accepted all-degree
Fourier estimate gives, uniformly in this window when the rational
Fourier coordinate is nonzero,



$$
\log\mathcal L_{n,k}
 \geq k\log2-o(n\log n).
\tag{34}
$$



This is the leading-scale consequence of the explicit bound



$$
\begin{aligned}
 \log\mathcal L_{n,k}
 &\geq(k-n/2-1)\log2-3\log(k-1)\\
 &\quad +(n+1)\left(\frac12\log\frac nk-\log4\right)
 -n\sqrt{\frac nk}-O(n).
\end{aligned}
\tag{35}
$$



Now suppose $a\ne b$.  By (25), $p\nmid g$, while
$d_0g_0\leq u^2$.  Therefore



$$
\frac{q_0}{g}
 =\frac{p^{a-\delta}u}{d_0g_0}
 \geq\frac1u.
\tag{36}
$$



Equations (14), (34), and positivity give



$$
\boxed{
 \Lambda\geq\frac{q_0\mathcal L_{n,k}}g
 \geq\frac{\mathcal L_{n,k}}u
 =\exp\bigl(k\log2-o(n\log n)\bigr).}
\tag{37}
$$



Under (6), the last expression tends to infinity.  This proves the first
part of the verdict.  If the rational Fourier coordinate is zero, then
$(A,B)=(0,1)$ and the matched form is
$q_n(e+\pi)-r_n$, which also diverges.  Thus zero coordinate does not
create an exception.

## 6. A fixed-prime bound for the Fourier coefficient

The crude archimedean bound for $C_0$ is not sharp enough for its
valuation at one fixed prime.  The exact super-Catalan representation
does give the needed estimate.

Put



$$
n=2r,\qquad K=k-1\geq2r,
\tag{38}
$$



and define



$$
\mathcal S(x,y)=\frac{(2x)!(2y)!}{x!y!(x+y)!}.
\tag{39}
$$



The accepted full-period calculation gives



$$
C_0=\sum_{j=0}^{r}\binom{2r}{2j}
 \mathcal S(r+j,K-r-j).
\tag{40}
$$



The quotient of the $j$-th super-Catalan term by the $j=0$ term is



$$
\frac{\mathcal S(r+j,K-r-j)}{\mathcal S(r,K-r)}
 =\prod_{s=0}^{j-1}
 \frac{2r+1+2s}{2K-2r-1-2s}.
\tag{41}
$$



Set



$$
D_r(K)=\prod_{s=0}^{r-1}
 \bigl(2K-(2r+1+2s)\bigr)
\tag{42}
$$



and



$$
\begin{aligned}
 F_r(K)
 =\sum_{j=0}^{r}\binom{2r}{2j}
 &\prod_{s=0}^{j-1}(2r+1+2s)\\
 &\times\prod_{s=j}^{r-1}
 \bigl(2K-(2r+1+2s)\bigr).
\end{aligned}
\tag{43}
$$



Equations (40)--(43) give the exact identity



$$
\boxed{
 C_0=\mathcal S(r,K-r)\frac{F_r(K)}{D_r(K)}.}
\tag{44}
$$



All factors in (42)--(43) are positive because $K\geq2r$.  Every
product in a summand of (43) has exactly $r$ factors, each at most
$2K$.  Since the sum of the even binomial coefficients is
$2^{2r-1}$,



$$
0<F_r(K)
 \leq2^{2r-1}(2K)^r
 <(8K)^r.
\tag{45}
$$



Let $s_p(x)$ denote the sum of the base-$p$ digits of $x$.
Legendre's formula, with the linear factorial terms cancelling, gives



$$
\begin{aligned}
 v_p\bigl(\mathcal S(r,K-r)\bigr)
 &=\frac{s_p(r)+s_p(K-r)+s_p(K)}{p-1}\\
 &\quad-\frac{s_p(2r)+s_p(2K-2r)}{p-1}\\
 &\leq3\bigl(1+\lfloor\log_pK\rfloor\bigr).
\end{aligned}
\tag{46}
$$



Because $D_r(K)$ is an integer, (44)--(46) imply



$$
v_p(C_0)\log p
 \leq r\log(8K)
 +3\bigl(1+\lfloor\log_pK\rfloor\bigr)\log p.
\tag{47}
$$



Finally, the exact primitive Fourier coefficient is



$$
B=\frac{L_KC_0}{h},\qquad
 L_K=\operatorname {lcm}(1,\ldots,K).
\tag{48}
$$



Since $v_p(L_K)=\lfloor\log_pK\rfloor$, equations (47)--(48) prove the
fully explicit bound



$$
\boxed{
 v_p(B)\log p
 \leq\frac n2\log(8K)
 +4\bigl(1+\lfloor\log_pK\rfloor\bigr)\log p.}
\tag{49}
$$



This is (7).  Under the critical-window hypothesis (6),
$\log K=\log n+O(\log\log n)$, so (49) is



$$
v_p(B)\log p
 \leq\frac12n\log n+O(n\log\log n).
\tag{50}
$$



The main-scale Bessel hypothesis (1) is twice as large at leading order.
Therefore $v_p(B)\ne a_n$ eventually, and Section 5 applies.

## 7. Consequence for support and exact scope

Formula (28) remains exact: the fixed-root hypothesis controls only the
outside part $u$ of $q_n$, not the outside part $v$ of $B$ or the
outside part $|M|/p^m$ of the matched constant.  Thus root depth alone
is not a fixed-support theorem for both primitive coefficients.

The new point is that (49) rules out exponent resonance altogether in
the critical window.  Hence $m=t=0$ by (25), and (37) makes
$\Lambda$ diverge.  Section 4 then contradicts the necessary decay for
singleton support.  No estimate of the remaining outside factors is
needed for this no-go.

The accepted generalized odd-prime-band theorem gives divergence for
$n<k\leq(3/10)n\log n$, and the very-high theorem gives divergence for
all sufficiently large $n$ whenever
$k\geq c n\log n$ with fixed $c>1/\log2$.  Choose any fixed compact
critical window that fills the gap between these two ranges.  Sections
5--6 handle that window.  Thus every choice $k>n$ is covered for all
sufficiently large $n$, even if $k/(n\log n)$ oscillates.

This note uses the singleton support set $\{p\}$, because that is the
support concentration supplied by one fixed ordinary root.  Enlarging it
to a fixed set $\mathcal S\supsetneq\{p\}$ requires a new support
theorem at every added prime; the singleton lower bound (31) need not
survive.  The conclusion is also specific to the fully matched
critical-Fourier family.  It is not a no-go for every possible auxiliary
construction.

## 8. Dependencies and exact certificate

The matching identities (13)--(19) and the localization
$g=\gcd(M,d)$ are the accepted theorems in

    sources/critical_fourier_odd_matching_gcd_localization.md

The Fourier bounds (34)--(35), the super-Catalan identity (40), and the
outer-range matching theorems are proved in

    sources/independent_critical_fourier_two_adic_closure.md
    sources/critical_fourier_pnt_matching_extension.md
    sources/critical_fourier_generalized_odd_prime_bands.md
    sources/critical_fourier_very_high_matching_closure.md

The fixed-support input (29) is Theorem 4.1 of

    sources/padic_subspace_prime_support_transcendence_criterion.md

The companion script

    scripts/bessel_fixed_root_fourier_single_prime_certificate.py

checks the exact primitive formulas (17)--(18), the valuation dichotomy
(24)--(26), and both outside-part formulas (27)--(28) over exhaustive
finite boxes and the archived critical-Fourier warning cases.  It also
checks the singleton outside-product inequality and, over an independent
finite box, the factorization (44), positivity bound (45), digit-sum
formula (46), and resulting valuation inequalities.  These are finite
diagnostics; the all-degree and asymptotic deductions are the symbolic
proofs in Sections 4--7.

Run

    python -m py_compile scripts/bessel_fixed_root_fourier_single_prime_certificate.py
    python scripts/bessel_fixed_root_fourier_single_prime_certificate.py

For byte-identical replay, use

    python scripts/bessel_fixed_root_fourier_single_prime_certificate.py \
      --output /tmp/bessel_fixed_root_fourier_single_prime_certificate.json
    cmp results/bessel_fixed_root_fourier_single_prime_certificate.json \
      /tmp/bessel_fixed_root_fourier_single_prime_certificate.json
