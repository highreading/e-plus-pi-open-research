> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 169 child note: the second divided-index transfer on an all-square beta fibre

Date: 2026-08-29 (Beijing time)

## 1. Scope and fixed-seed hypothesis

Let



$$
q_0=q_1=1,\qquad q_n=(4n-2)q_{n-1}+q_{n-2},
$$



and let $p_n$ be its companion beta numerator, with
$(p_0,p_1)=(1,3)$.  Fix a prime $p\geq7$ and a noncentral root
$0<r<s=p-1-r$ of the **actual** denominator.  Put



$$
\lambda={q_r\over p}\pmod p,\qquad
 \delta={-q_{r+p}-q_r\over p}\pmod p.
$$



This note assumes the first singular fibre is all-square:



$$
\boxed{\lambda=\delta=0.}                                      \tag{1.1}
$$



Thus $p^2\mid q_{r+xp}$ for every integer $x$.  No such noncentral
orbit is presently known for the fixed seed $(1,1)$; all conclusions
below are conditional structural theorems, not existence claims.

The restriction $p\geq7$ is exactly what is needed to invoke the
order-six Newton law (the all-even anti-period theorem with $k=3$).

## 2. The cubic controlling $p^2\longrightarrow p^3$

Set



$$
a_x=(-1)^xq_{r+xp},\qquad D_j=\Delta_x^j a_0.
$$



The fourth-antiperiod/Newton theorem gives



$$
a_x\equiv\sum_{j=0}^3D_j{ x\choose j}\pmod {p^3}.
$$



Under (1.1), $p^2\mid D_j$ for $0\leq j\leq3$.  Define



$$
\boxed{
 P(T)=\sum_{j=0}^3{D_j\over p^2}{T\choose j}
 \in\mathbf F_p[T].}                                           \tag{2.1}
$$



In the notation of the archived cube theorem,



$$
P(T)=C+DT+E{T\choose2}+H{T\choose3},                           \tag{2.2}
$$



where



$$
C={q_r\over p^2},\quad
 D={-q_{r+p}-q_r\over p^2},\quad
 E={q_{r+2p}+2q_{r+p}+q_r\over p^2},
$$





$$
H={-q_{r+3p}-3q_{r+2p}-3q_{r+p}-q_r\over p^2}
 \pmod p.                                                       \tag{2.3}
$$



For



$$
N(t,u)=r+tp+up^2,\qquad 0\leq t,u<p,
$$



the exact second-level dichotomy is



$$
\boxed{p^3\mid q_{N(t,u)}\iff P(t)=0.}                         \tag{2.4}
$$



In particular, the condition is independent of $u$.  For a fixed
$t$, either all $p$ children modulo $p^3$ survive or none do:

* if $P(t)\ne0$, all $p$ children have exact valuation two;
* if $P(t)=0$, all $p$ children have valuation at least three.

If $P\ne0$, at most three of the $p$ values of $t$ have the second
alternative.  If $P=0$, all $p^2$ descendants of $r\bmod p$ survive
through $p^3$.

## 3. The exact $p^3\longrightarrow p^4$ law

The all-even anti-period theorem at $k=3$ gives



$$
a_x\equiv\sum_{j=0}^5D_j{x\choose j}\pmod {p^4}.               \tag{3.1}
$$



Here $p^2\mid D_j$ for $0\leq j\leq5$, because the first six
standard values are all square roots, and the universal difference
valuation gives the stronger



$$
p^3\mid D_4,D_5.                                               \tag{3.2}
$$



Define the lifted divided polynomial



$$
\widehat P(T)=\sum_{j=0}^5{D_j\over p^2}{T\choose j}
 \pmod {p^2}.                                                    \tag{3.3}
$$



Since $j<p$, the binomial polynomials lie in $\mathbf Z_{(p)}[T]$,
and Taylor expansion at the integral displacement $pu$ is legitimate
modulo $p^2$.  Equations (3.1)--(3.3) give the exact divided-index law



