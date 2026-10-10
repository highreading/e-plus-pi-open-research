> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Higher determinants of the reduced beta ratios meet a multiplicity barrier

## Exact Dirichlet modes, optimal linear cancellation, and the surviving arithmetic escape

Checked: 2026-08-27 UTC

## 1. Scope and conclusion

Let



$$
r_N=\frac{P_N}{Q_N}
     =\frac{|E_{2N+2}|}{(2N+2)(2N+1)|E_{2N}|},
 \qquad \gcd(P_N,Q_N)=1,                                  \tag{1}
$$



where reduction of the raw quotient is understood, and put



$$
\alpha=\frac4{\pi^2}.              \tag{2}
$$



The preceding beta-denominator theorem proves that $r_N$ is strictly
decreasing to $\alpha$, and that its first error mode is



$$
r_N-\alpha
 =\frac {32}{27\pi^2}\,9^{-N}
    \left(1+O((9/25)^N)\right).                            \tag{3}
$$



This note investigates whether higher Vandermonde, Hankel, divided-
difference, continued-fraction, or simultaneous-ratio constructions can
upgrade the resulting $O(N)$ denominator floor to the $N\log N$
scale needed for the quadratic primitive-content problem.

The rigorous answer for the canonical constructions is negative.

1. The exact Dirichlet-mode expansion of $r_N$ is obtained in Section 2.
2. Among all linear forms in $h$ consecutive ratios that annihilate the
   constant mode, the unique filter that postpones the first surviving
   mode as far as possible reaches $(2h-1)^{-2}$.  Its analytic gain per
   denominator copy is

   

$$
\frac{2\log(2h-1)}h\leq\log3,             \tag{4}
$$



   with equality only at $h=2$, the original adjacent construction.
3. The all-size Vandermonde construction has an exact denominator floor
   of order $h(N+h)$, hence only order $N+h$ per distinct denominator.
   Its uniform analytic asymptotic contains no missing $\log(N+h)$.
4. A fixed $h\times h$ Hankel determinant is eventually nonzero, but
   its first $h$ Dirichlet modes produce only
   $2N\sum_{j<h}\log(2j+1)$ decay while its universal monomial clearing
   has exactly $h^2$ denominator copies.
5. Simultaneous higher Euler ratios telescope to products of the original
   $r_N$'s.  Their determinant has the same analytic gain and a clearing
   with exactly $h(h-1)$ copies.
6. Ordinary Hankel total positivity is false: an explicit $3\times3$
   principal minor is negative.  Thus a positive Stieltjes continued
   fraction cannot repair the multiplicity ledger.

These statements are a **canonical denominator-multiplicity no-go**, not
a classification of every nonlinear construction.  Two possibilities are
left open: nonvanishing of growing-size signed Hankel determinants, and a
large arithmetic cancellation in the actual least common denominator or
the cleared integer numerator.  Either would require information about
the correlations among the $Q_N$'s that is absent from the analytic beta
tail.  No result here proves $\log G_N=o(N\log N)$, and nothing here
classifies $e+\pi$.

## 2. The exact signed Dirichlet-mode expansion

Let $\chi=\chi_4$ be the primitive character modulo 4.  For
$\Re s>1$,



$$
\frac{\beta(s+2)}{\beta(s)}
 =\prod_{p\ {\rm odd}}
     \frac{1-\chi(p)p^{-s}}{1-\chi(p)p^{-s-2}}
 =\sum_{q\ {\rm odd}}c_q q^{-s}.                          \tag{5}
$$



The coefficients are multiplicative, $c_1=1$, and



$$
c_{p^a}=-\chi(p)^a\frac{p^2-1}{p^{2a}}
 \qquad(p\ {\rm odd\ prime},\ a\geq1).                    \tag{6}
$$



Thus, if $q>1$ is odd,



$$
c_q=(-1)^{\omega(q)}\chi(q)
       \frac{\prod_{p\mid q}(p^2-1)}{q^2},
 \qquad
 b_q:=\frac{c_q}{q}\ne0.                                  \tag{7}
$$



Put $b_1=1$ and $\lambda_q=q^{-2}$.  Equations (1), (2), and (5)
give the absolutely convergent expansion



$$
\boxed{
 r_N=\alpha\sum_{q\ {\rm odd}} b_q\lambda_q^N
 \qquad(N\geq1).}                                        \tag{8}
$$



The elementary estimate



$$
|b_q|\leq\frac1q                       \tag{9}
$$



will be useful below.  The first two nonconstant coefficients already
have opposite signs:



