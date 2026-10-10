> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The neighboring quartic powers: exact beta periods and the saddle-phase barrier

Date: 2026-08-27.

## 1. Scope and conclusion

For even `n`, put



$$
P_n(x)=x^n(1-x)^n,\qquad Q(x)=1+x^4,\qquad
 J_{n,k}=\int_0^1\frac{P_n(x)}{Q(x)^k}\,dx .             \tag{1}
$$



Let



$$
J_{n,k}=R_{n,k}+\frac{L_{n,k}}{2\sqrt2}\log(1+\sqrt2)
 +\left(\frac{E_{n,k}}{4\sqrt2}+\frac{b_{n,k}}8\right)\pi
                                                                  \tag{2}
$$



be the Hermite coordinates from the quartic-power reduction, so that
`L=a-c` and `E=a+c`.  When `k>n/2`, the `log 2` coordinate is zero.  The
neighboring determinant



$$
\mathcal K_{n,k}=L_{n,k+1}J_{n,k}-L_{n,k}J_{n,k+1}               \tag{3}
$$



therefore cancels the only remaining logarithm.

This note first proves three new facts about (3), and then a fourth fact
about three adjacent powers.

1.  Both `L` and `E` have exact beta-integral representations.  The `E`
    integral is positive and has the large real `1+y` saddle.  The `L`
    integral is the real part of an oscillatory integral and has a
    different, accessible complex saddle.  The superficially larger
    `1+y` saddle does **not** contribute to `L`.

2.  At the critical scale `k/n -> infinity`, including
    `k ~ c n log n`, the neighboring determinant does not cancel the
    complex saddle.  Its exact leading multiplier is

    

$$
-(1+i)r^5+O(r^6),\qquad r=(4k/n)^{-1/4}.                    \tag{4}
$$



    After taking the real part, however, the leading term contains
    `cos(Theta+pi/4)`.  Thus the complex amplitude is nonzero, but its
    leading real saddle projection has zeros when the power is varied as a
    continuous parameter; this statement alone does not locate an exact
    zero of (3).

3.  In every fixed critical window
    `c_1 n log n <= k <= c_2 n log n`, consecutive phases have mesh
    `r^5(1+o(1))`.  Short windows of length comparable with `r^{-5}` can
    select a power for which the determinant has its full saddle size.
    Conversely, the same mesh also gives powers within `O(r^5)` of a zero
    of the leading real saddle projection, where an extra factor `O(r^5)`
    is lost.  This does not assert a zero of the exact determinant.  Hence no
    all-power lower bound by a fixed positive multiple of the saddle
    envelope can be true.

4.  Three adjacent powers remove this phase obstruction.  Uniformly at the
    critical scale,

    

$$
L_{n,k+1}^2-L_{n,k}L_{n,k+2}>0.
$$



    This produces an exact integer quadratic $P(Q)>0$ whose three-power
    integral is log-free and positive.  A symmetrized version has positive
    $\pi$-coefficient $B$ and satisfies $\Lambda/B\to2\pi$.  Thus
    the new positive branch has no analytic smallness after its
    $\pi$-coefficient is normalized; only a separate, exceptionally
    large primitive-content effect could rescue it for coefficient matching.

The dyadic denominator of the surviving square-root `pi` coordinate is
given exactly in terms of an adjacent integer Wronskian.  The stable
valuation seen in the companion finite scan would leave essentially the
full doubled denominator, but that valuation is not proved here.  More
importantly, a lower bound at *every integer power* strong enough to rule
out exponentially close approaches to the moving zeros of the complete
real saddle expansion would require
an arithmetic phase-separation theorem not supplied by steepest descent.
Thus the two-neighbor route is narrowed to one precise unresolved issue.
The three-neighbor construction bypasses that issue but reaches the
scale-invariant analytic obstruction in (66).  Neither result classifies
`e+pi`.

## 2. Exact beta-integral coordinates

For `m>=0` and `k>=1`, set



$$
A_{m,k}=\frac{((3-m)/4)_{k-1}}{(k-1)!}.                         \tag{5}
$$



If `m` is even and `k>(m+1)/4`, reflection for the gamma function and
Euler's beta integral give



$$
\begin{aligned}
 A_{m,k}
 &=\frac{\sin(\pi(3-m)/4)}{\pi}
   B\!\left(\frac{m+1}{4},k-\frac{m+1}{4}\right)\\
 &=\frac{4\sin(\pi(3-m)/4)}{\pi}
   \int_0^\infty\frac{y^m}{(1+y^4)^k}\,dy .                     \tag{6}
 \end{aligned}
