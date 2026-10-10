> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The selected-gcd problem inside the cyclotomic-unit cone

Checked: 2026-08-27 UTC

## Verdict

Let



$$
K=\mathbb Q(\zeta_{20})^+,
 \qquad \Theta_d=-i\Lambda_{5,d},
 \qquad s=e+\pi,
 \tag{1}
$$



and let the least positive rational clearing of the two coefficients be



$$
q_d\Theta_d=u_ds+v_d,
              \qquad u_d,v_d\in\mathcal O_K.
 \tag{2}
$$



For a cyclotomic-unit multiplier $\theta_d$, put



$$
\begin{aligned}
  \mathcal A_d&=\operatorname {Tr}_{K/\mathbb Q}(\theta_du_d),\\
  \mathcal B_d&=\operatorname {Tr}_{K/\mathbb Q}(\theta_dv_d),\\
  g_d&=\gcd(\mathcal A_d,\mathcal B_d).
 \end{aligned}
 \tag{3}
$$



This note gives an exact reduction of the only cone left open by the
primitive-chamber theorem.  On every residue progression of a rational
unit ray, the multiplier coordinates follow a fixed unimodular order-four
recurrence.  If the varying trace matrix has Smith invariants
$\alpha_d\mid\beta_d$, then



$$
\boxed{
  g_d=\alpha_d\gcd\!\left(z_{1,d},
                  \frac{\beta_d}{\alpha_d}z_{2,d}\right).}
 \tag{4}
$$



The full Smith-coordinate vector
$(z_{1,d},z_{2,d},z_{3,d},z_{4,d})$ is primitive, but its selected first
two coordinates need not be.  Formula (4), not the norm of the coefficient
ideal, is therefore the exact remaining arithmetic problem.

The canonical trace-norm construction does give



$$
g_d^4\mid
        N_{K/\mathbb Q}(\mathcal A_dv_d-\mathcal B_du_d),
 \tag{5}
$$



but its resulting upper bound for $g_d$ is clearing-sensitive and too
weak.  Moreover, divisibility of the two traces puts
$\theta_d/g_d$ in a rank-two trace dual which is not a fractional ideal;
one cannot apply an algebraic-integer norm to it.  These facts rigorously
explain why the existing coefficient-ideal norm calculation does not close
the cone.

There is, however, a stronger denominator-transfer divisor which survives
every selected trace gcd.  Put



$$
D_d={!d},\qquad h_d=d!,\qquad
 D_{0,d}=\frac{D_d}{\gcd(D_d,h_d)}.
$$



For an explicitly defined integer $C_d(\theta_d)$, proved in Section 6,



$$
\boxed{
 \frac{D_{0,d}}{\gcd(D_{0,d},C_d(\theta_d))}
       \ \bigm|\ \frac{\mathcal A_d}{g_d}.}
 \tag{5a}
$$



Moreover,



$$
\log D_{0,d}\geq\frac12d\log d-O(d),
 \tag{5b}
$$



by the elementary rational-approximation lower bound for $e$.  Thus an
upper bound
$\log\gcd(D_{0,d},C_d)=o(d\log d)$ would close not only the exponential
gap on the ray below, but every fixed exponential gap of this type.  The
new unresolved arithmetic has therefore been reduced to one explicit
coordinate gcd.  No such all-degree bound is asserted here.

The simplest interior ray is



$$
\theta_d=u_7^d.
 \tag{6}
$$



It satisfies the three cone inequalities with room to spare, and its
primitive trace obeys the sharp comparison



$$
\boxed{
 \left|\frac{\mathcal A_d}{g_d}s+\frac{\mathcal B_d}{g_d}\right|
 \asymp
 \frac{|\mathcal A_d/g_d|}{d\varphi^d}.}
 \tag{7}
$$



Consequently an all-degree no-go on this ray requires a lower bound of
order $d\varphi^d$ for the primitive coefficient.  Conversely,
$|\mathcal A_d/g_d|=o(d\varphi^d)$ would give a genuinely decreasing,
eventually nonzero family.

The archived exact scan through $d=200$ finds



$$
\max_{d\leq200}g_d=2216\quad(d=199),
 \tag{8}
$$



while $|\mathcal A_{199}/g_{199}|$ has 1260 decimal digits.  This is
strongly divergent finite behavior, but it is only a diagnostic.  No
all-degree upper bound for the selected gcd in (4) is proved here, and no
primitive conclusion is claimed inside the cone.