$$
b_3=\frac8{27},\qquad
                    b_5=-\frac {24}{125}.                  \tag{10}
$$



This signed measure, rather than a positive Hausdorff measure, is the
basic obstruction to a mechanical total-positivity argument.

## 3. The optimal consecutive linear filter

Fix $h\geq2$, set $q_h=2h-1$, and define the primitive integer
polynomial



$$
A_h(X)=(X-1)\prod_{j=1}^{h-2}\bigl((2j+1)^2X-1\bigr)
       =\sum_{\ell=0}^{h-1}a_{h,\ell}X^\ell.               \tag{11}
$$



Its constant coefficient is $(-1)^{h-1}$, so its coefficients have no
common divisor.  Consider



$$
L_{N,h}=\sum_{\ell=0}^{h-1}
                               a_{h,\ell}r_{N+\ell}.        \tag{12}
$$



Substitution of (8) gives the exact response formula



$$
L_{N,h}=\alpha\sum_{q\ {\rm odd}}
             b_q\lambda_q^N A_h(\lambda_q).                \tag{13}
$$



The modes $q=1,3,\ldots,2h-3$ vanish.  The first surviving coefficient
is nonzero, and for each fixed $h$,



$$
\boxed{
 L_{N,h}=\alpha b_{q_h}A_h(q_h^{-2})q_h^{-2N}
 \left(1+O_h\left(((q_h)/(q_h+2))^{2N}\right)\right).}    \tag{14}
$$



In particular, $L_{N,h}\ne0$ for all sufficiently large $N$.  The
leading factor is completely explicit:



$$
|A_h(q_h^{-2})|
 =\left(1-q_h^{-2}\right)
   \frac{4^{h-2}(h-2)!(2h-2)!}{h!\,q_h^{\,2h-4}}.          \tag{15}
$$



The coefficient height is also explicit.  Put



$$
B_h=\prod_{j=1}^{h-2}(2j+1)^2.
$$



All coefficients in (11) alternate in sign, and hence



$$
\boxed{
 B_h\leq H(A_h)\leq\|A_h\|_1
 =2\prod_{j=1}^{h-2}(1+(2j+1)^2)
 \leq2^{h-1}B_h.}                                         \tag{15a}
$$



Consequently,



$$
\log H(A_h)=2h\log h+O(h).           \tag{15b}
$$



Thus taking $h\asymp N$ already imports coefficient height of order
$\exp(\Theta(N\log N))$; the exact cancellation below does not make
those coefficients arithmetically free.

There is also an all-parameter upper bound, with no fixed-$h$
asymptotic assumption.  For every odd $q\geq q_h$, every factor in
$|A_h(q^{-2})|$ is at most 1.  Equations (9) and (13) therefore give



$$
\boxed{
 |L_{N,h}|\leq
 \alpha q_h^{-2N}\left(\frac1{q_h}+\frac1{2N}\right).}    \tag{16}
$$



Here the sum over odd $q$ was enlarged to all integers and bounded by
its first term plus an integral.

There is a completely explicit certified nonvanishing range.  Since


$$
|b_{q_h}|\geq q_h^{-3},\qquad
 |A_h(q_h^{-2})|
 \geq\frac89\left(\frac2{5\mathrm e}\right)^{h-2},         \tag{16a}
$$


while the tail after $q_h$ is at most
$\alpha(q_h+2)^{-2N}$.  Explicitly,


$$
\sum_{q\geq q_h+2\atop q\ {\rm odd}}q^{-(2N+1)}
 \leq(q_h+2)^{-(2N+1)}
     +\int_{q_h+2}^{\infty}x^{-(2N+1)}\,dx
 \leq(q_h+2)^{-2N}.                                       \tag{16b}
$$


Define


$$
N_0(h)=1+\left\lceil\frac{q_h+2}{4}
 \left(
 3\log q_h+(h-2)\log\frac{5\mathrm e}{2}+\log\frac98
 \right)\right\rceil.                                     \tag{16c}
$$


Then the leading term in (14) strictly dominates the entire remaining
tail for every


$$
N\geq N_0(h),                     \tag{16d}
$$


so $L_{N,h}\ne0$ and has the sign of
$b_{q_h}A_h(q_h^{-2})$ throughout that range.  To prove (16a), use
$1-q_h^{-2}\geq8/9$,


$$
1-\frac{(2j+1)^2}{q_h^2}\geq\frac{2(h-j-1)}{q_h},
$$


