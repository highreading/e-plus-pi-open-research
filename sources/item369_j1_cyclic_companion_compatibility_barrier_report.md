> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 369 — minimal cyclic companion for the joint fixed-$j=1$ gate and the compatibility barrier

Date: 2026-09-01

## 1. Outcome and capacity first

Work throughout on the actual fixed-$j=1$ selector



$$
p=4h+6s+3,\qquad M=3h+4s+2,\qquad
n=2h,\qquad r=2s+1.                                    \tag{1.1}
$$



Item 360 proved the one-way implication



$$
\text{full ordinary collision}
\Longrightarrow a_{r,n}=0,\quad Q_0(h,s)=0\pmod p.       \tag{1.2}
$$



Item 366 placed these two coordinates in separate framed entries of a
rank-five divided-Frobenius moment and proved that its ordinary conjugacy
invariants forget $Q_0$.

This item finds the minimal target-aware cyclic compression.  Over
$\mathbb F_{p^2}$, one exact rank-two complete moment is



$$
\boxed{
\mathcal C_{h,s}=
\begin{bmatrix}-a_{r,n}&-Q_0(h,s)\\1&0\end{bmatrix}.}    \tag{1.3}
$$



The fixed vector $e_1$ is cyclic on every row, and



$$
\boxed{
\chi_{\mathcal C}(X)=X^2+a_{r,n}X+Q_0,\qquad
-\operatorname {tr}\mathcal C=a_{r,n},qquad
\det\mathcal C=Q_0.}                                    \tag{1.4}
$$



Thus the two collision-forced values are recovered exactly as the two
coefficients of one cyclic characteristic polynomial.  Rank two is
minimal for universal exact characteristic-coordinate recovery.

This does **not** create a new independent divisor.  The determinant in
(1.4) is exactly the already forced transverse coordinate.  Moreover,
the construction is a target-aware additive companionization, not a
prime-independent Frobenius representation or compatible system.

Two exact barriers delimit what has and has not been gained.

1. On the open stratum where both nilpotent entries of Item 366's original
   rank-five matrix are nonzero, its unframed conjugacy class forgets their
   ratio and hence forgets whether their selected sum $-Q_0$ vanishes.
   No unframed functor of that conjugacy class can recover the gate.
2. A literal full-order Kummer realization of the finite-log factor has at
   least $p-2$ ramification points.  It therefore fails the bounded-support
   admission test.

The companion identity applies to every actual row, so its raw reach is



$$
{M\over6}+o(M),\qquad {1\over36}\text{ per }6M.           \tag{1.5}
$$



No horizontal trace-determinant nonconcentration theorem is proved.  Hence



$$
\boxed{
\text{new linear log rate}=0,\quad
\text{new fixed-}j=1\text{ capacity reduction}=0,\quad
\text{booking}=0.}                                       \tag{1.6}
$$



The $1/36$ ceiling is retained and Route 1 remains ACTIVE.

## 2. Exact local companion moment

Retain Item 366's notation



$$
G(x)=1-4x+6x^2-4x^3,qquad E=p-r,                        \tag{2.1}
$$





$$
P_0(x)=(1-x)^{2h}(1+x)(1+x^2)^{2s},                     \tag{2.2}
$$



and the finite logarithm



$$
\mathscr L_p(w)
={ (1+w)^p-1-w^p\over p}\pmod p.                        \tag{2.3}
$$



Set



$$
F_Q(x)=P_0(x)\mathscr L_p(x^2),                          \tag{2.4}
$$





$$
T=2h+6s+2,qquad L=4h+4s+2.                             \tag{2.5}
$$



Over $q=p^2$, define the local matrix



$$
\mathcal K_{h,s}(x)=
\begin{bmatrix}
x^{-n}G(x)^E&2x^{-T}F_Q(x)-x^{-L}F_Q(x)\\
-1&0
\end{bmatrix},qquad x\in\mathbb F_q^\times.           \tag{2.6}
$$



The degree inequalities from Item 366 isolate all three required
coefficients.  Specifically,



$$
\sum_{x\in\mathbb F_q^\times}x^{-n}G(x)^E=-a_{r,n},     \tag{2.7}
$$