$$



The second line follows from `t=y^4/(1+y^4)` and has no branch choice:
all powers in its integrand are ordinary real powers.

For a monomial `x^m`, let `lambda_m` and `mu_m` denote respectively its
contributions to `a-c` and `a+c` after reduction modulo `x^4+1`.  For even
`m`, direct inspection of the four residue classes gives



$$
\begin{aligned}
 \lambda_m\sin\frac{\pi(3-m)}4
    &=\frac{\sqrt2}{2}(-1)^{m/2},\\
 \mu_m\sin\frac{\pi(3-m)}4
    &=\frac{\sqrt2}{2}.                                         \tag{7}
 \end{aligned}
$$



When `n` is even, only even binomial indices contribute to `a` and `c`,
and their signs `(-1)^j` are then one.  Substituting (6)--(7) in the exact
Hermite sum and using



$$
\sum_{j\ {\rm even}}\binom nj(-1)^{j/2}y^j
       =\operatorname {Re}(1+iy)^n,
 \quad
 \sum_{j\ {\rm even}}\binom njy^j
       =\frac{(1+y)^n+(1-y)^n}{2},                               \tag{8}
$$



proves the following exact identities.

**Proposition 2.1.**  If `n` is even and `k>(2n+1)/4`, then



$$
\boxed{
 L_{n,k}=(-1)^{n/2}\frac{2\sqrt2}{\pi}
 \operatorname {Re} I_{n,k},\qquad
 I_{n,k}=\int_0^\infty
 \frac{[y(1+iy)]^n}{(1+y^4)^k}\,dy }                            \tag{9}
$$



and



$$
\boxed{
 E_{n,k}=\frac{\sqrt2}{\pi}\int_0^\infty
 \frac{y^n\big((1+y)^n+(1-y)^n\big)}{(1+y^4)^k}\,dy>0.}        \tag{10}
$$



At infinity the integrands are `O(y^(2n-4k))`, so the displayed
condition is exactly sufficient for absolute convergence.  In particular,
it holds throughout the neighboring-power range `k>n/2`.

There is also an exact coefficient version.  For every quartic root
`alpha^4=-1`,



$$
\omega_{n,k}(\alpha)
 =[z^{k-1}](1-z)^{-3/4}
   [\alpha(1-z)^{1/4}]^n
   [1-\alpha(1-z)^{1/4}]^n.                                  \tag{11}
$$



Here (11) is an identity of the power series at `z=0`, with the branch
`(1-z)^(1/4)=1+O(z)`.  It follows immediately from
`A_{m,k}=[z^(k-1)](1-z)^((m-3)/4)` and the binomial theorem.  The four-point
DFT recovers `a,b,c,d`.  Formula (9), rather than an inadmissible rotation
through a pole of `1+y^4`, identifies the saddle which actually contributes
to `L`.

## 3. An exact double integral for the neighboring determinant

Put



$$
F_{n,k}(x)=\frac{[x(1-x)]^n}{(1+x^4)^k},\qquad
 H_{n,k}(y)=\frac{[y(1+iy)]^n}{(1+y^4)^k}.                       \tag{12}
$$



Equations (1), (3), and (9), followed only by Fubini (absolute convergence
holds), give



$$
\boxed{
 \begin{aligned}
 \mathcal K_{n,k}
 &=(-1)^{n/2}\frac{2\sqrt2}{\pi}
   \operatorname {Re}\int_0^\infty\!\int_0^1
   H_{n,k}(y)F_{n,k}(x)\\
 &\qquad\qquad\times
 \frac{x^4-y^4}{(1+x^4)(1+y^4)}\,dx\,dy .                       \tag{13}
 \end{aligned}}
$$



Thus the adjacent operation inserts `x^4-y^4`; it does not make the
two saddle fourth powers equal.

## 4. Uniform saddles when `k/n` tends to infinity

Write



$$
\kappa=\frac{k}{n},\qquad r=(4\kappa)^{-1/4}.                   \tag{14}
$$



After `x=ru` or `y=ru`, define



$$
\begin{aligned}
 \psi_-(u;r)&=\log u+\log(1-ru)
 -\frac1{4r^4}\log(1+r^4u^4),\\
 \psi_i(u;r)&=\log u+\log(1+iru)
 -\frac1{4r^4}\log(1+r^4u^4).                                 \tag{15}
 \end{aligned}
