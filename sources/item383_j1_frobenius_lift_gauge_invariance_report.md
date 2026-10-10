> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 383 — changing the Frobenius lift: a rational connection, but no bounded horizontal splitting

Date: 2026-09-01

## 1. Outcome and capacity first

The actual fixed-$j=1$ selector and one-way gate are unchanged:



$$
p=4h+6s+3,\quad M=3h+4s+2,
\quad n=2h,\quad r=2s+1,                    \tag{1.1}
$$





$$
\text{full ordinary collision}
\Longrightarrow a_{r,n}=0,\qquad Q_0=0\pmod p.          \tag{1.2}
$$



On the selected two-moment base put



$$
u=c_T,\qquad v=c_L,\qquad q=2u-v.                       \tag{1.3}
$$



Item 380 used the standard coordinatewise Frobenius and found an integral
horizontal connection which was neither rational nor overconvergent; its
formal splitting gauge had unbounded vertical $p$-poles.  This item asks
which conclusions survive a change of analytic coordinates and Frobenius
lift.

The answer has two parts.

1. **The literal lacunary/nonrational presentation is not invariant.**
   For every unit $\lambda\in\mathbb Z_p^\times$, there is an integral
   overconvergent Frobenius lift for which

   

$$
\boxed{\omega_\lambda={dq\over1-\lambda q}}          \tag{1.4}
$$



   is an exact flat horizontal connection.  It is rational, regular at the
   Hasse divisor $q=0$, and has only the fixed logarithmic pole
   $q=\lambda^{-1}$.  The pole lies on the unit boundary, so the
   resulting connection is still not dagger on the full closed moment
   disc.

2. **The bounded-splitting obstruction is invariant.**  For every
   Frobenius lift and every integral analytic coordinate change preserving
   the Hasse coordinate, no gauge in the bounded-denominator isocrystal
   ring can simultaneously split the connection and Frobenius.  The
   obstruction is the coordinate-invariant condition

   

$$
d\bar q=2\,d\bar u-d\bar v\ne0                       \tag{1.5}
$$



   in characteristic $p$.  A bounded splitting gauge would force
   $-\bar q$ to be a $p$-th power, contradicting (1.5).

3. **The global non-dagger obstruction is invariant.**  A flat dagger
   connection on the entire moment disc would have a dagger primitive by
   the dagger Poincare lemma.  Its gauge would reduce Frobenius to a
   constant extension, and a constant adjustment would give the forbidden
   bounded splitting equation.  Therefore every horizontal presentation
   has radius at most one somewhere on the full disc.  The single boundary
   pole in (1.4) is a sharp bounded-pole realization of this obstruction.

Thus Item 383 constructs a genuinely simpler bounded-pole horizontal
*connection*, but not a horizontal splitting of the filtered extension.
No weighted zero-density theorem or cross-prime geometric origin follows.

The fixed-$j=1$ ceiling remains $1/36$, new booking is zero, and Route
1 remains `ACTIVE`.

---

## 2. General Frobenius lifts and the horizontal equation

Let



$$
R=\mathbb Z_p[[u,v]],                                      \tag{2.1}
$$



and consider an arbitrary integral lift of absolute Frobenius



$$
F(u)=u^p+p\,a(u,v),\qquad
F(v)=v^p+p\,b(u,v).                                      \tag{2.2}
$$



The corrections may be bounded-degree polynomials or integral
overconvergent series.  Put



$$
C_F=p^{-1}F_\Omega^*.                                    \tag{2.3}
$$



The Item 374 Frobenius matrix remains



$$
A_q=\begin{bmatrix}p&0\\pq&1\end{bmatrix}.              \tag{2.4}
$$



The general calculation from Item 377 is independent of the chosen lift.
Whenever a lower horizontal connection exists, its one-form $\omega$
must satisfy



$$
\boxed{C_F(\omega)-\omega=dq.}                           \tag{2.5}
$$



Indeed, for every integral lift (2.2),
$F_\Omega^*(\Omega^1_R)\subset p\Omega^1_R$.  In any bounded or dagger
connection the other three entries in the general Item 377 matrix still
satisfy the same contracting equations and hence vanish.  Thus (2.5)
covers every bounded/dagger horizontal connection in this architecture,
not merely an ansatz chosen for the construction below.

At the closed point, let $J$ be the linear action induced by $C_F$ on
the cotangent space.  The constant cotangent term of (2.5) is



$$
(J-I)\omega_0=dq.                                        \tag{2.6}
$$



This gives the basic lift classification.

- If $C_F$ is adically topologically nilpotent, (2.5) has the unique
  Item 377 resolvent solution $-\sum_{j\ge0}C_F^j(dq)$.
- If $1$ is resonant in the relevant cotangent direction, (2.6) may
  obstruct existence or create nonuniqueness.
- A noncontracting lift can nevertheless have an explicit rational
  solution; Section 3 constructs one.

None of these alternatives changes the Frobenius equation for a
simultaneous splitting gauge, treated in Section 4.

---

## 3. An explicit rational logarithmic horizontal model

