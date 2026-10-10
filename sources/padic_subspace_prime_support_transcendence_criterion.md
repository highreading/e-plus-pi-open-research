> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A $p$-adic Subspace-Theorem criterion from primitive coefficient support

Checked: 2026-08-27 UTC.

## 1. Scope and verdict

Put



$$
\alpha=e+\pi.
$$



This note isolates an exact way in which prime support can amplify integer
linear forms



$$
\Lambda_\nu=Q_\nu\alpha-P_\nu,
       \qquad P_\nu,Q_\nu\in\mathbb Z,
       \qquad Q_\nu>0,
       \qquad \gcd(P_\nu,Q_\nu)=1.                 \tag{1}
$$



The result is a transcendence criterion, not merely an irrationality
criterion.  For a fixed finite set of primes $\mathcal S$, define the
inside and outside parts of a nonzero integer $m$ by



$$
m_{\mathcal S}=\prod_{p\in\mathcal S}p^{v_p(m)},
 \qquad
 m_{\mathcal S^c}=\frac{|m|}{m_{\mathcal S}}.       \tag{2}
$$



The central sufficient inequality is



$$
\boxed{
 |\Lambda_\nu|
 (P_\nu)_{\mathcal S^c}(Q_\nu)_{\mathcal S^c}
 \le Q_\nu^{1-\eta}}
                                                               \tag{3}
$$



for one fixed $\eta>0$, infinitely many primitive pairs, and
$Q_\nu\to\infty$.  Under these hypotheses, $e+\pi$ is
transcendental.

There is also a rigorous moving-support version.  If many distinct forms
can be put into blocks whose *union* of coefficient primes grows extremely
slowly, the quantitative $p$-adic Subspace Theorem gives the same
conclusion.  For a block of $M$ forms and $s$ places (including
infinity), the sufficient support scale is



$$
s^6\log(s+2)=o(\log M).           \tag{4}
$$



This is much stronger than bounding the number of prime divisors of each
individual coefficient.  It also explains why a square-free radical bound
alone is inadequate: all prime-power multiplicities outside the selected
set occur in (3).

The archive families do not currently meet either criterion.  The closest
formal fit is the factorial-digit family: its primitive forms already have
the required power-sublinear size uniformly, so a two-coefficient support
theorem plus unbounded primitive height would finish the problem.  No such
support theorem is known.  The cyclotomic, Bessel-matching, common-kernel,
and quartic families have additional height/content or nonvanishing gaps,
as audited below.

Nothing in this note proves that the hypotheses of (3) or (4) hold for an
archived infinite family.  Thus it does not classify $e+\pi$.

## 2. Exact quantitative input

The normalized rational absolute values used below are



$$
|x|_\infty=|x|,
 \qquad |p|_p=p^{-1}.                                  \tag{5}
$$