$$



The logarithms in (15) are local analytic logarithms near `u=1`.  The
integrands themselves are single-valued rational functions because all
exponents are integers.

For sufficiently small positive `r`, `psi_-` has one real critical point
`u_-(r)` near one, while `psi_i` has one critical point `u_i(r)` near one.
The analytic implicit-function theorem and direct substitution give



$$
\begin{aligned}
 u_-&=1-\frac r4-\frac9{32}r^2-\frac14r^3
       +\frac{247}{2048}r^4+O(r^5),\\
 u_i&=1+\frac{i r}{4}+\frac9{32}r^2-\frac{i}{4}r^3
       +\frac{247}{2048}r^4+O(r^5),                             \tag{16}
 \end{aligned}
$$



and



$$
\begin{aligned}
 \psi_-(u_-;r)
 &=-\frac14-r-\frac38r^2-\frac7{96}r^3+\frac14r^4+O(r^5),\\
 \psi_i(u_i;r)
 &=-\frac14+i r+\frac38r^2-\frac{7i}{96}r^3
    +\frac14r^4+O(r^5),                                        \tag{17}\\
 -\psi_-''(u_-;r)&=4-r+\frac14r^2+\frac{61}{32}r^3+O(r^4),\\
 -\psi_i''(u_i;r)&=4+i r-\frac14r^2+\frac{61i}{32}r^3+O(r^4).
 \end{aligned}
$$



**Lemma 4.1 (uniform saddle formula).**  If `n -> infinity` and `r -> 0`,
then, uniformly in such pairs,



$$
\begin{aligned}
 J_{n,k}
 &=r^{n+1}e^{n\psi_-(u_-;r)}
   \sqrt{\frac{2\pi}{-n\psi_-''(u_-;r)}}
   \left(1+O(n^{-1})\right),\\
 I_{n,k}
 &=r^{n+1}e^{n\psi_i(u_i;r)}
   \sqrt{\frac{2\pi}{-n\psi_i''(u_i;r)}}
   \left(1+O(n^{-1})\right).                                  \tag{18}
 \end{aligned}
$$



The square root in the second formula is the analytic branch which is
positive at `r=0`.

Here is a self-contained contour justification.  At `r=0`, both scaled
phases reduce to `log u-u^4/4`, with a unique nondegenerate saddle at one.
On a fixed rectangle around `[1/2,2]`, all zeros of `1+r^4u^4` and the
zero of `1+iru` have modulus `1/r`, and hence lie outside the rectangle.
The analytic Morse lemma gives a steepest arc through `u_i(r)` which is an
`O(r)` perturbation of the central real segment.  Continue this arc until
it meets the two fixed vertical lines through `1-delta` and `1+delta`, and
join those points to the real axis by vertical segments of length `O(r)`.
This gives a homotopy with fixed endpoints contained in the pole-free
rectangle; in particular, no quartic pole is crossed and no infinite ray
is rotated.  Because the connectors are `O(r)`-close to the two real
endpoints, continuity from `r=0` preserves the fixed negative phase gap
there.  Away from a fixed neighborhood of the saddle, the unchanged real
pieces have the same gap.  More
quantitatively, on the undeformed real ray the absolute-amplitude maximum
is



$$
-\frac14+\frac12r^2+O(r^4),
$$



whereas the contributing saddle has real action



$$
\operatorname {Re}\psi_i(u_i;r)
 =-\frac14+\frac38r^2+O(r^4).
$$



At the fixed scaled boundaries $u=1/2,2$, the limiting phase
$\log u-u^4/4$ lies below $-1/4$ by a fixed positive constant.
Consequently both tails, not merely their pointwise absolute maximum, are
$O(e^{-c n})$ relative to the contributing complex saddle after
monotonicity and the final power-law integration at infinity are applied.
Locally,
the analytic Morse coordinate gives the Gaussian and a uniform complete
expansion, whose first relative error is `O(1/n)`.

It remains only to bound the un-deformed tails.  In the scaled variable put



$$
h_r(u)=\log u+\frac12\log(1+r^2u^2)
 -\frac1{4r^4}\log(1+r^4u^4).
$$



The derivative of the logarithm of the absolute value of the original `I`
integrand has, after positive factors are removed, the sign of



$$
1+2t+(1-4\kappa)t^2+(2-4\kappa)t^3,\qquad t=y^2.                \tag{19}
$$