$(h-2)!\geq((h-2)/\mathrm e)^{h-2}$, and
$q_h\leq5(h-2)$ for $h\geq3$; the case $h=2$ has an empty product.
Finally,
$\log(1+2/q_h)\geq2/(q_h+2)$ gives (16c)--(16d).
In particular $N_0(h)=O(h^2)$.  This supplies a growing-$h$
nonvanishing window, but not the diagonal range $h\asymp N$.

Since the coefficients in (11) are integers,



$$
\left(\prod_{\ell=0}^{h-1}Q_{N+\ell}\right)L_{N,h}
 \in\mathbb Z.                                             \tag{17}
$$



Every coefficient $a_{h,\ell}$ is nonzero.  Thus one copy of each
$Q_{N+\ell}$ is also the exact universal monomial clearing profile when
the reduced denominators are treated as independent indeterminates.
The actual numerical least common denominator can be smaller only through
arithmetic gcd correlations among these $Q$'s.

Whenever $L_{N,h}\ne0$, (16)--(17) imply



$$
\boxed{
 \prod_{\ell=0}^{h-1}Q_{N+\ell}
 \geq
 \frac{q_h^{2N}}
      {\alpha\left(q_h^{-1}+(2N)^{-1}\right)}.}            \tag{18}
$$



For fixed $h$, (14) sharpens this to



$$
\sum_{\ell=0}^{h-1}\log Q_{N+\ell}
 \geq2N\log(2h-1)+O_h(1).                                 \tag{19}
$$



This filter is optimal in a precise dimension sense.  A linear form in
$h$ consecutive $r_N$'s has a response polynomial of degree at most
$h-1$.  If it tends to zero, that polynomial must vanish at $1$.  It
can then vanish at no more than $h-2$ further distinct atoms unless it
is the zero polynomial.  Killing the earliest atoms forces, up to a
scalar, exactly (11), and the first survivor can be no later than
$q_h^{-2}$.

Finally,



$$
(2h-1)^2\leq3^h\qquad(h\geq2),         \tag{20}
$$



with equality only for $h=2$.  The cases $h=2,3$ are immediate, and
the induction ratio is at most $(7/5)^2<3$.  Equations (19)--(20) prove
(4).  Thus higher exact mode cancellation gives no better leading rate
per cleared denominator than the adjacent difference.

## 4. All-size Vandermonde: an exact linear-scale floor

For $h\geq2$, put



$$
V_{N,h}=\prod_{0\leq i<j<h}(r_{N+i}-r_{N+j}),
 \quad
 K=\binom h2,
 \quad
 S=\sum_{0\leq i<j<h}i=\frac{h(h-1)(h-2)}6.               \tag{21}
$$



Strict decrease of $r_N$ proves $V_{N,h}>0$ for every $N\geq1$.
Moreover,



$$
V_{N,h}=
 \frac{I_{N,h}}{\prod_{i=0}^{h-1}Q_{N+i}^{h-1}},
 \qquad
 I_{N,h}=\prod_{i<j}
 (P_{N+i}Q_{N+j}-P_{N+j}Q_{N+i})\in\mathbb Z_{>0}.         \tag{22}
$$



Let $C=432/(13\pi^2)$.  The uniform beta-tail bound from the preceding
package gives



$$
0<r_{N+i}-r_{N+j}<r_{N+i}-\alpha
       <C\,3^{-2(N+i)-3}.                                  \tag{23}
$$



Multiplication over all pairs and use of $I_{N,h}\geq1$ yields the
all-parameter theorem



$$
\boxed{
 \begin{aligned}
 \sum_{i=0}^{h-1}\log Q_{N+i}
 &>h\left(N+\frac{h-2}{3}+\frac32\right)\log3
       -\frac h2\log C .
 \end{aligned}}                                            \tag{24}
$$



Thus the average floor is only $O(N+h)$, even if $h$ grows.

This is not an artifact of the one-sided estimate.  With



$$
c=\frac {32}{27\pi^2},\qquad \rho=\frac9{25},
$$



equation (3) gives, uniformly over all pairs,



$$
\begin{aligned}
 \log V_{N,h}
 &=K\log c-(NK+S)\log9\\
 &\quad+\sum_{d=1}^{h-1}(h-d)\log(1-9^{-d})
       +O(K\rho^N).                                        \tag{25}
 \end{aligned}
$$



Indeed, for $d=j-i\geq1$,


$$
r_{N+i}-r_{N+j}
 =c\,9^{-(N+i)}(1-9^{-d})(1+O(\rho^N)),                   \tag{25a}
$$