Use the linear coordinates



$$
q=2u-v,\qquad t=v.                                       \tag{3.1}
$$



Fix $\lambda\in\mathbb Z_p^\times$ and define



$$
\Phi_\lambda(q)
={1-(1-\lambda q)^p\exp(-\lambda p q)\over\lambda},
\qquad F(t)=t^p.                                         \tag{3.2}
$$



Because $p$ is odd,



$$
v_p\!\left({(\lambda p)^m\over m!}\right)
\ge m-v_p(m!)\longrightarrow+\infty                    \tag{3.3}
$$



linearly in $m$.  Hence the exponential in (3.2) is integral and
overconvergent.  Moreover,



$$
\Phi_\lambda(q)\equiv q^p\pmod p.                       \tag{3.4}
$$



Thus (3.2) is a genuine overconvergent lift of Frobenius.

Returning to $(u,v)$, set



$$
F(v)=v^p,qquad
F(u)={\Phi_\lambda(2u-v)+v^p\over2}.                    \tag{3.5}
$$



Then



$$
F(u)=u^p+p\,a_\lambda(u,v),\qquad F(v)=v^p,             \tag{3.6}
$$



with $a_\lambda$ integral and overconvergent.  Therefore this lies in
the class requested in (2.2), although it is not a bounded-degree
polynomial lift.

The defining identity



$$
1-\lambda\Phi_\lambda(q)
=(1-\lambda q)^p\exp(-\lambda p q)                      \tag{3.7}
$$



gives, after logarithmic differentiation,



$$
{d\Phi_\lambda(q)\over
 p(1-\lambda\Phi_\lambda(q))}
={dq\over1-\lambda q}+dq.                               \tag{3.8}
$$



Consequently



$$
C_F(\omega_\lambda)-\omega_\lambda=dq,
\qquad
\omega_\lambda={dq\over1-\lambda q}.                  \tag{3.9}
$$



The connection $E_{21}\omega_\lambda$ is flat because
$d\omega_\lambda=0$ and $E_{21}^2=0$.  It is rational, regular at
$q=0$, and logarithmic along the single fixed divisor
$1-\lambda q=0$.

This construction proves that Item 380's specific lacunary and
nonrational form is not invariant under changing the Frobenius lift.  It
also gives a bounded algebraic pole set.  However, the pole lies on the
unit boundary, so the power series $(1-\lambda q)^{-1}$ is not dagger on
the entire closed unit disc.  It defines the usual rational logarithmic
connection on the open complement of that divisor.

---

## 4. Coordinate- and lift-invariant no bounded splitting theorem

Let $F$ be **any** integral Frobenius lift on $R$.  An unfiltered lower
unipotent gauge



$$
G=U(f)=\begin{bmatrix}1&0\\f&1\end{bmatrix}             \tag{4.1}
$$



changes full Frobenius by



$$
G^{-1}A_qF(G)
=U\!\left(-f+q+{F(f)\over p}\right)
\begin{bmatrix}p&0\\0&1\end{bmatrix}.                 \tag{4.2}
$$



Therefore simultaneous splitting requires



$$
{F(f)\over p}-f=-q.                                     \tag{4.3}
$$



Suppose $f\in R[1/p]$.  Write



$$
f=p^m g,                                                 \tag{4.4}
$$



where $m\in\mathbb Z$ is the minimum coefficient
valuation and $g\in R$ is primitive modulo $p$.  Equation (4.3)
becomes



$$
p^{m-1}F(g)-p^m g=-q.                                   \tag{4.5}
$$



Because $q=2u-v$ is primitive, valuation comparison forces $m=1$.
Reducing (4.5) modulo $p$ then gives



$$
\bar g^p=-\bar q.                                      \tag{4.6}
$$



But $p$-th powers have zero Kähler differential, while



$$
d\bar q=2\,d\bar u-d\bar v\ne0.                        \tag{4.7}
$$



This contradiction proves



$$
\boxed{\text{no }f\in R[1/p]\text{ solves (4.3) for any Frobenius lift.}} \tag{4.8}
$$



The proof uses only the reduction of $F$ to absolute Frobenius and the
nonzero differential of the Hasse coordinate.  Both are invariant under
integral analytic coordinate changes.  Hence (4.8) survives every such
change preserving $q$, and more generally every change sending $q$ to
a coordinate with nonzero differential modulo $p$.

The statement also covers general bounded matrix gauges.  An isomorphism
from $A_q$ to the split Frobenius $\operatorname {diag}(p,1)$ satisfies



$$
A_qF(G)=G\operatorname {diag}(p,1).                      \tag{4.9}
$$



The bounded off-diagonal equations force the upper-right entry to vanish;
the lower-left entry, divided by a nonzero constant diagonal entry, obeys
(4.3).  Thus a non-unipotent bounded gauge cannot evade (4.8).

There is a useful global consequence.  Suppose that some lift admitted a
flat dagger lower connection on the entire two-variable closed disc.  The
dagger Poincare lemma would give a dagger function $f$ with
$df=-\omega$.  Gauging by $U(f)$ makes the connection trivial, so
Frobenius horizontality makes