For `kappa>1/2`, Descartes' rule gives exactly one positive root.  Thus the
absolute amplitude has one maximum, at `y/r=1+O(r^2)`, and is uniformly
below its maximum at the two boundaries `u=1/2,2`.  On `2<=u<=1/r` one has



$$
u h_r'(u)
 =1+\frac{r^2u^2}{1+r^2u^2}
   -\frac{u^4}{1+r^4u^4}
 \leq2-u^4/2\leq-6.                                         \tag{19a}
$$



This integrates the intermediate upper tail while retaining the fixed
phase gap at `u=2`.  For the remaining ray `y>=1`, write



$$
H(y)=\log y+\frac12\log(1+y^2)-\kappa\log(1+y^4).
$$



Then



$$
yH'(y)
 =1+\frac{y^2}{1+y^2}-4\kappa\frac{y^4}{1+y^4}
 \leq2-2\kappa,
$$



and therefore



$$
\int_1^\infty e^{nH(y)}\,dy
 \leq \frac{2^{n/2-k}}{2k-2n-1}.                           \tag{19b}
$$



Relative to the saddle term in (18), the logarithm of this bound is



$$
-k\log2+\frac{n+1}{4}\log(4k/n)+O(n+\log k),
$$



which tends to `-infinity` faster than a fixed negative multiple of `n`
as `r -> 0`.  The lower tail is handled by monotonicity up to `u=1/2` and
the fixed boundary gap.  Thus both tails are exponentially smaller than
the complex saddle with the required uniformity.  The real integral `J`
is the usual one-saddle Laplace argument.  This proves (18) without
rotating an infinite ray through any root of `1+y^4`.

Define



$$
x_-=r u_-(r),\qquad y_i=r u_i(r),\qquad
 \Theta_{n,k}=n\operatorname {Im}\psi_i(u_i;r)
 -\frac12\arg(-\psi_i''(u_i;r)).                              \tag{20}
$$



Then



$$
\Theta_{n,k}=n\left(r-\frac7{96}r^3+O(r^5)\right)
 -\frac r8+O(r^3).                                             \tag{21}
$$



## 5. The adjacent saddle multiplier

Apply the same saddle expansion with the analytic amplitude
`1/(1+z^4)`.  Uniformly as above,



$$
\frac{J_{n,k+1}}{J_{n,k}}
 =\frac1{1+x_-^4}+O(n^{-1}),\qquad
 \frac{I_{n,k+1}}{I_{n,k}}
 =\frac1{1+y_i^4}+O(n^{-1}).                                \tag{22}
$$



From (16),



$$
\begin{aligned}
 \frac1{1+y_i^4}&=1-r^4-ir^5-\frac34r^6
                    +\frac{7i}{32}r^7+O(r^8),\\
 \frac1{1+x_-^4}&=1-r^4+r^5+\frac34r^6
                    +\frac7{32}r^7+O(r^8).                    \tag{23}
 \end{aligned}
$$



Consequently the complex adjacent multiplier is



$$
\boxed{D_-(r)=\frac1{1+y_i^4}-\frac1{1+x_-^4}
 =-(1+i)r^5-\frac32r^6+\frac7{32}(-1+i)r^7+O(r^8),}            \tag{24}
$$



and is nonzero for every sufficiently small `r`.

Let



$$
\mathcal I_{n,k}=r^{n+1}e^{n\operatorname {Re}\psi_i(u_i;r)}
 \left|\sqrt{\frac{2\pi}{-n\psi_i''(u_i;r)}}\right|.          \tag{25}
$$



If additionally `n r^5 -> infinity` (true for `k ~ c n log n`), then
(3), (18), and (22)--(24) give the rigorous leading formula



$$
\boxed{
 \mathcal K_{n,k}
 =(-1)^{n/2}\frac{2\sqrt2}{\pi}J_{n,k}\mathcal I_{n,k}
 \left[-\sqrt2 r^5\cos\left(\Theta_{n,k}+\frac\pi4\right)
 +O\left(r^6+n^{-1}\right)\right].}                           \tag{26}
$$



Thus the adjacent operation retains the saddle with a nonzero complex
multiplier.  It does **not**, however, turn the real form positive.

For comparison, the positive coordinate `E` is dominated by the `1+y`
part of (10).  Its saddle `u_+(r)=u_-(-r)` has exponent



$$
\psi_+(u_+;r)=-\frac14+r-\frac38r^2+\frac7{96}r^3
 +\frac14r^4+O(r^5).                                         \tag{27}