and, if $c_N=[x^N]F_Q$,



$$
\sum_{x\in\mathbb F_q^\times}x^{-N}F_Q(x)=-c_N,
\qquad N=T,L.                                            \tag{2.8}
$$



Since $Q_0=2c_T-c_L$, the upper-right sum in (2.6) is
$-Q_0$.  Finally,



$$
\sum_{x\in\mathbb F_q^\times}(-1)=-(q-1)=1
\quad\text{in }\mathbb F_p.                             \tag{2.9}
$$



Therefore



$$
\boxed{
\mathcal C_{h,s}
=\sum_{x\in\mathbb F_q^\times}\mathcal K_{h,s}(x)
=\begin{bmatrix}-a_{r,n}&-Q_0\\1&0\end{bmatrix}.}      \tag{2.10}
$$



Equation (2.10) is an exact all-row finite-field identity.  The lower-left
entry is a fixed cyclic frame; no experimental fit or ambient period is
used.

## 3. Minimal cyclic/Krylov datum

For $e_1=(1,0)^t$,



$$
[e_1,\mathcal C e_1]
=\begin{bmatrix}1&-a_{r,n}\\0&1\end{bmatrix},qquad
\det[e_1,\mathcal C e_1]=1.                             \tag{3.1}
$$



Thus $e_1$ is uniformly cyclic, including on the joint-zero locus.  The
Krylov recurrence is the exact Cayley--Hamilton relation



$$
\boxed{
\mathcal C^2+a_{r,n}\mathcal C+Q_0I_2=0.}               \tag{3.2}
$$



The recurrence coefficients recover both target values.  Equivalently,
the coefficient map



$$
(a,Q_0)\longmapsto(-\operatorname {tr}\mathcal C,
                    \det\mathcal C)=(a,Q_0)              \tag{3.3}
$$



has Jacobian determinant $1$.

This is minimal in the following universal algebraic sense.  A rank-one
characteristic polynomial has only one coefficient $f(a,Q_0)$.  If both
$a$ and $Q_0$ could be recovered as rational functions of $f$, then
the transcendence-degree-two field $\mathbb Q(a,Q_0)$ would have
transcendence degree at most one, a contradiction.  Rank two supplies two
coefficients and (1.4) attains the lower bound.

Even if one asks only to detect the joint origin uniformly over an
algebraically closed coefficient field, one bounded-degree scalar equation
cannot have radical $\langle a,Q_0\rangle$: a nonzero principal ideal has
height at most one.  A prime-dependent finite-field indicator can evade
that statement only by using degrees growing with $p$; it is not a
uniform compatible-system datum.

Consequently the answer to the minimal-datum question is



$$
\boxed{
\text{one rank-two companion, one fixed cyclic vector, and its two}\\
\text{characteristic/Krylov coefficients}.}             \tag{3.4}
$$



## 4. Why Item 366's unframed matrix cannot supply the selector

Write Item 366's global rank-five matrix as



$$
\mathcal S(a,u,v)
=\operatorname {diag}\!\left(
-a,
\begin{bmatrix}0&u\\0&0\end{bmatrix},
\begin{bmatrix}0&v\\0&0\end{bmatrix}
\right),                                                 \tag{4.1}
$$



where



$$
u=-2c_T,qquad v=c_L,qquad u+v=-Q_0.                   \tag{4.2}
$$



Suppose $uv\ne0$.  With



$$
D(u,v)=\operatorname {diag}(1,u,1,v,1),                 \tag{4.3}
$$



direct multiplication gives



$$
D(u,v)^{-1}\mathcal S(a,u,v)D(u,v)
=\mathcal S(a,1,1).                                      \tag{4.4}
$$



Hence the entire unframed conjugacy class on this open stratum depends on
$a$ but not on the nonzero values of $u,v$.  In odd characteristic,



$$
(u,v)=(1,-1)\quad\text{and}\quad(1,1)                   \tag{4.5}
$$



give conjugate matrices, although the first has $Q_0=0$ and the second
has $Q_0=-2\ne0$.

Therefore



