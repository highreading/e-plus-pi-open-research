> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 380 — exact moment pullback and the horizontal gauge-complexity barrier

Date: 2026-09-01

## 1. Outcome and capacity screen

The actual fixed-$j=1$ selector remains



$$
p=4h+6s+3,\qquad M=3h+4s+2,
\qquad n=2h,\qquad r=2s+1.                    \tag{1.1}
$$



The only gate used here is



$$
\text{full ordinary collision}
\Longrightarrow a_{r,n}=0,\qquad Q_0(h,s)=0\pmod p.    \tag{1.2}
$$



Item 377 proved that the Item 374 rank-two filtered Hasse extension has a
unique flat horizontal connection for every formal Hasse coordinate
$q$.  This item pulls that connection back to the exact two selected
finite-log moments



$$
u=c_T,\qquad v=c_L,\qquad q=2u-v,             \tag{1.3}
$$



where



$$
T=2h+6s+2,\qquad L=4h+4s+2.                  \tag{1.4}
$$



There are two complementary conclusions.

1. **Bounded-dimensional formal descent exists.**  On
   $R=W(k)[[u,v]]$, with $F(u)=u^p$ and $F(v)=v^p$, the unique
   connection has the uniform exact formula

   

$$
\boxed{
   \omega_{u,v}
   =-2\sum_{j\ge0}u^{p^j-1}du
     +\sum_{j\ge0}v^{p^j-1}dv.}              \tag{1.5}
$$



   Thus dimension or rank alone cannot obstruct a two-moment packaging.

2. **No bounded-pole algebraic splitting exists for this descent.**  In
   the larger formal coefficient ring allowing unbounded $p$-adic
   denominators, put

   

$$
f_{u,v}
   =\sum_{j\ge0}{2u^{p^j}-v^{p^j}\over p^j}. \tag{1.6}
$$



   Then $df_{u,v}=-\omega_{u,v}$, and the unipotent gauge
   $U(f_{u,v})$ simultaneously trivializes the connection and changes
   full Frobenius to $\operatorname {diag}(p,1)$.  But the coefficients
   of $u^{p^j}$ and $v^{p^j}$ have valuations exactly $-j$.
   Consequently $f_{u,v}\notin R[1/p]$, no fixed $p$-power clears
   the gauge, and no rational or overconvergent gauge makes the connection
   rational or overconvergent.

This is a sharp obstruction for the **direct standard-Frobenius
two-moment descent**.  It is not a lower bound for the geometric conductor
of every possible realization of the discrete actual family.

The ambient pointwise product still has $p^2-O(p)$ nonidentity factors,
but after pullback to any two-parameter base its cotangent rank is at most
two.  Therefore the ambient independent-direction count cannot be booked
as an actual conductor lower bound.

No weighted zero-density theorem follows.  The raw ceiling remains



$$
\Gamma_{j=1}^{\max}={1\over36},              \tag{1.7}
$$



and the new booking is zero.

---

## 2. Exact pullback of the unique horizontal connection

Let



$$
R=W(k)[[u,v]],\qquad F(u)=u^p,\quad F(v)=v^p,             \tag{2.1}
$$



and let



$$
C=p^{-1}F_\Omega^*.                                     \tag{2.2}
$$



For $q=2u-v$,



$$
C^j(dq)=2u^{p^j-1}du-v^{p^j-1}dv.                       \tag{2.3}
$$



Substitution into Item 377's resolvent



$$
\omega_q=-\sum_{j\ge0}C^j(dq)                          \tag{2.4}
$$



gives (1.5).  In the Item 374 basis, the connection and full Frobenius are



$$
\Gamma_q=E_{21}\omega_q,
\qquad
A_q=\begin{bmatrix}p&0\\pq&1\end{bmatrix}
=U(q)\begin{bmatrix}p&0\\0&1\end{bmatrix}.             \tag{2.5}
$$



The formula is uniform in $p$ as a Mahler/Frobenius equation, but its
power-series exponents depend on $p$.  It is a bounded-*description*
formal descent, not an algebraic family of bounded degree.

The two variables in (2.1) are the selected complete moments themselves.
Evaluating $(u,v)$ at the actual pair $(c_T,c_L)$ recovers $Q_0$.
This evaluation alone does not construct a Frobenius-equivariant morphism
from the full pointwise finite-log family: linear moment formation and a
chosen coordinatewise Frobenius lift need not commute over $W(k)$.
Accordingly, (2.1) must be labeled a direct moment-coordinate model, not
a descent theorem for the original pointwise geometry.

---