For the divisor (5a), the same exact scan finds
$\gcd(D_{0,d},C_d)=1$ except at $d=4,8,12,28,199$.  At $d=199$ that
gcd is $277$, so (5a) alone gives a proved 366-digit divisor of the
primitive coefficient.  This finite pattern is not extrapolated.

Nothing in this note proves algebraicity or transcendence of $e+\pi$.

## 1. Relative-trace coordinates

Let $F=\mathbb Q(\sqrt5)$, and let $\tau$ be the nontrivial automorphism
of $K/F$.  The edge coefficient has the exact structure



$$
u_d\in F,
        \qquad v_d=v_{d,+}+v_{d,-},
        \qquad \tau(v_{d,\pm})=\pm v_{d,\pm}.
 \tag{9}
$$



For any $\theta\in\mathcal O_K$, set



$$
x=\theta+\tau\theta,
              \qquad y=\theta-\tau\theta.
 \tag{10}
$$



Taking the relative trace first gives the exact pair



$$
\boxed{
 \begin{aligned}
 \operatorname {Tr}_{K/\mathbb Q}(\theta u_d)
   &=\operatorname {Tr}_{F/\mathbb Q}(x u_d),\\
 \operatorname {Tr}_{K/\mathbb Q}(\theta v_d)
   &=\operatorname {Tr}_{F/\mathbb Q}
        (xv_{d,+}+yv_{d,-}).
 \end{aligned}}
 \tag{11}
$$



The two relative coordinates are not independent.  If
$n=N_{K/F}(\theta)$, then



$$
y^2=x^2-4n.
 \tag{12}
$$



For a unit multiplier, $n\in\mathcal O_F^\times$.  Relation (12) is
useful for exact modular investigations, but it does not turn the two
rational trace congruences in (11) into divisibility of $x$ and $y$
as algebraic integers.  Each rational trace congruence cuts only one
dimension from the two-dimensional $F$-coordinate space.

## 2. Fixed recurrence on a rational ray

Let



$$
\theta_d=u_3^{m_3(d)}u_7^{m_7(d)}u_9^{m_9(d)},
 \qquad \mathbf m(d)=d\mathbf r+O(1),
 \qquad \mathbf r\in\mathbb Q^3.
 \tag{13}
$$



Choose a common denominator $N$ for $\mathbf r$, and restrict to one
class $d=d_0+Nn$.  The bounded integer offset takes only finitely many
values.  After fixing one such value, every term belongs to the orbit



$$
\theta_{d_0+Nn}=\xi\gamma^n,
 \qquad
              \gamma=u_3^{Nr_3}u_7^{Nr_7}u_9^{Nr_9},
 \tag{14}
$$



with a fixed unit $\xi$.  In the integral basis



$$
1,\quad \zeta_5+\zeta_5^{-1},\quad
 i(\zeta_5-\zeta_5^{-1}),\quad
 i(\zeta_5^2-\zeta_5^{-2}),
 \tag{15}
$$



let ${\bf x}_n\in\mathbb Z^4$ be the coordinate column of
$\xi\gamma^n$.  Multiplication by $\gamma$ is a unimodular integral
matrix $C_\gamma$, so



$$
{\bf x}_{n+1}=C_\gamma{\bf x}_n,
              \qquad \det C_\gamma=1.
 \tag{16}
$$



In particular, every coordinate sequence satisfies the fixed order-four
recurrence given by the characteristic polynomial of $C_\gamma$, and
${\bf x}_n$ is primitive for every $n$.

The recurrence (16) does not by itself solve the gcd problem: the Smith
basis of the trace matrix below varies with $d$, because the Padé edge
coefficients vary with $d$.

## 3. Exact Smith and prime-adic formulas

In the basis (15), the trace Gram matrix is



$$
G=\begin{pmatrix}
 4&-2&0&0\\
 -2&6&0&0\\
 0&0&10&0\\
 0&0&0&10
 \end{pmatrix}.
 \tag{17}
$$



If ${\bf u}_d,{\bf v}_d$ are the coordinate columns of $u_d,v_d$,
put



$$
M_d=\begin{pmatrix}
       (G{\bf u}_d)^t\\
       (G{\bf v}_d)^t
     \end{pmatrix}.
 \tag{18}
$$