$$



The square-root part of the `pi` coefficient in (3) is



$$
B^{(\sqrt2)}_{n,k}
 =\frac{L_{n,k+1}E_{n,k}-L_{n,k}E_{n,k+1}}8.                  \tag{28}
$$



Its corresponding complex saddle multiplier is



$$
D_+(r)=\frac1{1+y_i^4}-\frac1{1+x_+^4}
 =(1-i)r^5-\frac32r^6+O(r^7).                               \tag{29}
$$



The real projections in (24) and (29) are in quadrature.  Near a leading
zero of (26), the surviving square-root `pi` coefficient (28) has its full
leading size.  This is analytically consistent with the stable nonzero
adjacent determinants in the finite exact scan.

## 6. Phase selection and the obstruction to an all-power lower bound

Extend `k` temporarily to a positive real parameter in the convergent
integrals.  Differentiating the saddle action, or taking the argument in
the second ratio of (22), gives



$$
\Theta_{n,k+1}-\Theta_{n,k}=-r^5+O(r^6+n^{-1}).                \tag{30}
$$



The same statement holds for the derivative with respect to continuous
`k`, with unit increment replaced by differentiation.  The derivative of
the argument of `D_-(r)` is smaller by a factor `1/n`.  Hence the complete
leading phase in (26) is strictly decreasing for all sufficiently large
critical parameters.

Fix `0<c_1<c_2`.  In the window



$$
c_1n\log n\leq k\leq c_2n\log n,                              \tag{31}
$$



the total phase variation is



$$
n(4\log n)^{-1/4}
 \big(c_1^{-1/4}-c_2^{-1/4}+o(1)\big),                         \tag{32}
$$



which tends to infinity, while the phase mesh between consecutive integer
powers is `r^5(1+o(1))`, which tends to zero.

It follows by the intermediate value theorem and rounding that:

* every block of `C r^{-5}` consecutive powers, for a sufficiently large
  absolute `C`, contains an integer power with
  `|cos(Theta+pi/4)|>=1/2`; at that power (26) is a two-sided saddle lower
  bound of order `J Ical r^5`;
* throughout (31), there are integer powers within phase distance
  `O(r^5)` of a zero of the leading real saddle projection.  At those powers,

  

$$
|\mathcal K_{n,k}|
     \leq C J_{n,k}\mathcal I_{n,k}
          (r^{10}+r^6+n^{-1}).                                \tag{33}
$$



The `r^6` in (33) is only the truncation error of the displayed multiplier.
If the exact analytic phase `arg D_-(r)` is used instead of its first term,
the same argument removes it and gives `O(r^10+n^{-1})`.  Either version
rigorously refutes a fixed-positive-envelope lower bound that is uniform in
all powers.

The phase-selection lemma is useful in both directions.  It gives abundant
subsequences on which a conventional saddle lower bound is rigorous.  It
also shows why such a bound cannot settle an adversarial choice of the
neighboring power: exponentially precise separation of an integer `k`
from the moving continuous zeros is an arithmetic problem, not a missing
term in Laplace's method.

## 7. Exact dyadic bookkeeping and the remaining content question

Let



$$
d_k=3(k-1)-s_2(k-1),\qquad
 D_k=2^{d_k}.                                                   \tag{34}
$$



The exact monomial denominator theorem gives `D_k` as a common denominator
of `a,b,c,d`.  Let `A_k,C_k` be the raw integer numerators of `a,c` on the
larger denominator `4^(k-1)(k-1)!`, and divide each by the odd part of
`(k-1)!`, obtaining integers `tilde A_k,tilde C_k`.  Put



$$
T_{n,k}=2(\widetilde A_{k+1}\widetilde C_k
             -\widetilde C_{k+1}\widetilde A_k).               \tag{35}
$$



Equations (28) and `L=a-c,E=a+c` give the exact identity



$$
B^{(\sqrt2)}_{n,k}=\frac{T_{n,k}}{2^{d_k+d_{k+1}+3}}.          \tag{36}
$$



Therefore, if `T` is nonzero, the reduced dyadic denominator exponent of
this coordinate is exactly



$$
\delta_{n,k}=d_k+d_{k+1}+3-v_2(T_{n,k}).                      \tag{37}
$$



No odd content can alter (37).  The companion exact scan found