The following is the rational-integral quantitative $p$-adic Subspace
Theorem in the normalization needed here.  It is quoted on page 246,
equations (1.3)--(1.5), of H. P. Schlickewei,
“The quantitative Subspace Theorem for number fields,” *Compositio
Mathematica* **82** (1992), 245--273,
[NUMDAM PDF](https://www.numdam.org/item/CM_1992__82_3_245_0.pdf).
There Schlickewei is restating the main rational-integral theorem of
H. P. Schlickewei, “The number of subspaces occurring in the $p$-adic
subspace theorem in diophantine approximation,” *J. Reine Angew. Math.*
**406** (1990), 44--108,
[DOI 10.1515/crll.1990.406.44](https://doi.org/10.1515/crll.1990.406.44).

Let



$$
\mathcal V=\{\infty,p_2,\ldots,p_s\},
$$



let $K/\mathbb Q$ be a normal number field of degree $d$, and, for
each $v\in\mathcal V$, let
$L^{(v)}_1,\ldots,L^{(v)}_n$ be linearly independent linear forms in
$n$ variables with coefficients in $K$.  An embedding of $K$ into
the chosen algebraic closure of $\mathbb Q_v$ is fixed at each place.
If $0<\delta<1$, consider the rational integral solutions
$\mathbf x\ne0$ of



$$
\prod_{v\in\mathcal V}\prod_{i=1}^n
       |L_i^{(v)}(\mathbf x)|_v
 <
 \left(
  \prod_{v\in\mathcal V}
   |\det(L_1^{(v)},\ldots,L_n^{(v)})|_v
 \right)
 \|\mathbf x\|_2^{-\delta}.                         \tag{6}
$$



Apart from solutions satisfying



$$
\|\mathbf x\|_2<
 \max\left\{(n!)^{8/\delta},
 H(L_i^{(v)}):v\in\mathcal V,1\le i\le n\right\},      \tag{7}
$$



all solutions of (6) lie in at most



$$
\boxed{
 R(n,s,d,\delta)=
 \left\lfloor
 (8sd)^{2^{6n}s^6\delta^{-2}}
 \right\rfloor}                                        \tag{8}
$$



proper rational subspaces.  The version for an arbitrary coefficient
field of degree $d$ has $d!$ in place of $d$.  Schlickewei states
immediately after (1.5) on page 246 that $d!$ may be replaced by $d$
when the coefficient field is normal.  Passing to the normal closure will
therefore be used throughout this note.

Only the rational-integral statement (6)--(8) is used below.  In
particular, no issue about algebraic-integer variables, local degrees, or
field discriminants enters the application.

## 3. The exact product identity

Suppose temporarily that $\alpha$ is algebraic, and let $K$ be the
normal closure of $\mathbb Q(\alpha)$.  At infinity use the distinguished
real embedding and the two forms



$$
L_{1,\infty}(X,Y)=-X+\alpha Y,
 \qquad
 L_{2,\infty}(X,Y)=Y.                              \tag{9}
$$



At every $p\in\mathcal S$, use



$$
L_{1,p}(X,Y)=X,
 \qquad
 L_{2,p}(X,Y)=Y.                                  \tag{10}
$$



Every coefficient matrix has determinant $1$ or $-1$, so the
determinant product on the right of (6) is exactly one.  Evaluate at
$\mathbf x=(P,Q)$.  Equations (5), (9), and (10) give



$$
\begin{aligned}
 \prod_{v\in\{\infty\}\cup\mathcal S}
 |L_{1,v}(P,Q)L_{2,v}(P,Q)|_v
 &=|Q\alpha-P|Q\prod_{p\in\mathcal S}|PQ|_p\\
 &=\frac{|\Lambda|Q}{P_{\mathcal S}Q_{\mathcal S}}\\
 &=\boxed{
   \frac{|\Lambda|P_{\mathcal S^c}Q_{\mathcal S^c}}
        {|P|}}.                                      \tag{11}
\end{aligned}
$$



The last equality is just



$$
P_{\mathcal S}P_{\mathcal S^c}=|P|,
 \qquad
 Q_{\mathcal S}Q_{\mathcal S^c}=Q.                 \tag{12}
$$



This proves the product formula; it is not an estimate.  A primitive pair
with $P=0$ has $Q=1$, so the last expression is legitimate for every
term of any sequence with $Q\to\infty$, after discarding at most
finitely many terms.

Two points in (11) are essential.

* The factor outside $\mathcal S$ contains both primitive coefficients,
  not just the denominator $Q$.
* It contains valuations with multiplicity, not just the radical of
  $PQ$.

## 4. Fixed-support transcendence theorem

### Theorem 4.1

Let $\mathcal S$ be a fixed finite set of rational primes.  Suppose
there are infinitely many primitive pairs $(P_\nu,Q_\nu)$, with
$Q_\nu>0$, $Q_\nu\to\infty$, and, for one fixed $\eta>0$,



$$
|Q_\nu\alpha-P_\nu|
 (P_\nu)_{\mathcal S^c}(Q_\nu)_{\mathcal S^c}
 \le Q_\nu^{1-\eta}.                               \tag{13}
$$



Then $\alpha=e+\pi$ is transcendental.

### Proof

The outside cofactors are positive integers.  Thus (13) first gives



$$
\left|\alpha-\frac{P_\nu}{Q_\nu}\right|
 =\frac{|\Lambda_\nu|}{Q_\nu}
 \le Q_\nu^{-\eta}.                                \tag{14}
$$



Hence $P_\nu/Q_\nu\to\alpha>0$, and therefore



$$
|P_\nu|\asymp Q_\nu,
 \qquad
 \|(P_\nu,Q_\nu)\|_2\asymp Q_\nu.                \tag{15}
$$



Assume for contradiction that $\alpha$ is algebraic.  Apply (11) and
(13).  There is a fixed constant $C>0$ such that



$$
\prod_v|L_{1,v}(P_\nu,Q_\nu)L_{2,v}(P_\nu,Q_\nu)|_v
 \le C Q_\nu^{-\eta}.                              \tag{16}
$$



Replacing $\eta$ by $\min\{\eta,1\}$ if necessary, (15)--(16) imply,
for all sufficiently large $\nu$,



$$
\prod_v|L_{1,v}(P_\nu,Q_\nu)L_{2,v}(P_\nu,Q_\nu)|_v
 <\|(P_\nu,Q_\nu)\|_2^{-\eta/2}.                  \tag{17}
$$



The threshold (7) is fixed, because the coefficient forms in (9)--(10)
are fixed.  The Subspace Theorem therefore puts all sufficiently large
pairs into finitely many rational lines through the origin.  Each rational
line contains at most two primitive integer points, which are negatives of
one another; the condition $Q>0$ leaves at most one.  This contradicts
$Q_\nu\to\infty$.  Hence $\alpha$ is not algebraic.  $\square$

The proof also excludes the possibility that $\alpha$ is rational.  If
$\alpha=a/b$ in lowest terms, the only primitive exact-zero point with
positive second coordinate is $(a,b)$, so it cannot occur in a sequence
with $Q\to\infty$.

A fixed multiplicative constant on the right of (13), or an
$Q^{o(1)}$ factor, is harmless: decrease $\eta$ and discard finitely
many terms.  The same convention applies to the $\ll$-inequalities in
the family audit.

## 5. Fixed-support corollaries and the exact phase diagram

The following statements are proved corollaries of Theorem 4.1, not
additional conjectures.

### 5.1 Denominator-only support: a Ridout-type corollary

Suppose, for one fixed $\eta>0$,



$$
|\Lambda_\nu|(Q_\nu)_{\mathcal S^c}
              \le Q_\nu^{-\eta}.                         \tag{18}
$$



By (15),
$(P_\nu)_{\mathcal S^c}\le|P_\nu|=O(Q_\nu)$, so (18)
implies (13), after decreasing the exponent.  Thus (18), together with
primitive $Q_\nu\to\infty$, proves transcendence.  In particular, if
every $Q_\nu$ is an $\mathcal S$-unit, then any fixed power saving



$$
|\Lambda_\nu|\le Q_\nu^{-\eta}  \tag{19}
$$



suffices.  This is the direct Ridout-style specialization of the
two-variable $p$-adic Subspace argument.

### 5.2 Both coefficients supported on $\mathcal S$

If $P_\nu$ and $Q_\nu$ are both $\mathcal S$-units, then the outside
factor in (13) is one.  It is enough to have



$$
|\Lambda_\nu|\le Q_\nu^{1-\eta}.
                                                               \tag{20}
$$



The linear form in (20) need not tend to zero; it may even diverge.  What
matters is that it is smaller than its coefficient by a fixed power.

### 5.3 No finite places

For $\mathcal S=\varnothing$, one has
$(P_\nu)_{\mathcal S^c}=|P_\nu|\asymp Q_\nu$ and
$(Q_\nu)_{\mathcal S^c}=Q_\nu$.  Thus (13) reduces, up to fixed
constants and an arbitrarily small loss in the exponent, to the ordinary
Roth-strength condition



$$
|\Lambda_\nu|\le Q_\nu^{-1-\eta}.
                                                               \tag{21}
$$



### 5.4 Exponent bookkeeping

Set



$$
\lambda_\nu=-\frac{\log|\Lambda_\nu|}{\log Q_\nu},
 \qquad
 t_\nu=\frac{
  \log(P_\nu)_{\mathcal S^c}
 +\log(Q_\nu)_{\mathcal S^c}}
 {\log Q_\nu}.                                      \tag{22}
$$



The criterion is exactly



$$
t_\nu<1+\lambda_\nu          \tag{23}
$$



with a fixed positive margin.  This is useful even when
$\lambda_\nu<0$, that is, when the primitive linear form diverges.

Finally, define the outside radical by



$$
\operatorname {rad}_{\mathcal S^c}(PQ)
 =\prod_{\substack{p\notin\mathcal S\\p\mid PQ}}p.
$$



Then the exact decomposition is



$$
\begin{aligned}
 \log(P_{\mathcal S^c}Q_{\mathcal S^c})
 &={}
 \log\operatorname {rad}_{\mathcal S^c}(PQ)\\
 &\quad+
 \sum_{p\notin\mathcal S}
       \bigl(v_p(PQ)-1\bigr)_+\log p.                 \tag{24}
\end{aligned}
$$



Therefore a bound for the radical without a bound for the excess-valuation
sum does not verify (13).

## 6. A quantitative moving-support theorem

The fixed set $\mathcal S$ may change between sufficiently large
blocks, provided a block contains more distinct primitive points than the
quantitative theorem can place on rational lines.

### Theorem 6.1

For each $j$, let $\mathcal B_j$ be a set of $M_j$ distinct
primitive pairs $(P,Q)$ with $Q>0$, and let $\mathcal S_j$ be a
finite set of rational primes.  Put



$$
s_j=1+|\mathcal S_j|.             \tag{25}
$$



Suppose that



$$
\min_{(P,Q)\in\mathcal B_j}Q\longrightarrow\infty,      \tag{26}
$$



that for one fixed $0<\eta\le1$, every point in every sufficiently
large block satisfies



$$
|Q\alpha-P|P_{\mathcal S_j^c}Q_{\mathcal S_j^c}
 \le Q^{1-\eta},                                       \tag{27}
$$



and that



$$
s_j^6\log(s_j+2)=o(\log M_j).           \tag{28}
$$



Then $\alpha=e+\pi$ is transcendental.

### Proof

Assume that $\alpha$ is algebraic and let $D$ be the degree of the
normal closure of $\mathbb Q(\alpha)$.  The argument in (14)--(17),
uniformly in a block, lets us apply (6) with



$$
n=2,\qquad \delta=\eta/2.
$$



The coefficient heights and the small-solution threshold (7) are fixed,
independently of the identities of the primes in $\mathcal S_j$.
Equations (8) and (25) give at most



$$
T(s_j,D,\eta)
 =\left\lfloor
   (8s_jD)^{2^{14}\eta^{-2}s_j^6}
  \right\rfloor                                        \tag{29}
$$



rational lines containing the points in the large part of the block.
Here



$$
2^{14}=2^{6\cdot2}\cdot4
$$



because $(\eta/2)^{-2}=4\eta^{-2}$.  Each line contains at most one
primitive point with $Q>0$.  For fixed $D,\eta$,



$$
\log T(s_j,D,\eta)
 =O_{D,\eta}\bigl(s_j^6\log(s_j+2)\bigr).                \tag{30}
$$



Condition (28) therefore gives $M_j>T(s_j,D,\eta)$ for all sufficiently
large $j$, a contradiction.  $\square$

### Corollary 6.2: full block support

Take $\mathcal S_j$ to be the union of all prime divisors of all
$P Q$ in the block.  Then (27) becomes simply



$$
|Q\alpha-P|\le Q^{1-\eta}.      \tag{31}
$$



Thus it suffices that (31), (26), and



$$
\boxed{
 \omega\!\left(\prod_{(P,Q)\in\mathcal B_j}|PQ|\right)^6
 \log\!\left(
 2+\omega\!\left(\prod_{(P,Q)\in\mathcal B_j}|PQ|\right)
 \right)
 =o(\log M_j)}                                          \tag{32}
$$



hold.  Here $\omega$ counts distinct rational primes.  Formula (32)
uses the union of supports across the whole block.  A uniform bound on
$\omega(PQ)$ for each individual point does not imply (32), since the
individual supports may be disjoint.

## 7. Audit of the factorial-digit families

The exact primitive forms in
`factorial_digit_entire_fixed_b_rays.md` and
`factorial_digit_entire_varying_b_regimes.md` are



$$
\begin{aligned}
 W_{a,b}&=\Delta^b(a!),\\
 Z_{a,b}&=\Delta^b C_a,\\
 H_{a,b}&=\gcd(W_{a,b},Z_{a,b}),\\
 Q_{a,b}&=W_{a,b}/H_{a,b},\\
 P_{a,b}&=Z_{a,b}/H_{a,b},\\
 \Lambda_{a,b}
 &=Q_{a,b}\alpha-P_{a,b}
   =\Delta^b x_a/H_{a,b}.                         \tag{33}
 \end{aligned}
$$



For $b\ge1$, the sharp digit-range bound used here is



$$
|\Delta^b x_a|<
 U_{a,b}:=2^{b-1}
 \left(1+\frac1a-\frac1{a+b+1}\right),                 \tag{34}
$$



while $|\Delta^0x_a|<2$.  The archive also proves, for
$0\le b\le a+1$,



$$
W_{a,b}\ge\frac{a}{a+b}(a+b)!\quad(b\ge1),
 \qquad W_{a,0}=a!.                                    \tag{35}
$$



There is an immediate and useful consequence which was not visible in an
ordinary Roth calibration.  Uniformly for all admissible $b$,



$$
|\Delta^b x_a|\le W_{a,b}^{1/2} \tag{36}
$$



for all sufficiently large $a$.  Indeed, the left side is
$\exp(O(a))$, while the logarithm of the right side is
$\tfrac12a\log a+O(a)$, uniformly for $b\le a+1$.  Since
$Q=W/H\le W$, (33) and (36) give



$$
|\Lambda_{a,b}|
 =\frac{|\Delta^b x_a|}{W_{a,b}}Q_{a,b}
 \le Q_{a,b}^{1/2}.                                    \tag{37}
$$



Thus the analytic size hypothesis (31) is already proved, with
$\eta=1/2$, for every sufficiently large factorial-digit form.  To use
Corollary 6.2 one would still need:

1. blocks containing many *distinct* primitive pairs;
2. $\min Q_{a,b}\to\infty$; and
3. the ultra-sparse cumulative support estimate (32).

None of these three assertions is proved in the archive.  In particular,
for fixed $b\ge1$, eventual nonvanishing is equivalent to the unknown
irrationality of $e+\pi$, although Theorem 4.1 itself does not need a
separate nonvanishing hypothesis once distinct primitive heights tend to
infinity.

For a fixed set $\mathcal S$, the denominator-only sufficient condition
(18) becomes the exact desired inequality



$$
\boxed{
 U_{a,b}(Q_{a,b})_{\mathcal S^c}W_{a,b}^{\eta}
 \le H_{a,b}^{1+\eta}}.                                \tag{38}
$$



The two-coefficient condition (13) is implied by



$$
\boxed{
 U_{a,b}(P_{a,b})_{\mathcal S^c}(Q_{a,b})_{\mathcal S^c}
 \le W_{a,b}^{1-\eta}H_{a,b}^{\eta}}.                  \tag{39}
$$



For varying $b$, the exact local-content decomposition is



$$
W=a!D,
 \qquad H=gJ,
 \qquad Q=D'\frac{a!}{J},
 \qquad D'=D/g,
 \qquad \gcd(J,D')=1.                                  \tag{40}
$$



The local digit factor $g$ only cancels the $D$-part.  Concentrating
the denominator on a fixed $\mathcal S$ would require the residual
factor $J\mid a!$ to cancel almost all of the outside-$\mathcal S$
factorial mass in (40), unless a separate support theorem for $D'$ is
found.  The admissible digit ranges provably cannot control $J$; the
archive gives an adversarial canonical-digit construction witnessing this
barrier.  No fixed-support or cumulative-support theorem for the actual
digits of $\pi$ is known.

**Audit verdict.**  This is the cleanest formal candidate for the present
criterion because (37) is unconditional.  The desired new lemma is purely
arithmetic: prime-support concentration and unbounded distinct primitive
heights.

## 8. Audit of the cyclotomic-unit families

Use the sign orientation



$$
Q_d=|\mathcal A_d|/g_d,
 \qquad
 P_d=-\operatorname {sgn}(\mathcal A_d)\mathcal B_d/g_d,
                                                               \tag{41}
$$



so that $Q_d>0$ and the absolute value of the standard form
$Q_d\alpha-P_d$ equals the primitive trace value.  On the elementary
interior ray $\theta_d=u_7^d$,
`cyclotomic_unit_cone_selected_gcd.md` proves



$$
|\Lambda_d|\asymp
                         \frac{Q_d}{d\varphi^d}.          \tag{42}
$$



Consequently the denominator-only condition (18) would follow from



$$
Q_d^{1+\eta}(Q_d)_{\mathcal S^c}
 \ll d\varphi^d,                                       \tag{43}
$$



and the exact two-coefficient condition to seek is



$$
(P_d)_{\mathcal S^c}(Q_d)_{\mathcal S^c}Q_d^\eta
 \ll d\varphi^d.                                       \tag{44}
$$



Even if both coefficients were supported on one fixed $\mathcal S$,
(44) would require



$$
Q_d^\eta\ll d\varphi^d,
 \qquad\text{hence}\qquad \log Q_d=O(d).               \tag{45}
$$



The denominator-transfer theorem in the same note gives an explicit
divisor



$$
\frac{D_{0,d}}{\gcd(D_{0,d},C_d)}\mid Q_d,
 \qquad
 \log D_{0,d}\ge\frac12d\log d-O(d).                  \tag{46}
$$



Thus (45) would force the near-total cancellation



$$
\log\gcd(D_{0,d},C_d)
 \ge\frac12d\log d-O(d).                               \tag{47}
$$



This is the opposite of the small-gcd estimate sought in the existing
primitive-divergence program.  The finite selected-gcd data are tiny, but
they are diagnostic only and cannot be used to negate (47) in all degrees.

Outside the open coefficient-dominant cone of
`cyclotomic_unit_rational_primitive_chambers.md`, the archive proves that
the primitive quotient $|\Lambda_d|/Q_d$ is bounded away from zero or
grows.  There (20) fails for every fixed $\eta>0$, even under hypothetical
full fixed support.  Inside the cone the quotient can decay, but no
simultaneous exponential-height/content theorem and no support theorem are
known.

The accelerated ray of `cyclotomic_unit_accelerated_u7_gcd.md`, with
$t_d/(d\log d)\to\infty$, satisfies



$$
\frac{\log|\Lambda_d|}{\log Q_d}\to1.  \tag{48}
$$



It therefore fails the power-sublinear condition (20), even before asking
for prime support.

Finally, the local $n=5$ first-jet branch does not supply a fixed-support
theorem.  The exact note
`algebraic_unit_two_log_n5_all_prime_counterexample.md` proves the
unconditional new base pair



$$
(p,d)=(109321,6219),             \tag{49}
$$



with



$$
N_{\mathbb Q(\sqrt5)/\mathbb Q}
                    (\mathfrak J_{6219})=109321.
$$



This refutes the conjectural universal support by the old prime $19$ in
that local-content ideal.  It does not prove that infinitely many new
primes occur, and it is not by itself a statement about the rational trace
pair in (41); it merely removes one proposed route to a finite support
claim.

**Audit verdict.**  The rational $u_7$-ray would need two effects at
once: almost total denominator-transfer cancellation to make $Q_d$
exponential, and sufficiently concentrated support to satisfy (44).  No
archived theorem provides either effect.  Accelerating the unit exponent is
rigorously counterproductive.

## 9. Audit of the Bessel and coefficient-matching families

For even $n$, the primitive exponential beta form is



$$
E_n=q_ne-p_n>0,
 \qquad \gcd(p_n,q_n)=1,                                \tag{50}
$$



with



$$
n^n\le q_n<2(2n)^n,
 \qquad
 \frac{n!}{(2n+1)!}\le E_n
 \le\frac{e\,n!}{(2n+1)!}.                             \tag{51}
$$



Thus, for every fixed $\eta<1$,



$$
E_n\le q_n^{-\eta}         \tag{52}
$$



eventually.  If the denominators $q_n$ had fixed finite prime support,
(18) would prove that $e$ is transcendental.  More generally, since
$E_n=q_n^{-1+o(1)}$ on the logarithmic scale allowed by (51), it would
be enough for a fixed set $\mathcal S$ to carry a positive logarithmic
proportion of $q_n$.  This only recovers a conclusion already known for
$e$; the direct form (50) does not contain $e+\pi$.

To obtain the target, the archive matches (50) with a primitive
$\pi$-form



$$
\mathcal L=A+B\pi,
 \qquad \gcd(A,B)=1,\quad B>0.                         \tag{53}
$$



Put $d=(q_n,B)$.  Before the final content $g$ is removed, minimal
matching gives target coefficient $q_nB/d$; the local argument in the
archive proves $g\mid d$.  Hence the final primitive target coefficient
is



$$
Q_{n,k}=\frac{q_nB}{dg}.          \tag{54}
$$



The projective approximation is content-invariant:



$$
\frac{\Lambda_{n,k}^{\rm prim}}{Q_{n,k}}
 =\frac{E_n}{q_n}\mathbin{\pm}\frac{\mathcal L}{B},    \tag{55}
$$



with the sign dictated by the orientation of (53).

No archived matching family currently supplies all three of the following:

1. a fixed power-sublinear bound
   $|\Lambda_{n,k}^{\rm prim}|\le Q_{n,k}^{1-\eta}$;
2. unbounded distinct primitive target coefficients; and
3. fixed support, or blocks satisfying (28), for both final coefficients.

The zero-gap theorem in
`bessel_denominator_zero_gap_smooth_radical_barrier.md` gives



$$
\sum_{n=N}^{2N-1}
 \log\operatorname {rad}_{\le X}(q_n)
 \le3NX^{2/3}\log X+2X^{5/3}\log X.                    \tag{56}
$$



For $X\asymp N\log N$, its average is $o(N\log N)$.  This controls
only the square-free mass of small primes.  It does not control the
excess-valuation term in (24), the cofactor outside a *fixed* set, the
other primitive target coefficient, or the union of supports in a block.
The prime-power period law even records large lifts such as
$7^4\mid q_{361}$ and $11^5\mid q_{1359}$, so the missing valuation
tail is genuine rather than a notational technicality.

The positive critical quadratic-power and fixed-denominator matching
barriers prove divergence of broad primitive families.  Divergence alone
does not logically refute (20), because a divergent form can still be
power-sublinear in its coefficient.  What is absent is a suitable upper
bound relative to (54), together with coefficient support.  In the
known no-go ranges, the archived estimates were designed to rule out
convergence to zero, not to establish the support-weighted inequality (3).

**Audit verdict.**  The Bessel congruences are useful local information,
but current smooth-radical results have the wrong granularity for (3) and
the wrong scope for (32).  No fixed-$\mathcal S$ or controlled-union
construction for the final matched pair is known.

## 10. Audit of the common-kernel families

The direct common-kernel identity in
`common_kernel_lattice_identity_and_capacity_audit.md` produces



$$
\int_0^1 f(x)\left(e^x+\frac4{1+x^2}\right)dx
 =a\alpha+b,                                             \tag{57}
$$



with $(a,b)$ in the exact image



$$
8\mathbb Z\times2\mathbb Z.     \tag{58}
$$



After dividing $(a,b)$ by their gcd and orienting the first coefficient,
(57) has the form (1).  The exact image theorem is not a prime-support
theorem: it imposes only fixed factors $8$ and $2$, and the remaining
primitive coefficients may contain arbitrary moving primes.

The saturated lattice has a large exact zero-form kernel, and its effective
quotient is rank two.  The potential-theoretic model predicts only



$$
|a\alpha+b|\asymp |a|^{-1},      \tag{59}
$$



the ordinary Dirichlet/Roth boundary, from generic determinant balancing.
That model is supported by exact finite quotient data but is not an
all-degree theorem.  Exceptional vectors remain possible.  A fixed-support
amplification could in principle turn a weaker-than-Roth form into a
transcendence proof, but no infinite support estimate, no uniform
nonvanishing theorem, and no power-sublinear exceptional sequence are
proved.

The symmetric rational-kernel constructions in
`direct_integral_linear_forms_audit.md` and the projective family in
`n_dependent_fixed_denominator_kernel_barrier.md` are different: they
first make $e$- and $\pi$-forms and then match their coefficients.
For projective kernel complexity $o(n\log n)$, the latter note proves



$$
|\Lambda_n^{\rm prim}|
              \ge\frac{c_\pi}{2}\frac{q_n}{B_n^9}\to\infty.  \tag{60}
$$



Again, (60) is a lower bound and does not by itself decide the
power-sublinear inequality (20).  These constructions contain lcm and
Bessel factors with moving primes, and no theorem bounds the outside
cofactors of both primitive coefficients.

**Audit verdict.**  The direct identity (57) is structurally compatible
with support amplification, but its exact coefficient image gives no
support concentration.  The coefficient-matched common-kernel branches
have neither the needed relative upper bound nor the needed support
theorem.

## 11. Audit of the quartic-power families

For



$$
J_{n,k}=\int_0^1\frac{x^n(1-x)^n}{(1+x^4)^k}\,dx,       \tag{61}
$$



`quartic_power_kernel_hermite_and_matching_obstruction.md` proves that the
non-polynomial Hermite coordinates have a universal dyadic denominator



$$
2^{3(k-1)-s_2(k-1)}.             \tag{62}
$$



It is tempting to interpret (62) as fixed support at $2$, but this is
not the denominator of the final primitive rational pair.  Clearing the
rational endpoint also introduces, in a valid universal clearing,



$$
\operatorname {lcm}(1,\ldots,k-1)
 \operatorname {lcm}(1,\ldots,2n+1),                    \tag{63}
$$



and minimal primitive cancellation is unresolved.  Thus the proved
dyadic coordinate structure does not verify fixed support.

The inversion-balanced log-free ray



$$
n=4j+2,\qquad k=3j+2            \tag{64}
$$



has exponential primitive $\pi$-coefficient height, but its forms after
matching with the Bessel $e$-form diverge even after full algebraic
content removal in the real quadratic coefficient field.  A rational
integer application of Theorem 4.1 would additionally require an accepted
trace/rationalization.  In any event, the theorem proves a no-go for
convergence to zero; it does not supply a coefficient-relative upper bound
or a prime-support bound adequate for (3).

The neighboring two-power determinant cancels the logarithm but is
sign-indefinite; no uniform all-power lower bound, nonvanishing theorem, or
primitive endpoint-support theorem is known.  Three adjacent powers give
a genuine rational form



$$
A+B\pi,                          \tag{65}
$$



and `quartic_three_power_fixed_slope_content_barrier.md` identifies the
entire remaining primitive content as one explicit determinant gcd.  At
fixed slope the scale-invariant $\pi$-approximation is exponentially
small in $n$, but matching with $q_n$ in (50) produces a
superfactorial target coefficient unless that gcd removes almost all of
the Bessel/factorial height.  No such content theorem, and no support
theorem for the resulting pair, is available.

For four powers,
`quartic_four_power_primitive_content_smith_reduction.md` proves the exact
selected-content formula



$$
\gcd((Bv)_1,(Bv)_2)
 =s_1\gcd\left(u,\frac{s_2}{s_1}\right),                \tag{66}
$$



but the selected Smith coordinate $u$ of the canonical phase-removing
direction remains uncontrolled.  The first surviving odd-coordinate
asymptotic is phase-dependent, so all-power nonvanishing also remains open.
The weighted-Fleck theorem in
`quartic_boundary_weighted_fleck_valuation.md` determines one complete
two-primary denominator law, but explicitly leaves the other odd
coordinates, odd rational-endpoint denominator, and final determinant gcd
uncontrolled.  These are precisely the quantities needed before one can
evaluate (3) for the primitive pair.

The growing-window lattice in
`quartic_multi_power_kernel_lattice_and_phase_tradeoff.md` has exact
endpoint index $\delta_4/\delta_2$, but for five or more powers also has
nontrivial exact zero relations.  A short kernel vector can therefore be a
zero form.  No block of distinct nonzero primitive pairs with support
satisfying (32) is constructed.

**Audit verdict.**  Dyadic Hermite denominators are not fixed-S primitive
coefficients.  Every current quartic route is missing a final endpoint
content/support theorem; the two- and four-power branches additionally
retain phase/nonvanishing gaps.  None presently meets (3) or (32).

## 12. Concrete live lemmas and decisive barriers

The following are desired lemmas, not results proved in this note.

### Desired lemma A: factorial denominator concentration

Find a fixed finite $\mathcal S$, a fixed $\eta>0$, and infinitely
many admissible $(a,b)$, with $b\ge1$, and distinct primitive
$Q_{a,b}\to\infty$
such that



$$
U_{a,b}(Q_{a,b})_{\mathcal S^c}W_{a,b}^{\eta}
 \le H_{a,b}^{1+\eta}.                                  \tag{67}
$$



By (38) and Theorem 4.1, this alone proves that $e+\pi$ is
transcendental.  Formula (40) shows the exact obstruction: control of the
residual factorial divisor $J$, not merely local digit content $g$.

### Desired lemma B: factorial cumulative support blocks

Construct blocks of $M_j$ distinct factorial-digit pairs with minimum
primitive denominator tending to infinity and



$$
\omega\!\left(\prod_{(a,b)\in\mathcal B_j}
                  P_{a,b}Q_{a,b}\right)^6
 \log\!\left(2+
 \omega\!\left(\prod_{(a,b)\in\mathcal B_j}
                  P_{a,b}Q_{a,b}\right)\right)
 =o(\log M_j).                                           \tag{68}
$$



The size estimate needed with (68) is already the theorem (37); no new
analytic estimate is required.  The sixth-power threshold makes (68) very
strong, but it is an exact all-prime target rather than a vague smoothness
request.

### Desired lemma C: selected endpoint support after matching

For one Bessel--quartic or Bessel--cyclotomic family, prove directly for
the *final primitive pair* that



$$
|\Lambda_n| (P_n)_{\mathcal S^c}(Q_n)_{\mathcal S^c}
 \le Q_n^{1-\eta}                                       \tag{69}
$$



with fixed $\mathcal S,\eta$, or prove the block analogue (27)--(28).
Bounds for the raw clearing, one coordinate ideal, the radical of $q_n$,
or an unselected Smith invariant do not imply (69).  This is the sharp
obstruction common to the current matching constructions.

Of these, Desired lemma A is the narrowest fixed-support target, while
Desired lemma B is the cleanest use of the quantitative moving-support
theorem.  The cyclotomic $u_7$ ray is less promising for this method
because (46)--(47) demand near-total factorial cancellation before support
amplification can even enter.  The Bessel and quartic radical/denominator
results are presently too one-sided to control the exact outside cofactor
in (24).

## 13. Computational status

No new computational certificate is needed for this note.  The Subspace
Theorem application, product identity, corollaries, moving-block count,
and factorial power-sublinear estimate are symbolic proofs.  The family
audit invokes only all-parameter theorems already proved in the cited
archive notes; finite scans are explicitly identified as diagnostics and
are not used as hypotheses.

The primary-source normalization in Section 2 was checked against page 246,
equations (1.3)--(1.5), of Schlickewei's 1992 paper.  Passing to the normal
closure justifies the replacement of $d!$ by $d$, the coefficient
heights are fixed in this application, and every local determinant is a
unit.  There is no remaining hypothesis uncertainty in Theorems 4.1 and
6.1.  The unresolved assertions are exactly the desired arithmetic lemmas
in Section 12.

## 14. Archive dependencies

The family audit used the following source notes; no script or result file
is an input to the proofs in Sections 2--6:

* `factorial_digit_entire_fixed_b_rays.md`;
* `factorial_digit_entire_varying_b_regimes.md`;
* `cyclotomic_unit_cone_selected_gcd.md`;
* `cyclotomic_unit_rational_primitive_chambers.md`;
* `cyclotomic_unit_accelerated_u7_gcd.md`;
* `algebraic_unit_two_log_n5_all_prime_counterexample.md`;
* `direct_integral_linear_forms_audit.md`;
* `n_dependent_fixed_denominator_kernel_barrier.md`;
* `critical_quadratic_power_fourier_barrier.md`;
* `critical_fourier_very_high_matching_closure.md`;
* `exponential_beta_bessel_period_congruence.md`;
* `bessel_denominator_zero_gap_smooth_radical_barrier.md`;
* `common_kernel_lattice_identity_and_capacity_audit.md`;
* `quartic_power_kernel_hermite_and_matching_obstruction.md`;
* `quartic_neighbor_saddle_phase_barrier.md`;
* `quartic_multi_power_kernel_lattice_and_phase_tradeoff.md`;
* `quartic_three_power_fixed_slope_content_barrier.md`;
* `quartic_four_power_primitive_content_smith_reduction.md`;
* `quartic_four_power_odd_residual_first_correction.md`; and
* `quartic_boundary_weighted_fleck_valuation.md`.

The external theorem and its normalization were checked directly on page
246, equations (1.3)--(1.5), of the Schlickewei 1992 primary source cited
in Section 2, rather than inferred from an archive summary.  That page
identifies the underlying 1990 paper and records the normal-field
replacement of $d!$ by $d$.