## 3. The unique simultaneous splitting gauge

Define the enlarged $(u,v)$-adic formal series



$$
f_q:=\sum_{j\ge0}p^{-j}F^j(q)
=\sum_{j\ge0}{2u^{p^j}-v^{p^j}\over p^j}.               \tag{3.1}
$$



Termwise differentiation gives



$$
df_q
=2\sum_{j\ge0}u^{p^j-1}du
-\sum_{j\ge0}v^{p^j-1}dv
=-\omega_q.                                             \tag{3.2}
$$



It also satisfies the exact Frobenius-difference equation



$$
{F(f_q)\over p}-f_q=-q.                                 \tag{3.3}
$$



Let $G_q=U(f_q)$, where



$$
U(t)=\begin{bmatrix}1&0\\t&1\end{bmatrix}.             \tag{3.4}
$$



The connection gauge rule gives



$$
G_q^{-1}\Gamma_qG_q+G_q^{-1}dG_q
=E_{21}(\omega_q+df_q)=0.                               \tag{3.5}
$$



For semilinear Frobenius,



$$
G_q^{-1}A_qF(G_q)
=U\!\left(-f_q+q+{F(f_q)\over p}\right)
 \begin{bmatrix}p&0\\0&1\end{bmatrix}
=\begin{bmatrix}p&0\\0&1\end{bmatrix}.                \tag{3.6}
$$



So the horizontal filtered extension is formally split after forgetting
the filtration and admitting the enlarged gauge (3.1).

This gauge is forced.  If a matrix $G$ trivializes the connection, then



$$
dG=-\Gamma_qG.                                          \tag{3.7}
$$



Writing $G=(g_{ij})$, its top row is constant and each lower entry is a
constant plus the corresponding top-row constant times $f_q$.  Since
an invertible matrix has a nonzero top row, every fundamental gauge
contains a nonzero constant multiple of $f_q$.  Thus the pole behavior
below cannot be avoided by using a non-unipotent gauge.

A gauge which preserves the fixed filtration line $Re_1$ cannot even
perform the formal splitting when $dq\ne0$: its first column would force
the lower component in (3.7) to vanish, contradicting $df_q=-\omega_q$.

---

## 4. Sharp unbounded-denominator theorem

For every $j\ge0$, the coefficient of $u^{p^j}$ in $f_q$ is



$$
{2\over p^j},                                           \tag{4.1}
$$



and the coefficient of $v^{p^j}$ is



$$
-{1\over p^j}.                                          \tag{4.2}
$$



All actual primes here are odd, so



$$
v_p(2/p^j)=v_p(-1/p^j)=-j.                              \tag{4.3}
$$



It follows that



$$
f_q\notin R[1/p]
=\bigcup_{B\ge0}p^{-B}R.                                \tag{4.4}
$$



Equivalently, no integer $B$, independent of Frobenius level, makes
$p^Bf_q$ integral.  By the forced-gauge calculation after (3.7), no
fundamental gauge with a uniformly bounded vertical $p$-pole exists.

More generally, suppose a Hasse coordinate $q$ has a unit coefficient
at a monomial whose exponent vector is not divisible by $p$.  Along its
Frobenius orbit, the primitive (3.1) has coefficients of valuation $-j$
for all sufficiently large $j$; integral higher orbit terms cannot
cancel the primitive unit modulo $p$.  Thus the same no-go applies to
any pullback with a unit primitive monomial.  The actual two-moment model
has two such linear monomials.

This is a vertical denominator theorem.  It is not, by itself, a Swan,
Artin, or geometric conductor theorem.

---

## 5. Rational and overconvergent no-go

Restrict (1.5) to $v=0$.  Its $du$-coefficient is



$$
-2\sum_{j\ge0}u^{p^j-1}.                                \tag{5.1}
$$



This series is not rational over $W(k)[1/p](u)$.  Indeed, the Taylor
coefficients of a rational function regular at the origin satisfy an
eventual constant-coefficient linear recurrence.  A nonzero such sequence
cannot contain arbitrarily long blocks of zeros followed by a nonzero
term.  The support $\{p^j-1:j\ge0\}$ has precisely those growing gaps.

The same series is not overconvergent: its nonzero coefficients are units,
so its radius of convergence is exactly one, not strictly greater than
one.  Therefore $\Gamma_q$ is neither rational nor overconvergent on the
standard moment-coordinate disc.

These properties are invariant under rational or overconvergent gauge in
the needed direction.  If both a gauge $G$ and the transformed
connection were in the rational (respectively overconvergent) category,
then