For every $d\geq2$, this matrix has rank two.  Choose an integral Smith
decomposition



$$
S_dM_dV_d=
       \begin{pmatrix}\alpha_d&0&0&0\\0&\beta_d&0&0\end{pmatrix},
 \qquad \alpha_d\mid\beta_d,
 \tag{19}
$$



where $S_d\in\operatorname {GL}_2(\mathbb Z)$ and
$V_d\in\operatorname {GL}_4(\mathbb Z)$.  Let



$$
{\bf z}_d=V_d^{-1}{\bf x}_d.
 \tag{20}
$$



Left multiplication by $S_d$ preserves the ordinary gcd of a pair.
Equations (18)--(20) therefore give



$$
\begin{aligned}
 g_d
  &=\gcd(\alpha_dz_{1,d},\beta_dz_{2,d})\\
  &=\alpha_d\gcd\!\left(z_{1,d},
             \frac{\beta_d}{\alpha_d}z_{2,d}\right),
 \end{aligned}
 \tag{21}
$$



which proves (4).  Although



$$
\gcd(z_{1,d},z_{2,d},z_{3,d},z_{4,d})=1,
 \tag{22}
$$



there is no implication that $z_{1,d}$ and $z_{2,d}$ are coprime.
This is the exact difference from the two-dimensional quadratic-ray
calculation, where the transformed vector had only two coordinates.

For every rational prime $p$, (21) also gives the precise valuation



$$
\boxed{
 v_p(g_d)=\min\{v_p(\alpha_d)+v_p(z_{1,d}),
                  v_p(\beta_d)+v_p(z_{2,d})\}.}
 \tag{23}
$$



Equivalently,



$$
p^t\mid g_d
 \quad\Longleftrightarrow\quad
 M_d{\bf x}_d\equiv0\pmod {p^t}.
 \tag{24}
$$



Thus the unresolved content is an orbit-hit problem for the fixed unit
recurrence (16) against the varying codimension-two kernels (24).  The
Smith divisor $\alpha_d$ is forced trace content; the remaining factor
in (21) is selected orbit content.  A bound for the former is not a bound
for the latter.

## 4. Why coefficient-ideal norms do not bound (21)

Let



$$
\mathcal M_d=\mathbb Zu_d+\mathbb Zv_d.
 \tag{25}
$$



The two divisibilities in (3) say exactly that



$$
\frac{\theta_d}{g_d}\in
 \mathcal M_d^\vee:=
 \{x\in K:\operatorname {Tr}(x\mathcal M_d)\subseteq\mathbb Z\}.
 \tag{26}
$$



This is not the codifferent of the full coefficient ideal
$(u_d,v_d)$.  Indeed, the rational annihilator



$$
\mathcal M_d^\perp=
 \{x\in K:\operatorname {Tr}(xu_d)=\operatorname {Tr}(xv_d)=0\}
 \tag{27}
$$



has dimension two over $\mathbb Q$, and
$\mathcal M_d^\perp\subset\mathcal M_d^\vee$.  Hence
$\mathcal M_d^\vee$ is not a discrete full lattice or a fractional
ideal.  In particular, (26) does **not** make $\theta_d/g_d$ an
algebraic integer, and the unit identity $|N(\theta_d)|=1$ gives no
upper bound for $g_d$.

There is one genuine norm inequality.  Define



$$
W_d=\mathcal A_dv_d-\mathcal B_du_d.
 \tag{28}
$$



Since



$$
\frac{W_d}{g_d}
  =\frac{\mathcal A_d}{g_d}v_d
   -\frac{\mathcal B_d}{g_d}u_d\in\mathcal O_K,
 \tag{29}
$$



and $u_d,v_d$ are rationally independent for $d\geq2$, a nonzero
trace pair gives a nonzero element in (29).  Its norm is a nonzero integer,
so



$$
1\leq\left|N\!\left(\frac{W_d}{g_d}\right)\right|
       =\frac{|N(W_d)|}{g_d^4}.
 \tag{30}
$$



This proves (5) and the formal lower bound



$$
\left|\frac{\mathcal A_d}{g_d}\right|
 \geq\frac{|\mathcal A_d|}{|N(W_d)|^{1/4}}.
 \tag{31}
$$