with an absolute implied constant once $N$ is large: the main factor
$1-9^{-d}$ is at least $8/9$.  Taking logarithms of (25a) and summing
over the $K$ pairs gives the single sum displayed in (25) and the
uniform accumulated error $O(K\rho^N)$.

The analytic gain is exactly of order $Nh^2+h^3$, while the cleared
denominator has $h(h-1)$ copies.  At indices of size $N+h$, this is a
linear, not $(N+h)\log(N+h)$, gain per copy.  A large lower bound for
the integer $I_{N,h}$ could add arithmetic information, but it would
not come from the beta-tail decay itself.

## 5. Fixed-size Hankel determinants

Define



$$
H_{N,h}=\det(r_{N+i+j})_{0\leq i,j<h}.   \tag{26}
$$



Applying Cauchy--Binet to (8) gives the absolutely convergent discrete
Vandermonde expansion



$$
H_{N,h}=\alpha^h
 \sum_{1\leq q_0<\cdots<q_{h-1}\atop q_j\ {\rm odd}}
 \left(\prod_{a=0}^{h-1}b_{q_a}q_a^{-2N}\right)
 \prod_{0\leq a<b<h}(q_b^{-2}-q_a^{-2})^2.                \tag{27}
$$



For fixed $h$, the unique leading set is
$q_a=2a+1$.  Therefore



$$
\boxed{
 H_{N,h}=C_h
   \prod_{a=1}^{h-1}(2a+1)^{-2N}
   (1+O_h(\theta_h^N)),}                                   \tag{28}
$$



where $0<\theta_h<1$ and



$$
C_h=\alpha^h\left(\prod_{a=0}^{h-1}b_{2a+1}\right)
 \prod_{0\leq a<b<h}
 ((2b+1)^{-2}-(2a+1)^{-2})^2\ne0.                         \tag{29}
$$



Thus $H_{N,h}\ne0$ for every sufficiently large $N$, for each fixed
$h$.

For $0\leq t\leq2h-2$, set



$$
m_t=\min(t+1,\,2h-1-t,\,h).              \tag{30}
$$



Then



$$
\boxed{
 \left(\prod_{t=0}^{2h-2}Q_{N+t}^{m_t}\right)H_{N,h}
 \in\mathbb Z,
 \qquad
 \sum_{t=0}^{2h-2}m_t=h^2.}                               \tag{31}
$$



Indeed, a determinant term chooses one cell in each row and column.  The
largest possible number of selected cells on the anti-diagonal $i+j=t$
is its length $m_t$; the corresponding partial matching extends to a
permutation.  Hence (30) is also the exact universal monomial clearing
exponent when the denominators are treated as independent indeterminates.

Equations (28) and (31) give only



$$
\sum_{t=0}^{2h-2}m_t\log Q_{N+t}
 \geq2N\sum_{a=1}^{h-1}\log(2a+1)+O_h(1).                 \tag{32}
$$



The gain is $O_h(N)$ at fixed size, and for large $h$ the formal
gain-per-copy scale is $2N\log h/h$.  Formula (28) does not assert
uniform nonvanishing when $h=h(N)$; that signed growing-size problem is
explicitly left open.

## 6. Simultaneous higher Euler ratios

For $a\geq0$, define



$$
\begin{aligned}
 R_{n,a}
 &=\frac{|E_{2n+2a}|}
 {((2n+2a)!/(2n)!)|E_{2n}|}\\
 &=\prod_{u=0}^{a-1}r_{n+u}
 =\alpha^a\frac{\beta(2n+2a+1)}{\beta(2n+1)},
 \qquad R_{n,0}=1.                                        \tag{33}
 \end{aligned}
$$



The telescoping identity in (33) is the exact bridge from simultaneous
higher ratios back to the original denominators.  Put



$$
\mathcal S_{N,h}
                  =\det(R_{N+i,a})_{0\leq i,a<h}.          \tag{34}
$$



Factoring the row denominators in the beta expression gives



$$
\mathcal S_{N,h}
 =\alpha^{h(h-1)/2}
   \prod_{i=0}^{h-1}\beta(2N+2i+1)^{-1}
   \det(\beta(2N+2i+2a+1))_{0\leq i,a<h}.                 \tag{35}
$$



The same discrete Cauchy--Binet expansion, now with weights $\chi(q)$,
shows that for each fixed $h$,



$$
\boxed{
 \mathcal S_{N,h}=\widetilde C_h
 \prod_{a=1}^{h-1}(2a+1)^{-(2N+1)}
 (1+O_h(\widetilde\theta_h^N)),
 \qquad \widetilde C_h\ne0.}                              \tag{36}
$$



For $0\leq t\leq2h-3$, put