$$
\boxed{
\begin{gathered}
\text{no invariant depending only on the unframed conjugacy class of}\\
\mathcal S\text{ can recover the transverse relation on }uv\ne0.
\end{gathered}}                                          \tag{4.6}
$$



This includes traces, determinants, characteristic polynomials, Jordan
type on the open stratum, and every conjugacy-equivariant bounded-rank
functor followed by an unframed conjugacy invariant.  Bounded rank does not
repair lost framing.

The statement is genuinely relevant to the tied family.  On the
predeclared actual row



$$
(h,s,p)=(10,11,109),                                     \tag{4.7}
$$



one has



$$
(c_T,c_L)=(60,11),\qquad(u,v)=(98,11),\qquad
uv\ne0,\quad u+v=0.                                     \tag{4.8}
$$



Thus an actual transverse zero can lie in the generic nonzero Jordan
stratum; rank or Jordan type does not detect it.

The scope of (4.6) is exact but limited.  It is a universal functorial
no-go from the unframed matrix alone.  It does not exclude a new arithmetic
identity holding only on the actual tied orbit.  The companion (2.10)
escapes (4.6) precisely because it uses the chosen frame and the selected
linear combination $u+v$.

## 5. What the companion does and does not prove about Frobenius

The characteristic polynomial (1.4) has the formal shape one would want
from a rank-two Frobenius object.  In particular,



$$
a_{r,n}=Q_0=0
\quad\Longleftrightarrow\quad
\chi_{\mathcal C}(X)=X^2
\quad\Longleftrightarrow\quad
\mathcal C^2=0.                                          \tag{5.1}
$$



Thus a genuine compatible-system realization, together with a horizontal
nonconcentration theorem for simultaneous trace and determinant
divisibility, would be ledger-relevant.

But (2.10) is not such a realization.  It is an additive sum of local
matrices assembled after selecting the two target coefficient functionals.
The companion trick works for *every* ordered pair $(A,B)$:



$$
\begin{bmatrix}-A&-B\\1&0\end{bmatrix}
\quad\text{has}\quad X^2+AX+B.                          \tag{5.2}
$$



Therefore bounded rank and cyclicity alone add no arithmetic distribution
law.  No prime-independent coefficient field, lisse sheaf, crystalline
module, multiplicative Frobenius action, or compatible characteristic-zero
lift is constructed here.  The dependence on $p$ through
$\mathscr L_p$ is especially important.

The determinant $Q_0$ in (1.4) is consequently a *repackaged existing
divisor*, not a newly derived Frobenius divisor.  It receives no extra
codimension or mass credit.

## 6. Literal bounded-support Kummer construction fails

Item 366 proved



$$
\mathscr L_p'(w)={1-w^{p-1}\over1+w}.                    \tag{6.1}
$$



Every root of $\mathscr L_p$ has multiplicity at most two, so
$\mathscr L_p(z^2)$ has at least $p-2$ distinct roots over the
algebraic closure.  At each such root its multiplicity is one or two.
For every actual $p\ge13$, neither multiplicity is divisible by the
order $p-1$ of the base-field full Teichmüller character, nor by the
extension-field order $p^2-1$.

It follows that the literal full-order Kummer pullback along the finite-log
factor is ramified at every one of these roots.  Therefore



$$
\boxed{
\text{its finite conductor support has size at least }p-2.}             \tag{6.2}
$$



This rules out the direct fixed-support Kummer/black-box Weil route to a
uniform compatible system for the companion's upper-right entry.

The scope remains strict.  Equation (6.2) does not rule out a different
unipotent $F$-crystal, an Artin--Schreier description, cancellation of
apparent singularities, or another target-specific bounded-conductor
compression.  None is constructed here.

## 7. Declared exact controls

The deterministic certificate uses only four rows predeclared in Items
218, 342, 360, and 366.  There is no prime or collision scan.