But (31) is not invariant under harmless common clearing.  Replacing
$(u_d,v_d)$ by $(m u_d,m v_d)$ multiplies
$(\mathcal A_d,\mathcal B_d)$ by $m$, leaves the primitive pair
unchanged, and multiplies $W_d$ by $m^2$.  The right side of (31) is
therefore divided by $m$.  Even at the least clearing, the archived exact
records show that this fourth-root norm bound is weaker than the trivial
integer bound at every displayed degree.  A successful norm argument would
need additional projectively invariant information about the selected
orbit factor in (21).

For another exact warning, keep $d=2$ and its coefficient ideal fixed.
The two multipliers $u_7^2$ and $u_7^{1275}$ give selected trace gcds
$50$ and $994110$, respectively.  This finite comparison does not
describe their asymptotic growth; it proves only that the fixed coefficient
ideal by itself does not determine the selected gcd.

## 5. The elementary interior ray $u_7^d$

The coordinate vector of $u_7$ in (15) is



$$
(2,1,-1,-1).
 \tag{32}
$$



Its multiplication matrix and characteristic polynomial are



$$
C_7=\begin{pmatrix}
 2&1&-4&-3\\
 1&1&-3&-1\\
 -1&-1&2&1\\
 -1&0&1&1
 \end{pmatrix},
 \qquad
 P_7(X)=X^4-6X^3+X^2+4X+1.
 \tag{33}
$$



Thus $\det C_7=1$, and every coordinate of $u_7^d$ satisfies



$$
x_{d+4}=6x_{d+3}-x_{d+2}-4x_{d+1}-x_d.
 \tag{34}
$$



At the four real embeddings, in order $1,3,7,9$,



$$
\sigma_k(u_7)=\frac{\sin(7k\pi/20)}{\sin(k\pi/20)}.
 \tag{35}
$$



The polynomial (33) has two roots in $(-1/2,0)$, one root in
$(1,6/5)$, and one root greater than $5$; exact rational isolating
intervals are in the certificate.  Formula (35) assigns the two negative
roots to $k=3,9$ and the smaller positive root to $k=7$.  For the
distinguished embedding, one can also see the last bound directly:
$\sin(7\pi/20)>\sin(\pi/3)>5/6$, while
$\sin(\pi/20)<\pi/20<11/70$, so $\sigma_1(u_7)>5$.

Since $\varphi<2$, these inequalities imply



$$
\mu_1-\mu_3>\log\varphi,
 \qquad
 \mu_1-\mu_7>\log\varphi,
 \qquad
 \mu_1>\mu_9.
 \tag{36}
$$



Hence this ray lies strictly inside the unresolved cone.  In fact
$\varphi^2<3$, and the same bounds show



$$
\frac{|\sigma_1(u_7)|}{\varphi}
   >\max\{\varphi|\sigma_3(u_7)|,
           \varphi\sigma_7(u_7),
           |\sigma_9(u_7)|\}.
 \tag{37}
$$



Thus both the coefficient and the raw value have unique dominant embedding
$1$, and their rate gap is exactly $-\log\varphi$.  The endpoint
expansion at that embedding includes the nonzero factor $d^{-1}$.
Consequently



$$
\left|\frac{T_d}{a_d}\right|
                       \asymp\frac1{d\varphi^d},
 \tag{38}
$$



where $T_d=a_ds+b_d$ is the rational trace before clearing.

Since



$$
\frac{\mathcal A_d/g_d}{a_d}T_d
    =\frac{\mathcal A_d}{g_d}s+\frac{\mathcal B_d}{g_d},
 \tag{39}
$$



(38) proves the sharp primitive comparison (7).  Notice that the factorial
size visible in the cleared coefficients is not, by itself, a proof: it may
be removed only after the selected gcd in (21) is controlled.

## 6. A denominator-transfer divisor which survives primitivization

The preceding Smith formula isolates the exact selected gcd, but the
factorial denominator on the exponential side gives one more rigorous
piece of information.  Put



$$
h=d!,\qquad \ell=\operatorname {lcm}(1,\ldots,d),\qquad
 P_d(X)=hA_d(X)\in\mathbb Z[X].
 \tag{40}
$$



Also put $Q_d(X)=h\ell B_d(X)\in\mathbb Z[X]$, and define