$$
v_2(T_{n,k})=
 \begin{cases}
 n/2+2+v_2(n/4),&4\mid n,\\
 n/2+1,&n\equiv2\pmod4,
 \end{cases}                                                   \tag{38}
$$



for every tested pair, with no zero.  Formula (38) is still a finite-scan
conjecture, not a theorem in this note.  If it holds in the critical
range, then



$$
\delta_{n,k}=6k-O(n+\log k),                                 \tag{39}
$$



so essentially the full doubled dyadic denominator survives even at the
powers where the analytic value is near a phase zero.  Since the raw saddle
envelopes in (18) have logarithm only `O(n log log n)` at
`k ~ c n log n`, while (39) has logarithm
`(6c log 2+o(1))n log n`, ordinary saddle cancellation by any fixed or
polylogarithmic factor cannot make the primitive form vanish.

What remains open is precisely the conjunction of two possible exceptional
effects:

1. an integer power can in principle lie exponentially close to a moving
   real zero of the complete oscillatory expansion; and
2. without an all-parameter proof of (38), unexpectedly large dyadic
   numerator content has not been excluded.

The exact identities and the saddle theorem reduce the neighboring quartic
route to those arithmetic questions.  They do not classify `e+pi`.

## 8. Three adjacent powers remove the phase obstruction

The oscillatory obstruction in (26) is special to a two-term determinant.
Three adjacent powers have a phase-independent Hankel minor.

### 8.1 Uniform positivity of the Hankel minor

For brevity write



$$
L_s=L_{n,k+s}\quad(0\leq s\leq2),\qquad
 \mathscr D_{n,k}=L_1^2-L_0L_2.                              \tag{40}
$$



Let



$$
g_i=\frac1{1+y_i^4}=\rho e^{i\eta}.
$$



Applying the uniform saddle expansion with the fixed analytic amplitudes
$(1+y^4)^{-s}$, for $s=0,1,2$, gives one common complex number
$Z_{n,k}$, with $|Z_{n,k}|=\mathcal I_{n,k}$, such that



$$
I_{n,k+s}=Z_{n,k}\left(g_i^s+O(n^{-1})\right)                 \tag{41}
$$



uniformly for these three values of $s$.  If
$Z_{n,k}=M e^{i\theta}$, the elementary identity



$$
\begin{aligned}
 &\big(\operatorname {Re}(Zg_i)\big)^2
 -\operatorname {Re}(Z)\operatorname {Re}(Zg_i^2)\\
 &\hspace{35mm}=M^2\rho^2\sin^2\eta                         \tag{42}
 \end{aligned}
$$



is independent of $\theta$.  Equations (9), (23), and (41)--(42)
therefore prove



$$
\boxed{
 \mathscr D_{n,k}=\frac8{\pi^2}\mathcal I_{n,k}^2\rho^2
 \left(r^{10}+O(r^{12}+n^{-1})\right).}                       \tag{43}
$$



Here $\eta=-r^5+O(r^7)$.  We have proved the following all-parameter
asymptotic theorem.

**Theorem 8.1.**  If $n$ is even, $k/n\longrightarrow\infty$, and



$$
n r^{10}\longrightarrow\infty,
 \qquad r=(4k/n)^{-1/4},                                      \tag{44}
$$



then $\mathscr D_{n,k}>0$ for all sufficiently large $n$.  In
particular this holds uniformly when



$$
c_1n\log n\leq k\leq c_2n\log n
$$



for fixed $0<c_1<c_2$.  Unlike (26), this conclusion is uniform in the
oscillatory phase.

### 8.2 An exact positive rational kernel

The direct squared construction is



$$
(L_2Q-L_1)^2+\mathscr D_{n,k}>0.                             \tag{45}
$$



Its coefficients obey



$$
L_2^2L_0-2L_1L_2L_1+(2L_1^2-L_0L_2)L_2=0,                  \tag{46}
$$



so the three-power combination



$$
L_2^2J_{n,k}-2L_1L_2J_{n,k+1}
 +(2L_1^2-L_0L_2)J_{n,k+2}                                  \tag{47}
$$



is exactly log-free and positive.  All its coefficients are rational;
no quadratic coefficient field is necessary.

There is a substantially smaller integer construction.  Clear the three
rational numbers $L_0,L_1,L_2$ to a primitive integer vector



$$
(a,b,c),\qquad H=\max(|a|,|b|,|c|).                         \tag{48}
$$



Then $b^2-ac>0$.  Put



$$
f(t)=a-2bt+ct^2.                                            \tag{49}
$$