| $(h,s,p)$ | $M$ | $(a_{r,n},Q_0)$ | $(c_T,c_L)$ | $(u,v)$ | finite-log roots |
|---|---:|---:|---:|---:|---:|
| $(1,1,13)$ | $9$ | $(0,9)$ | $(9,9)$ | $(8,9)$ | $10$ |
| $(2,1,17)$ | $12$ | $(8,14)$ | $(2,7)$ | $(13,7)$ | $16$ |
| $(8,2,47)$ | $34$ | $(0,30)$ | $(36,42)$ | $(22,42)$ | $46$ |
| $(10,11,109)$ | $76$ | $(70,0)$ | $(60,11)$ | $(98,11)$ | $106$ |

For each row the certificate independently verifies the integer selected
Hasse prefix, the finite-log convolution, the complete
$\mathbb F_{p^2}$ matrix sum (2.10), the characteristic coefficients,
the cyclic identity, and the finite-log root count.

The first and third rows are selected-Hasse separation controls.  The
fourth is a transverse-zero separation control and an actual witness for
(4.8).  No row is asserted to be a full collision or used as density
evidence.

## 8. Capacity audit and the exact remaining target

Define



$$
\mathcal W_{\rm cyc}(M)
=\sum_{\substack{s\in\mathcal S_M,\ p_s\ \mathrm{prime}\\
\operatorname {tr}\mathcal C_{h_s,s}=0\ (\mathrm{mod}\ p_s)\\
\det\mathcal C_{h_s,s}=0\ (\mathrm{mod}\ p_s)}}
\log p_s.                                                \tag{8.1}
$$



By (1.4), this is exactly Item 360's joint envelope:



$$
\mathcal W_{\rm cyc}(M)=\mathcal W_{H,Q}(M),             \tag{8.2}
$$



and



$$
\mathcal W_{\rm full}(M)\leq\mathcal W_{\rm cyc}(M).    \tag{8.3}
$$



All actual rows are reached, so the raw capacity remains



$$
\mathcal W_{\rm cyc}(M)\leq {M\over6}+o(M).              \tag{8.4}
$$



A theorem $\mathcal W_{\rm cyc}(M)=o(M)$ would remove the entire
fixed-$j=1$ ceiling.  A strict linear constant below $1/6$ per $M$
would already book a partial saving.

No such theorem follows from companionization.  The live input would have
to be one of:

- a genuine prime-independent bounded-conductor realization of (1.4);
- horizontal trace-determinant nonconcentration for the tied chosen primes;
- a framed extension-class distribution theorem; or
- an average-gcd theorem for the exact integer carriers of $a$ and
  $Q_0$.

Absent one of these, the full $1/36$ ceiling remains.

## 9. Strict decision

### PROVED

- the exact all-row rank-two cyclic companion moment (2.10);
- exact recovery of the Hasse and transverse coordinates as trace and
  determinant;
- universal rank-two minimality for exact characteristic-coordinate
  recovery;
- the unframed conjugacy-class no-go (4.6) for Item 366's rank-five matrix;
- the literal full-order finite-log Kummer bounded-support no-go (6.2);
- zero booking.

### EXACT FINITE ONLY

- four predeclared controls;
- an actual transverse zero in the generic nonzero nilpotent stratum;
- no collision scan, full-collision claim, or density inference.

### OPEN

- a genuine prime-independent bounded-conductor compatible system realizing
  $X^2+aX+Q_0$;
- an actual-orbit identity escaping the universal conjugacy obstruction;
- framed or trace-determinant horizontal nonconcentration;
- weighted joint-zero density, any strict fixed-$j=1$ ceiling reduction,
  Route 1, and every conclusion about $e+\pi$.

## 10. Ledger consequence



$$
\begin{array}{c|c}
\text{quantity}&\text{Item 369 value}\\ \hline
\text{actual rows reached}&\text{all}\\
\text{minimal cyclic rank}&2\\
\text{new independent collision condition}&0\\
\text{new proved excluded log mass}&0\\
\text{new fixed-}j=1\text{ capacity reduction}&0\\
\text{retained fixed-}j=1\text{ ceiling per }6M&1/36
\end{array}                                               \tag{10.1}
$$



Item 369 compresses the framed pair optimally but also shows why the
compression is not yet arithmetic progress: a universal companion matrix
can package any two values.  The unresolved theorem is compatibility and
horizontal nonconcentration, not rank reduction.