$$
-f+q+{F(f)\over p}=\kappa                              \tag{4.10}
$$



constant.  A constant gauge adjustment solves away $\kappa$, since
$c/p-c=-\kappa$ has a solution $c\in\mathbb Q_p$.  This produces
(4.3), contradicting (4.8).  Hence



$$
\boxed{\text{no Frobenius lift admits a horizontal dagger connection on
the whole moment disc.}}                                \tag{4.11}
$$



In particular, the non-overconvergence/radius-one barrier is invariant in
this global sense, even though rationality and lacunarity are not.

---

## 5. Allowed filtered gauges are even more rigid

The fixed filtration is



$$
\operatorname {Fil}^1=Re_1.                             \tag{5.1}
$$



A filtration-preserving gauge is upper triangular in the Item 374 basis.
If it trivialized a lower connection $E_{21}\omega$, the fundamental
matrix equation



$$
dG=-E_{21}\omega G                                     \tag{5.2}
$$



would force the lower-left entry to have derivative $-\omega g_{11}$.
Upper triangularity makes that entry identically zero, while invertibility
makes $g_{11}\ne0$.  Hence a filtered splitting would require
$\omega=0$, which contradicts (2.5) because $dq\ne0$.

Thus:

- no filtration-preserving gauge splits the horizontal extension, even in
  the enlarged formal coefficient ring;
- after forgetting the filtration, a formal splitting may exist, but
  (4.8) shows it cannot have uniformly bounded $p$-poles.

The rational connection in Section 3 illustrates this exactly.  Its
formal primitive is



$$
f_\lambda=\lambda^{-1}\log(1-\lambda q),                \tag{5.3}
$$



for which $df_\lambda=-\omega_\lambda$.  The coefficients
$\lambda^{n-1}/n$ have unbounded negative $p$-adic valuations along
$n=p^j$, so $f_\lambda\notin R[1/p]$, in agreement with (4.8).

---

## 6. What is and is not invariant

The exact classification needed for research management is:

| Feature | Invariant under allowed lift/coordinate change? | Result |
|---|---:|---|
| Item 380's particular lacunary/nonrational formula | No | replaced by the rational form (1.4) |
| Failure of dagger overconvergence on the full moment disc | Yes | follows from (4.10)--(4.11) |
| Existence of a bounded-dimensional formal model | Yes | rank two on two moment coordinates |
| No filtered splitting when $dq\ne0$ | Yes | follows from (5.2) |
| No bounded-denominator unfiltered Frobenius splitting | Yes | follows from (4.5)--(4.8) |
| Geometric conductor of the actual tied family | Not determined | no prime-independent actual-family descent is constructed |

The Section 3 construction improves the local presentation but remains
tautological in the Hasse coordinate $q$.  It accepts every value of
$q$, uses no second target-forced condition, and does not control the
moving map $(h,s)\mapsto(c_T,c_L)$.

---

## 7. Capacity and strategic conclusion

The rational logarithmic model does not supply a Frobenius trace,
monodromy distribution, or splitting-prime theorem for the actual tied
rows.  The invariant (4.8) in fact says that the extension cannot be
reduced to a bounded split compatible system by changing only the lift and
coordinates.

Accordingly:

- no weighted nonconcentration theorem is proved;
- no strict fixed-$j=1$ ceiling reduction is proved;
- the retained ceiling is $1/36$;
- new booking is $0$;
- Route 1 remains `ACTIVE`.

The next admissible step would need new global arithmetic structure, not
another local Frobenius lift.  In particular, it must connect the actual
moving finite-log moments across primes and produce a horizontal statistic
whose zero set can be counted.

---

## 8. Strict labels

### PROVED

1. General lift equation $C_F(\omega)-\omega=dq$.
2. Explicit integral overconvergent lift (3.2)--(3.6) with rational
   logarithmic horizontal connection (1.4).
3. The Item 380 literal lacunary/nonrational connection is not
   lift-invariant, while global non-dagger behavior is invariant.
4. Coordinate- and lift-invariant no bounded-denominator simultaneous
   splitting theorem (4.8).
5. No global dagger horizontal connection on the full moment disc.
6. No filtration-preserving horizontal splitting when $dq\ne0$.
7. Zero booking and retained $1/36$ ceiling.

### DECLARED EXACT CONTROLS ONLY

The deterministic certificate verifies the Frobenius congruence,
logarithmic derivative, matrix gauge equation, valuation lemma, and
declared truncations of the exponential and logarithm.  These are exact
algebraic controls, not a prime or collision census.

### OPEN

1. A prime-independent geometric realization of the actual tied
   $(h,s)\mapsto(c_T,c_L)$ family.
2. Whether a different nonsplit dagger presentation on another global
   base yields a useful monodromy statistic.
3. Any genuine geometric conductor or weighted splitting-prime theorem.
4. Weighted joint-zero density, a strict fixed-$j=1$ ceiling reduction,
   Route 1, and every conclusion about $e+\pi$.