$$
\begin{aligned}
 X_d(\theta)={}&\operatorname {Tr}_{K/\mathbb Q}
   \{\theta P_d(\eta)P_d(\bar\eta)\},\\
 R_d={}&P_d(\eta)Q_d(\bar\eta)
       -P_d(\bar\eta)Q_d(\eta),\\
 Z_d(\theta)={}&\operatorname {Tr}_{K/\mathbb Q}\{\theta(0,-R_d)\}.
 \end{aligned}
 \tag{41}
$$



Here $(0,-R_d)$ denotes the anti-fixed integral element in the ambient
pair model of $K$.  The points $\eta,\bar\eta$ are algebraic-integer
units.  Hence $P_d(\eta),P_d(\bar\eta),Q_d(\eta),Q_d(\bar\eta)$
are algebraic integers.  Conjugation interchanges $\eta$ and
$\bar\eta$, so it sends $R_d$ to $-R_d$; consequently the pair
$(0,-R_d)$, which represents $-iR_d$, is both integral and fixed by
full complex conjugation, hence belongs to $\mathcal O_K$.  Thus every
element in (41) is integral and



$$
X_d(\theta),Z_d(\theta)\in\mathbb Z.
 \tag{42}
$$



Set



$$
C_d(\theta)=2\ell X_d(\theta),
               \qquad E_d(\theta)=5Z_d(\theta).
 \tag{43}
$$



To derive the cleared pair rather than merely infer it from the finite
certificate, write



$$
a_d=P_d(1)=(-1)^dD_d.
 \tag{43a}
$$



In the ambient pair model the three safe coordinate blocks are exactly



$$
\begin{aligned}
 U_d^{\rm safe}&=(2\ell a_dP_d(\eta)P_d(\bar\eta),0),\\
 V_{d,\rm fix}^{\rm safe}
   &=(-2(-1)^dh\ell P_d(\eta)P_d(\bar\eta),0),\\
 V_{d,\rm anti}^{\rm safe}
   &=5a_d(0,-R_d).
 \end{aligned}
 \tag{43b}
$$



Each line is integral by (40)--(42).  Tracing (43b) against $\theta$,
using (43a), gives respectively



$$
(-1)^dD_dC_d,\qquad
       (-1)^d(-hC_d),\qquad
       (-1)^dD_dE_d.
 \tag{43c}
$$



Therefore the exact safe rational clearing $h^3\ell$ of the edge gives,
up to the common sign $(-1)^d$, the integer pair



$$
\boxed{
       \bigl(D_dC_d(\theta),
             -hC_d(\theta)+D_dE_d(\theta)\bigr),
       \qquad D_d={!d}.}
 \tag{44}
$$



This is a safe pair, not necessarily the least-cleared pair (3).  To make
the denominator transfer precise, let $q_d$ be the least positive
rational clearing in (2).  Since $h^3\ell$ is itself an admissible
positive integer clearing, $m_d=h^3\ell/q_d$ is a positive integer and



$$
(U_d^{\rm safe},V_d^{\rm safe})=m_d(u_d,v_d).
 \tag{44a}
$$



Thus tracing multiplies both rational coordinates by the same integer
$m_d$.  The safe pair (44), the least-cleared pair, and the pair obtained
after dividing either one by its ordinary coordinate gcd consequently
represent exactly the same rational projective class.  In particular,
their primitive integer pairs agree up to a common sign; no claim that the
safe clearing is least is used below.

Let



$$
\delta_d=\gcd(D_d,h),\qquad
 D_{0,d}=D_d/\delta_d,\qquad h_{0,d}=h/\delta_d.
 \tag{45}
$$



After dividing the common factor $\delta_d$, (44) becomes



$$
\bigl(D_{0,d}C_d,
             -h_{0,d}C_d+D_{0,d}E_d\bigr),
       \qquad \gcd(D_{0,d},h_{0,d})=1.
 \tag{46}
$$



Fix a prime $p$, and write
$a=v_p(D_{0,d})$, $c=v_p(C_d)$.  If $c<a$, then the two summands of
the second coordinate in (46) have respective valuations $c$ and at
least $a$.  They cannot cancel, so the second coordinate has valuation
exactly $c$.  The first has valuation $a+c$.  Thus the primitive first
coordinate retains the full factor $p^a$.  If $c\geq a$, the trivial
lower valuation zero is all that follows.  In particular,



$$
\boxed{
 \frac{D_{0,d}}{\gcd(D_{0,d},C_d(\theta))}
       \ \bigm|\ \frac{\mathcal A_d}{g_d}.}
 \tag{47}
$$