If $c=0$, the third power is already log-free and the constant
polynomial $P(Q)=1$ suffices.  Suppose $c\ne0$.  Between the two real
roots of (49), one has $cf(t)<0$.

The saddle model gives a quantitative version of this interval.  For the
unperturbed three cosines in (42), the roots are



$$
t_\pm=
 \frac{\cos(\theta+\eta)\mathbin\pm|\sin\eta|}
      {\rho\cos(\theta+2\eta)}.                              \tag{50}
$$



At least one of them satisfies



$$
|\rho t_\pm-1|\leq2|\eta|.                                 \tag{51}
$$



Indeed, write $A=\theta+2\eta$ and choose the sign in (50) for which
$|\sin A\mathbin\pm1|\leq|\cos A|$; the assertion follows after
expanding $\cos(A-\eta)$.  The limiting cases $\cos A=0$ follow by
continuity.  At either model root the derivative of the model quadratic
has magnitude exactly $2\rho|\sin\eta|$.  The absolute $O(M/n)$
errors in (41) therefore move the bounded root by
$O((n|\eta|)^{-1})=o(|\eta|)$ under (44).  The exact root interval has
length at least a fixed multiple of $|\eta|$: after the common scale is
removed, (43) bounds its discriminant below by a multiple of $\eta^2$,
while its quadratic coefficient is uniformly bounded above.

Starting at the bounded root furnished by (51), move into the exact root
interval by distances between two fixed small multiples of $|\eta|$.
This gives a closed subinterval of length $c_0|\eta|$, lying strictly
between the roots and at distance at least $c_0|\eta|$ from each endpoint.
It is contained in a fixed bounded interval.  A uniform rational grid
provides coprime integers $u,v$, with



$$
t=\frac uv,\qquad 1\leq v\leq C|\eta|^{-1},\qquad |u|\leq Cv, \tag{52}
$$



such that $t$ lies in this subinterval.  Now set



$$
(C_0,C_1,C_2)=
 \operatorname {sgn}(c)\,(cv,-2cu,-av+2bu).                  \tag{53}
$$



Then



$$
aC_0+bC_1+cC_2=0                                            \tag{54}
$$



and the integer quadratic



$$
\begin{aligned}
 P(Q)&=C_0Q^2+C_1Q+C_2\\
 &=\operatorname {sgn}(c)v\big(c(Q-t)^2-f(t)\big)>0
 \qquad(Q\in\mathbb R).                                     \tag{55}
 \end{aligned}
$$



Moreover,



$$
\max_j|C_j|\leq C H|\eta|^{-1}=O(Hr^{-5}),                 \tag{56}
$$



and if $A=|c|v$ is its leading coefficient and $m$ its minimum,



$$
\frac mA=-\frac{f(t)}c\geq c_1\eta^2.                      \tag{57}
$$



Dividing (53) by its integer content preserves strict positivity and can
only improve (56).  This explicit cone-lattice lemma avoids the square of
the logarithmic-coordinate height in (45).

Define



$$
\Lambda_{n,k}(P)=\sum_{s=0}^2C_sJ_{n,k+s}
 =\int_0^1\frac{P_n(x)P(1+x^4)}{(1+x^4)^{k+2}}\,dx.           \tag{58}
$$



Equations (54)--(55) prove that this is an exactly log-free, strictly
positive form.  Its $\pi$-coefficient is nonzero.  To see this without
any independence conjecture, integrate the proper rational differential
in (58) over the whole real line.  For even $n$ its integrand is positive
there.  In a Hermite reduction the exact rational part can be chosen proper,
so its values at both infinities vanish.  The odd reduced terms integrate
to zero, and hence



$$
\int_{-\infty}^{\infty}
 \frac{P_n(x)P(1+x^4)}{(1+x^4)^{k+2}}\,dx
 =\frac\pi{\sqrt2}E(P)>0,                                   \tag{59}
$$



where $E(P)$ is the combined $a+c$ coordinate.  Therefore
$E(P)>0$, and the $\pi$-coordinate cannot vanish.

### 8.3 A symmetric positive form and a scale-invariant obstruction

Half-line integration of an unsymmetrized Hermite form includes a rational
endpoint jump; it is generally false that it equals twice the displayed
$\pi$-coordinate.  Symmetrization removes this defect.  Put



$$
F(x)=\frac{x^n(1-x)^nP(1+x^4)}{(1+x^4)^{k+2}}
$$