$$
w_t=\min(t+1,\,h-1,\,2h-2-t).             \tag{37}
$$



Multiplying row $i$ by
$\prod_{u=0}^{h-2}Q_{N+i+u}$ clears every entry in that row.  Hence



$$
\boxed{
 \left(\prod_{t=0}^{2h-3}Q_{N+t}^{w_t}\right)
 \mathcal S_{N,h}\in\mathbb Z,
 \qquad
 \sum_{t=0}^{2h-3}w_t=h(h-1).}                            \tag{38}
$$



The exponents in (37) are again the exact universal maxima: for a fixed
position $t$, a permutation of the columns can make every eligible row
interval cover $t$, and the remaining assignments extend to a
permutation.  Thus the simultaneous construction has the same
$O(Nh\log h)$ analytic gain but $\Theta(h^2)$ denominator copies.
Reducing the actual common denominator far below (38) would be new
arithmetic saturation information, not a consequence of telescoping or
the beta asymptotic.

## 7. Why ordinary total positivity and continued fractions do not close the gap

The signed weights (10) already prevent (8) from being the canonical
positive discrete moment representation.  More concretely, exact
arithmetic gives



$$
\det(r_{1+i+j})_{0\leq i,j<3}
 =-\frac{1238314183775556121}
 {51629038152493172462784000}<0.                           \tag{39}
$$



Thus the Hankel matrix of $(r_N)$ is not totally nonnegative.  A
Stieltjes or Jacobi continued-fraction argument whose denominator gain
comes from positive Hankel minors is therefore unavailable.  Formal
continued fractions may still be defined when the required minors are
nonzero, but their coefficients are ratios of the same signed Hankel
minors and inherit the clearing ledger (31).  They do not by themselves
remove denominator multiplicity.

The general discrete-Vandermonde expression (27) is standard for Hankel
determinants of Dirichlet series; see H. Monien, *Hankel determinants of
Dirichlet series*, arXiv:0901.1883,
<https://arxiv.org/abs/0901.1883>.  Here it was derived directly from
Cauchy--Binet, and the signed beta-ratio coefficients (6)--(10) are what
distinguish the present problem from the positive zeta case.

## 8. Comparison with the quadratic primitive-height threshold

The exact identity



$$
\log Q_N=\log((2N+2)(2N+1)|E_{2N}|)-\log G_N             \tag{40}
$$



and Stirling's formula show that



$$
\log G_N=o(N\log N)
 \quad\Longleftrightarrow\quad
 \log Q_N=2N\log N+o(N\log N).                            \tag{41}
$$



The constructions above do not reach (41):

* the optimal $h$-term linear filter gives total gain
  $2N\log(2h-1)$, spread over $h$ denominators, and (20) says the
  adjacent pair is already optimal per copy;
* the Vandermonde gives only $O(h(N+h))$ after its exact clearing;
* fixed Hankel and simultaneous determinants give
  $O(Nh\log h)$ before division among $\Theta(h^2)$ copies.

Even if one grants nonvanishing beyond the certified range (16d), taking
$h\asymp N$ in the linear filter would produce only an $N\log N$
**total** exponent, spread across $\asymp N$ different denominators.
The target for their sum would instead be $\asymp N^2\log N$.  This is
the denominator-multiplicity barrier in its simplest form.

The remaining arithmetic escape can now be stated precisely: one would
need either

1. a growing-size determinant with decay beyond the Dirichlet-mode
   capacity established here and a proof of nonvanishing, or
2. a systematic reduction of the actual clearing in (17), (31), or (38)
   by a factor large enough to remove $\Theta(h)$ denominator copies,
   or a comparably large universal divisor of the cleared numerator.

Neither is supplied by total positivity, the beta tail, or elementary
telescoping.  Establishing such a cancellation would be a genuinely new
arithmetic lemma about adjacent Euler-number gcds.

## 9. Deterministic replay

The companion certificate verifies:

* the Euler-product coefficient formula on a declared finite grid;
* the exact filter polynomials, their roots, primitive content, response
  denominators, and the leading factor (15);
* the all-size formula (24) on an exact rational grid;
* the Hankel and simultaneous determinant clearings and the exponent
  profiles (30), (37);
* the negative minor (39); and
* numerical convergence to the fixed-size asymptotics.

The finite grid is not used to prove the all-parameter results.  From the
research directory run

    python3 scripts/root_unity_beta_higher_determinant_certificate.py
    sha256sum -c results/root_unity_beta_higher_determinant_hashes.sha256

No claim in this package classifies $e+\pi$.