$$
\boxed{
 {(-1)^{t+u}q_{N(t,u)}\over p^2}
 \equiv \widehat P(t)+puP'(t)\pmod {p^2}.}                      \tag{3.4}
$$



Indeed, $p\widehat P'(t)\equiv pP'(t)\pmod {p^2}$, because the
$j=4,5$ coefficients in (3.3) vanish modulo $p$.

Now suppose $P(t)=0$, and define the legitimate next constant



$$
\widehat C_t={\widehat P(t)\over p}
 \equiv {(-1)^tq_{r+tp}\over p^3}\pmod p.                      \tag{3.5}
$$



Dividing (3.4) by one more factor of $p$ gives



$$
\boxed{
 {(-1)^{t+u}q_{N(t,u)}\over p^3}
 \equiv \widehat C_t+uP'(t)\pmod p.}                           \tag{3.6}
$$



Thus the complete second-level Hensel classification is:

1. If $P'(t)\ne0$, exactly one $u\bmod p$ reaches $p^4$; the
   other $p-1$ children have exact valuation three.
2. If $P'(t)=0$ and $\widehat C_t\ne0$, the branch is dead at the
   fourth-power threshold: every child has exact valuation three.
3. If $P'(t)=\widehat C_t=0$, the branch is all-lift: every child has
   valuation at least four.

This is the requested dead/ordinary/all-lift trichotomy.  A multiple root
of the cubic is necessary, but not sufficient, for a third-level all-lift.
The extra fixed-seed digit $\widehat C_t$ cannot be discarded.

If $P\equiv0$, then $D_0,\ldots,D_5$ are all divisible by $p^3$,
and



$$
Q(T)=\sum_{j=0}^5{D_j\over p^3}{T\choose j}\in\mathbf F_p[T]
$$



is the archived degree-five threshold polynomial: either $Q\ne0$ and
at most five standard $t$'s reach $p^4$, or $Q=0$ and the whole
fibre does.

## 4. The derivative is the divided prime-square index slope

Let $n_t=r+tp$, $M=p^2$, and



$$
\delta_M(n)={-q_{n+M}-q_n\over M}\pmod M.
$$



The prime-power second-antiperiod theorem says that the first slope is
inherited.  Hence (1.1) implies $p\mid\delta_M(n_t)$.  On the other
hand,



$$
a_{t+p}-a_t=(-1)^tM\delta_M(n_t).
$$



Subtracting (3.1) at $t+p$ and $t$, dividing by $p^3$, and reducing
modulo $p$ yields



$$
\boxed{
 {\delta_{p^2}(n_t)\over p}
 \equiv(-1)^tP'(t)\pmod p.}                                    \tag{4.1}
$$



Thus a simple root of $P$ is precisely an ordinary root for the divided
prime-square slope; a multiple root is precisely a singular one.

There is also a literal continuant formula.  Suppose $n_t<(M-1)/2$, put



$$
H_t={M-3\over2}-n_t,
$$



and let ${\cal K}_{H_t}(X)=X{\cal L}_{H_t}(X^2)$ be the odd symmetric
continuant.  Write ${\cal D}_{H_t}={\cal K}'_{H_t}(0)$.  The same exact
transfer calculation as at the prime level, now with the odd modulus
$M=p^2$, gives



$$
\delta_M(n_t)\equiv-2{\cal D}_{H_t}q_{n_t-1}\pmod M.            \tag{4.2}
$$



For the fixed beta seed, the equality of the reflection quotient and the
index slope follows by combining exact reflection modulo $M^2$ with the
prime-power affine law.  Since adjacent beta denominators are coprime,
$q_{n_t-1}$ is a $p$-unit.  Consequently $p\mid{\cal D}_{H_t}$, and
(4.1)--(4.2) give



$$
\boxed{
 P'(t)\equiv
 -2(-1)^t{{\cal D}_{H_t}\over p}q_{n_t-1}\pmod p.}              \tag{4.3}
$$



For an upper member of a reflection pair, apply (4.3) to the lower member.
Formula (4.3) is the desired continuant interpretation of the second-level
ordinary/singular split.

At the base level, the analogous formula is



$$
\delta\equiv-2{\cal D}_{(p-3)/2-r}q_{r-1}\pmod p.
$$



It shows that first-level singularity forces one continuant derivative to
vanish modulo $p$.  It does **not** force $p^2\mid q_r$; the latter is
the independent fixed-seed condition $\lambda=0$.

## 5. Reflection coupling

The paired cubic is



$$
\boxed{P_s(T)=P_r(-1-T).}                                     \tag{5.1}
$$



Thus a root $t$ pairs with $t'=-1-t$, and



$$
P_s'(t')=-P_r'(t).                                             \tag{5.2}
$$



At the fourth-power layer the paired second digit is $u'=-1-u$.  Exact
reflection modulo $p^4$, followed by the legitimate division by $p^3$,
gives the refined constant relation



$$
\boxed{
 \widehat C_s(-1-t)=\widehat C_r(t)-P_r'(t).}                   \tag{5.3}
$$



Indeed,



$$
\widehat C_s(t')+u'P_s'(t')
 =\widehat C_r(t)+uP_r'(t).
$$



Hence the paired fibres have exactly the same fourth-power status.

## 6. Equal-valuation matching and CRT cost

Write the primitive mixed form as



$$
L=a+\varepsilon b\pi,\qquad \gcd(a,b)=1,
$$



and suppose first that $v_p(b)=2$.  Put



$$
\beta={b\over p^2}\in\mathbf Z_p^\times,
 \qquad s_0=(-1)^r.
$$



The beta-numerator period gives $p_{N(t,u)}\equiv p_r\pmod p$, while
$\varepsilon=s_0(-1)^{t+u}$.  The first final-content digit is therefore
controlled by



$$
\boxed{
 M(T)=\beta p_r-s_0aP(T)\in\mathbf F_p[T].}                     \tag{6.1}
$$



More precisely,



$$
p\mid P^*\quad\Longleftrightarrow\quad M(t)=0.                 \tag{6.2}
$$



This condition is independent of $u$.  At a root of $M$,



$$
P(t)=s_0\beta p_ra^{-1}\ne0,
$$



so $v_p(q_{N(t,u)})=2$ automatically: the matching digit is transverse
to the digit which lifts the denominator to $p^3$.

If $M\ne0$, let $c_p\leq3$ be its number of roots.  The matched indices
form exactly $c_p$ classes modulo $p^2$, or $c_p$ classes modulo
$2p^2$ after the required parity is imposed.  Equivalently, inside a
modulo-$p^3$ enumeration they occupy $c_pp$ classes because $u$ is
free.  Their absolute natural density is



$$
{c_p\over2p^2},
$$



or $c_p/p^2$ inside the prescribed parity class.  For distinct such
primes, CRT gives $\prod_pc_p$ classes modulo
$2\prod_pp^2$.  When $M\equiv0$, necessarily $P$ is the corresponding
nonzero constant, and all $p$ values of $t$ match; this is a further
exceptional all-lift alternative, not the generic cubic count.

For completeness, suppose instead that $v_p(b)=3$, and take a root
$P(t)=0$.  With $\beta_3=b/p^3$, the first matching digit at exact
denominator valuation three is



$$
\boxed{
 M_3(t,u)=\beta_3p_r-s_0a\{\widehat C_t+uP'(t)\}.}              \tag{6.3}
$$



If $P'(t)\ne0$, exactly one $u$ matches.  It is distinct from the
unique $u$ which raises the denominator to $p^4$, because at the latter
value the second term of (6.3) is zero while $\beta_3p_r\ne0$.  Thus one
parity-compatible class modulo $2p^3$ is selected.  If $P'(t)=0$ and
$\widehat C_t\ne0$, (6.3) is all or none in $u$, selecting a class
modulo $2p^2$ when it holds.  If $\widehat C_t=0$, every child has
valuation at least four, so equal valuation with an exact $p^3\parallel b$
fails and no final-content digit is gained.

## 7. Why an arbitrary modified seed is not an example

The symmetric transfer matrix and the identity
${\cal K}_h(2p)=2p{\cal D}_h+8p^3R_h(4p^2)$ are seed-independent.
The following ingredients are not:

* beta anti-periodicity and the all-even Newton laws;
* exact reflection $q_{M-1-n}\equiv q_n\pmod M$;
* the identification of a reflection quotient with an index slope;
* the companion-numerator period used in (6.1).

Therefore a recurrence solution manufactured by prescribing values near
$r$ cannot automatically be inserted into (2.4), (3.4), or (6.1).

The archived comparison $(p,h,r)=(107,2,50)$ illustrates the distinction.
Since ${\cal D}_2=963$ is divisible by $107$, prescribing
$u_{49}=1,u_{50}=107$ makes the reflected value satisfy
$u_{56}\equiv107\pmod {107^2}$.  But exact forward propagation gives



$$
u_{157}\equiv92\pmod {107}.
$$



Thus the reflected pair is singular in the continuant sense, while
$r+p=157$ is not even an index root modulo $107$.  This is a valid
recurrence/transfer countermodel, but it is not a noncentral all-lift orbit
of the actual beta denominator.

## 8. Remaining gaps

The formulas above do not prove any of the following:

1. existence of a noncentral fixed-seed orbit satisfying (1.1);
2. nonvanishing of $P$, simplicity of its roots, or nonvanishing of
   $\widehat C_t$ at a multiple root;
3. synchronization of roots of the matching polynomial (6.1) with the
   actual mixed-cubic coefficient $b_m$ at positive logarithmic mass;
4. a positive asymptotic rate from the exceptional all-lift cases.

Nothing here proves irrationality, rationality, or transcendence of
$e+\pi$.