This proves (5a).  The primewise statement just proved is slightly stronger
than (47): whenever $v_p(C_d)<v_p(D_{0,d})$, the full
$p^{v_p(D_{0,d})}$, not merely the quotient of the two powers, survives.

The size of $D_{0,d}$ is unconditional.  Indeed,



$$
\frac{D_d}{h}=\sum_{j=0}^d\frac{(-1)^j}{j!},
 \qquad
 \left|e^{-1}-\frac{D_d}{h}\right|<\frac1{(d+1)!}.
 \tag{48}
$$



For $d\geq2$, both numbers in the reciprocal are at least $1/3$, so



$$
\left|e-\frac{h_{0,d}}{D_{0,d}}\right|
                      <\frac9{(d+1)!}.
 \tag{49}
$$



For completeness, Euler's continued fraction



$$
e=[2;1,2,1,1,4,1,1,6,1,\ldots]
 \tag{49a}
$$



gives an absolute $c_e>0$ such that every reduced rational $r/q$
satisfies



$$
\left|e-\frac rq\right|
                  \geq\frac{c_e}{q^2\log(2q)}.
 \tag{50}
$$



Here is a short proof of the uniform form (50).  By Legendre's criterion,
every nonconvergent has error at least $1/(2q^2)$, which is enough after
decreasing $c_e$.  For the $n$-th convergent the standard
continued-fraction inequalities give



$$
|e-r/q|>\{(a_{n+1}+2)q^2\}^{-1}.
 \tag{50a}
$$



The pattern (49a) has $a_{n+1}\leq2n+2$, while the convergent
denominators dominate the Fibonacci denominators, so
$n=O(\log(2q))$.  This proves (50), with the finitely many small
denominators absorbed into $c_e$.

Apply (50) to the reduced fraction $h_{0,d}/D_{0,d}$.  Since
$D_{0,d}\leq D_d<h=d!$, (49)--(50) imply



$$
D_{0,d}^2
   \geq\frac{c_e(d+1)!}{9\log(2d!)},
 \qquad
 \log D_{0,d}\geq\frac12d\log d-O(d).
 \tag{51}
$$



In particular,



$$
\frac{D_{0,d}}{d\varphi^d}\longrightarrow\infty.
 \tag{52}
$$



Indeed, the elementary bound
$\log((d+1)!)\geq(d+1)\log(d+1)-(d+1)$, inserted in (51), gives



$$
\log\frac{D_{0,d}}{d\varphi^d}
       \geq\frac12d\log d-O(d)\longrightarrow+\infty,
 \tag{52a}
$$



which is the claimed comparison and not a numerical extrapolation.

Combining (7), (47), and (51) proves the following conditional reduction,
with no hidden ideal-norm assumption:



$$
\log\gcd(D_{0,d},C_d(\theta_d))=o(d\log d)
 \quad\Longrightarrow\quad
 \left|\frac{\mathcal A_d}{g_d}s+
       \frac{\mathcal B_d}{g_d}\right|\longrightarrow\infty
 \tag{53}
$$



on the ray $u_7^d$.  More generally, the same conclusion holds whenever
the logarithm of that gcd is smaller than
$\log D_{0,d}-d\log\varphi-\log d$ by a quantity tending to infinity.
The exact finite sparsity of $\gcd(D_{0,d},C_d)$ is not a proof of this
hypothesis.

## 7. Exact finite certificate

The companion script reconstructs $u_d,v_d$ from the integral edge
recurrences, multiplies $u_7^d$ in the integral basis, and for every
$2\leq d\leq200$:

1. verifies the direct trace pair against the matrix product (18);
2. computes a full Smith decomposition (19);
3. verifies (21) and the prime-by-prime valuation formula (23);
4. checks that all four transformed orbit coordinates are primitive;
5. reconstructs the safe pair (44), verifies its primitive equivalence,
   and checks the divisor (47);
6. at selected degrees, checks (5) by an exact field norm.

The finite support of primes occurring in the selected gcds, the largest
extra factor after $\alpha_d$, selected Smith coordinates, primitive
coefficient digit counts, and fourth-root norm comparisons are recorded in
<results/cyclotomic_unit_cone_selected_gcd_d200.json>.

The exact generator is
<scripts/cyclotomic_unit_cone_selected_gcd.py>.  The bounded scan is not
used as evidence for an unproved all-degree gcd estimate.