and



$$
\Lambda^{\rm sym}_{n,k}
 =\int_0^1(F(x)+F(-x))\,dx
 =\int_{-1}^{1}F(x)\,dx.                                    \tag{60}
$$



The odd Hermite coordinates cancel.  The logarithmic coordinate is twice
the already vanishing one, and the $\pi$-coefficient is



$$
B^{\rm sym}_{n,k}=\frac{E(P)}{2\sqrt2}>0.                   \tag{61}
$$



Equation (59) now gives the exact, scaling-invariant identity



$$
\boxed{
 \frac{\Lambda^{\rm sym}_{n,k}}{B^{\rm sym}_{n,k}}
 =2\pi\,
 \frac{\int_{-1}^{1}F(x)\,dx}
      {\int_{-\infty}^{\infty}F(x)\,dx}.}                    \tag{62}
$$



The quotient of integrals tends to one at the critical scale.  Here is a
uniform proof.  If the exceptional case $c=0$ in Section 8.2 occurs, then
the chosen kernel is $P(Q)=1$ and the next bound is immediate.  Otherwise,
(55)--(57) give, for $Q\geq1$,



$$
\frac{P(Q)}{\min_{\mathbb R}P}
 \leq1+C\eta^{-2}(1+Q^2).                                  \tag{63}
$$



The negative half of the main interval contains the positive saddle of



$$
\frac{[y(1+y)]^n}{(1+y^4)^{k+2}},
$$



at $y=r(1+O(r))<1$.  Its logarithm is
$-\frac n4\log(4k/n)+O(n)$.  For $y\geq1$, on the other hand,



$$
y\frac d{dy}
 \left(\log y+\log(1+y)-\frac kn\log(1+y^4)\right)
 \leq2-2k/n<0.                                               \tag{64}
$$



Equations (63)--(64), with the harmless two powers of $Q$ in (63)
absorbed by the denominator, give



$$
\frac{\int_{|x|>1}F(x)\,dx}{\int_{-1}^{1}F(x)\,dx}
 \leq \eta^{-2}\exp\left(
  -(k-n)\log2+\frac n4\log(4k/n)+O(n)\right)=o(1)            \tag{65}
$$



uniformly in every fixed critical window.  Therefore



$$
\frac{\Lambda^{\rm sym}_{n,k}}{B^{\rm sym}_{n,k}}
 =2\pi(1+o(1)).                                               \tag{66}
$$



This is a rigorous analytic no-go for the new positive branch: after
normalizing its $\pi$-coefficient to one, its value is bounded away from
zero and in fact tends to $2\pi$.  If it is coefficient-matched with the
positive exponential form $E_n=q_ne-p_n$ before arithmetic content is
removed, the same-sign matched value is at least
$(2\pi-o(1))q_n$.  A claim about the *fully primitive* matched algebraic
integer still has to account for a possible common coefficient ideal; the
ratio (66) shows exactly that any rescue would have to come from such
arithmetic content, not from analytic smallness or saddle cancellation.

### 8.4 Why a leading-phase Baker bound does not finish two powers

The critical points, their multipliers, and their Hessians are algebraic of
bounded degree.  The leading phase can be written as a fixed-length product
of algebraic numbers raised to the integer powers $n$ and $k$.  A
linear-form-in-logarithms estimate can therefore separate a *nonzero*
leading projection from zero by a subfactorial bound.  This observation
does not by itself lower-bound the exact two-power determinant: the first
omitted saddle coefficient is only relatively $O(1/n)$, much larger than
the generic explicit Baker lower bound, and equality of the leading
algebraic projection must also be treated separately.  One would need a
rigorous high-order, exponentially accurate expansion together with
uniform height control for its growing truncations.  The three-power minor
(43) avoids that issue entirely.

## 9. Reproducible certificate

Run

    python -m py_compile scripts/quartic_neighbor_saddle_phase_certificate.py
    python scripts/quartic_neighbor_saddle_phase_certificate.py

For a byte-identical rerun, pass an output path under `/tmp` and compare it
with the frozen JSON.  The script verifies the beta-coordinate identities
against the independent Hermite sums, the exact two- and three-power
determinant formulas, all displayed saddle series, the multiplier
expansions, the phase mesh, the positive integer-kernel construction, and
the dyadic identity (36).  Its bounded valuation, Hankel-sign, and phase
scans are diagnostics only; the all-parameter assertions used above are
proved in the text.