$$
\Gamma_q
=G\Gamma'G^{-1}-dG\,G^{-1}                       \tag{5.2}
$$



would be in that category as well, a contradiction.  Hence:



$$
\boxed{\text{no rational or overconvergent gauge makes the direct
two-moment connection rational or overconvergent.}}       \tag{5.3}
$$



This rules out the most literal bounded-pole/dagger realization of the
Item 377 connection.  A different geometric construction, a different
base, or additional cancellation after actual specialization is not ruled
out.

---

## 6. Why the $p^2-O(p)$ ambient support is not an actual conductor bound

On the independent pointwise coefficient base, put



$$
q=y_1+\cdots+y_N,qquad
N\ge p^2-1-\{4+2(p-1)+2|h-s|\}.                         \tag{6.1}
$$



Then



$$
\omega_q
=-\sum_{i=1}^N\sum_{j\ge0}y_i^{p^j-1}dy_i,             \tag{6.2}
$$



and the simultaneous splitting primitive is



$$
f_q=\sum_{i=1}^N\sum_{j\ge0}{y_i^{p^j}\over p^j}.      \tag{6.3}
$$



Thus all $N=p^2-O(p)$ directions have the same exact vertical
denominator obstruction on the **independent ambient base**.

The actual finite-log values are not independent coordinates.  Pullback
to any two-parameter $(h,s)$ or $(u,v)$ base sends their cotangent
space to a module of rank at most two:



$$
\operatorname {rank}\operatorname {im}
\bigl(\langle dy_1,\ldots,dy_N\rangle
\longrightarrow\Omega^1_{\mathrm{base}}\bigr)\le2.     \tag{6.4}
$$



Moreover, the actual selected condition uses only the global combination
$q=2c_T-c_L$.  Therefore (6.1) cannot be turned into a lower bound
$\operatorname {cond}\gg p^2$ after specialization.  The sharp proved
actual-moment statement is (4.4), not a growing geometric conductor.

This also explains the limitation of the literal finite-log expression.
The polynomial $\mathscr L_p(x^2)$ has $p-1$ nonzero terms and moving
degree, so the direct coefficient-extraction formula is not uniformly
bounded as written.  No theorem here excludes an undiscovered identity
which compresses those terms after the tied $(h,s)$ specialization.

---

## 7. Strategic conclusion

Item 380 separates three notions which had been at risk of conflation.

1. The filtered connection has a **bounded-dimensional formal**
   two-moment description.
2. Its direct standard-Frobenius realization has **unbounded vertical
   gauge denominators** and is neither rational nor overconvergent.
3. The $p^2-O(p)$ ambient coefficient support gives **no proved
   geometric conductor lower bound** after actual specialization.

Accordingly, the natural direct descent is too formal to support a
bounded-conductor Chebotarev or monodromy argument, but no global no-go for
all possible geometric descents has been proved.

The remaining admissible target is a genuinely new identity or geometric
model that simultaneously:

- descends the moving finite-log coefficients to a prime-independent
  bounded-complexity base;
- avoids the unbounded-denominator Mahler primitive (3.1); and
- proves weighted nonconcentration for the actual splitting locus.

No such model is constructed here.  The $1/36$ ceiling is unchanged,
new booking is $0$, and Route 1 remains `ACTIVE`.

---

## 8. Strict labels

### PROVED

1. Exact two-moment connection formula (1.5).
2. Exact simultaneous formal splitting gauge (3.1)--(3.6).
3. No bounded-$p$-pole fundamental gauge in the natural coefficient
   ring.
4. Nonrationality and non-overconvergence of the direct moment connection,
   and the corresponding rational/dagger gauge no-go.
5. Ambient $p^2-O(p)$ coefficient support collapses to cotangent rank at
   most two after a two-parameter pullback.
6. Zero booking and retained $1/36$ ceiling.

### DECLARED EXACT CONTROLS ONLY

The certificate checks the gauge identities, denominator valuations,
Mahler truncations, lacunary gaps, and cotangent-rank algebra on declared
symbolic or finite-depth controls.  It performs no prime or collision
scan and draws no asymptotic conclusion from those controls.

### OPEN

1. Whether the actual tied $(h,s)$ coefficient map admits a different
   prime-independent bounded-complexity geometric descent.
2. Any genuine geometric conductor lower bound after actual
   specialization.
3. Any cancellation or compression special to the moving finite-log
   coefficients.
4. Weighted joint-zero density, a strict fixed-$j=1$ ceiling reduction,
   Route 1, and every conclusion about $e+\pi$.

