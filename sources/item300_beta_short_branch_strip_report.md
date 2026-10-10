> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 300 — the actual short strip and a sublinear-depth phase-blind no-go

Checked: 2026-08-31 (Beijing time)

## 1. Capacity-first verdict

Let



$$
q_0=q_1=1,\qquad
q_n=(4n-2)q_{n-1}+q_{n-2}\quad(n\ge2).               \tag{1.1}
$$



For $n\ge4$, put



$$
A=4n-2,\qquad
a=q_{n-1},\quad b=q_n,\quad c=q_{n-2},\quad d=q_{n-3}.
                                                               \tag{1.2}
$$



Then



$$
b=Aa+c,\qquad a=(A-4)c+d.                             \tag{1.3}
$$



With



$$
T_n=bc-a^2,\qquad
x_n=\frac{T_n}{b},\qquad
t_n=\operatorname{nint}(x_n),\qquad
r_n=bt_n-T_n,                                         \tag{1.4}
$$



the desired half-bound is



$$
|r_n|\ge\frac a2.                                     \tag{1.5}
$$



Item 300 does not prove (1.5), its stronger Item-295 version, or an
actual counterexample. It proves a global, sharply scoped no-go:

> **SUBLINEAR-DEPTH PHASE-BLIND AFFINE-STRIP NO-GO.**
> Suppose an argument retains only the exact affine updates for $x_j$,
> membership in the seed-specific strips $I_j$, and the moving
> denominator grids $q_j^{-1}\mathbb Z$, over a backward depth
> $L(n)=o(n)$. For every sufficiently large $n$, that model class
> contains two denominator-grid-compatible strip orbits with opposite
> current half-bound behavior: one has $r_n=-1$, while the other has
> $|r_n|=(q_n-1)/2$.

These witnesses are not the actual Turán numerator orbit. They preserve
the moving denominator grid and membership in every propagated strip,
but not the identity $T_j=q_jq_{j-2}-q_{j-1}^2$ as a fixed seed
numerator, and not necessarily primitive denominator at every earlier
level. Thus the theorem does not exclude linear-depth phase retention,
an exact seed congruence, a nonlinear invariant, or another arithmetic
argument.

Even a proof of the full-$b$ half-bound would not transfer as a lower
bound to a proper de-overlapped divisor $Q\mid b$. Item 282's product
baseline also remains separate. Therefore



$$
\boxed{
\text{new Route-1 rate}=0,\qquad
\text{new beta capacity reduction}=0.}                \tag{1.6}
$$



## 2. The normalized candidate state

Set



$$
\theta_n=\frac ca,\qquad
\theta_{n-1}=\frac dc,\qquad
y_n=\frac{x_n}{c},\qquad
s_n=\frac{r_n}{a}.                                    \tag{2.1}
$$



The ratio state closes:



$$
\boxed{
\theta_n=\frac1{A-4+\theta_{n-1}}.}                   \tag{2.2}
$$



Items 295 and 298 give



$$
x_n=\frac ab(4c-x_{n-1}).
                                                               \tag{2.3}
$$



Consequently



$$
\boxed{
y_n=
\frac{4-\theta_{n-1}y_{n-1}}{A+\theta_n}.}            \tag{2.4}
$$



The normalized seed-specific strip is



$$
\boxed{
\frac{4-\theta_{n-1}}{A}
<y_n<
\frac{5-\theta_{n-1}}{A+1}.}                          \tag{2.5}
$$



Moreover,



$$
s_n=(A+\theta_n)(t_n-x_n),                            \tag{2.6}
$$



so



$$
|r_n|\ge\frac a2
\iff
|s_n|\ge\frac12,                                      \tag{2.7}
$$



and the stronger target



$$
A(2|r_n|-a)\ge2c
$$



is equivalent to



$$
|s_n|\ge\frac12+\frac{\theta_n}{A}.                   \tag{2.8}
$$



The real ratio state is compact after scaling, but the centered phase
is not removed. If



$$
\operatorname{cent}(z)=z-\operatorname{nint}(z),
$$



then the exact centered update is



$$
\boxed{
s_{n-1}
=-\frac{
\operatorname{cent}(s_n-\theta_nt_n)
}{\theta_n}.}                                         \tag{2.9}
$$



Thus a proof needs the phase of $\theta_nt_n=ct_n/a$. The remaining
sections show that the real strip and any sublinear number of its affine
ancestors do not force this phase.

## 3. The actual strip and its integer width

Define



$$
I_n=(L_n,U_n),                                        \tag{3.1}
$$



where



$$
L_n=\frac{4c-d}{A},
\qquad
U_n=\frac{5c-d}{A+1}.                                 \tag{3.2}
$$



Item 295 proved



$$
x_n\in I_n.                                           \tag{3.3}
$$



The width is exact:



$$
\begin{aligned}
|I_n|
&=\frac{5c-d}{A+1}-\frac{4c-d}{A}\\
&=\frac{(A-4)c+d}{A(A+1)}\\
&=\boxed{\frac{a}{A(A+1)}}.                           \tag{3.4}
\end{aligned}
$$



At $n=5$,



$$
A=18,\qquad a=q_4=1001,\qquad
|I_5|=\frac{1001}{18\cdot19}>2.                       \tag{3.5}
$$



This persists. If $a>2A(A+1)$, then at the next row



$$
a'=b>Aa>2A^2(A+1)
>2(A+4)(A+5)                                          \tag{3.6}
$$



for $A\ge18$. Hence



$$
\boxed{|I_n|>2\quad(n\ge5).}                          \tag{3.7}
$$



The normalized interval (2.5) is short on the real scale, but the
unscaled nearest-integer digit sees $I_n$, whose width grows without
bound. The strip alone never forces $t_n$ from $n=5$ onward.

The exact margins around the actual point will be useful:



$$
\boxed{
x_n-L_n=\frac{ac}{Ab},\qquad
U_n-x_n=\frac{a(a-c)}{(A+1)b}.}                       \tag{3.8}
$$



They follow by substituting $x_n=c-a^2/b$ and $b=Aa+c$.

## 4. One affine ancestral strip lies strictly inside

Define the decreasing affine map



$$
F_n(z)=\frac ab(4c-z).                                \tag{4.1}
$$



Then



$$
x_n=F_n(x_{n-1}).                                     \tag{4.2}
$$



Let



$$
J_n=F_n(I_{n-1}).                                     \tag{4.3}
$$



Because $F_n$ is decreasing,



$$
J_n=\bigl(F_n(U_{n-1}),F_n(L_{n-1})\bigr).            \tag{4.4}
$$



Write $B=A-4$. At the previous row, the exact analogues of (3.8) are



$$
x_{n-1}-L_{n-1}=\frac{cd}{Ba},
\qquad
U_{n-1}-x_{n-1}=\frac{c(c-d)}{(B+1)a}.                \tag{4.5}
$$



Transporting them by $a/b$ gives



$$
x_n-F_n(U_{n-1})
=\frac{c(c-d)}{b(A-3)},                               \tag{4.6}
$$



and



$$
F_n(L_{n-1})-x_n
=\frac{cd}{b(A-4)}.                                   \tag{4.7}
$$



For the left endpoint, (3.8) and (4.6) reduce the desired strict
inclusion to



$$
\frac aA>\frac{c-d}{A-3}.                             \tag{4.8}
$$



Its cross-multiplied difference is



$$
(A-3)a-A(c-d)
=(A-2)(A-6)c+(2A-3)d>0.                              \tag{4.9}
$$



For the right endpoint, it is enough to note



$$
(A-4)a(a-c)
>(A-4)^2(A-5)c^2
>(A+1)cd                                              \tag{4.10}
$$



for $A\ge14$, using $a>(A-4)c$, $a-c>(A-5)c$,
and $d<c$. Therefore



$$
\boxed{F_n(I_{n-1})\subsetneq I_n\quad(n\ge4).}       \tag{4.11}
$$



The transported width is also exact:



$$
\boxed{
|J_n|
=\frac ab|I_{n-1}|
=\frac{ac}{b(A-4)(A-3)}.}                             \tag{4.12}
$$



For $n=8$, this is greater than $2$. A direct global proof follows
from



$$
\frac ab>\frac1{A+1}
$$



and



$$
c>2(A+1)(A-4)(A-3),                                  \tag{4.13}
$$



whose $n=8$ base is $A=30$, $c=q_6=398959$.
The latter inequality persists because $c'=a>(A-4)c$ and



$$
(A-4)^2(A-3)>A(A+5)\quad(A\ge30).                    \tag{4.14}
$$



Thus



$$
\boxed{|F_n(I_{n-1})|>2\quad(n\ge8).}                 \tag{4.15}
$$



Already one exact affine ancestor leaves more than a full centered
integer cell for every $n\ge8$.

## 5. Exact depth-$L$ transported strips

Let $1\le L\le n-3$, set $m=n-L$, and define



$$
J_{n,L}
=F_n\circ F_{n-1}\circ\cdots\circ F_{m+1}(I_m).       \tag{5.1}
$$



Repeated use of (4.11) gives



$$
J_{n,L}\subset I_n,                                   \tag{5.2}
$$



and every intermediate inverse state lies in its corresponding strip.

The derivative magnitudes telescope:



$$
\prod_{j=m+1}^{n}\frac{q_{j-1}}{q_j}
=\frac{q_m}{q_n}.                                     \tag{5.3}
$$



Using (3.4) at row $m$,



$$
\boxed{
|J_{n,L}|
=
\frac{q_mq_{m-1}}
{q_n(4m-2)(4m-1)}.}                                   \tag{5.4}
$$



This width diverges for every sublinear depth.

### The sublinear-depth estimate

Since



$$
q_j<(4j-1)q_{j-1},
$$



one has



$$
\frac{q_n}{q_m}
<
\prod_{j=m+1}^{n}(4j-1)
\le(4n+1)^L.                                          \tag{5.5}
$$



Also, for $m\ge6$,



$$
q_{m-1}
>7\prod_{j=3}^{m-1}(4j-2)
\ge(2m-2)^{\lfloor m/2\rfloor}.                       \tag{5.6}
$$



Equations (5.4)-(5.6) imply



$$
\boxed{
|J_{n,L}|
>
\frac{(2m-2)^{\lfloor m/2\rfloor}}
{(4n+1)^{L+2}}.}                                      \tag{5.7}
$$



Now let $L=L(n)=o(n)$. For all sufficiently large $n$,



$$
L\le\frac n4,\qquad m=n-L\ge\frac{3n}{4},
\qquad
\lfloor m/2\rfloor\ge\frac n3,                        \tag{5.8}
$$



and



$$
\log(2m-2)\ge\log n,\qquad
\log(4n+1)\le2\log n.                                 \tag{5.9}
$$



Because $L=o(n)$, eventually $L+2\le n/12$. Taking logarithms in
(5.7) then gives



$$
\log|J_{n,L}|
>
\frac n3\log n-\frac n6\log n
=\frac n6\log n.                                      \tag{5.10}
$$



Therefore



$$
\boxed{
L(n)=o(n)
\Longrightarrow
|J_{n,L(n)}|\longrightarrow\infty.}                  \tag{5.11}
$$



This is an explicit estimate, not an inference from bounded rows.

## 6. Opposite denominator-grid phases in the same propagated strip

Every open interval of length greater than $2$ contains a full
centered unit cell. Indeed, if $\mu$ is its midpoint and $k$ is a
nearest integer to $\mu$, then $|k-\mu|\le1/2$, while the half-width
is greater than $1$. Hence



$$
[k-\tfrac12,k+\tfrac12]\subset J_{n,L}.               \tag{6.1}
$$



For $b=q_n>2$, define two current states



$$
w_{\mathrm{close}}=k+\frac1b,                         \tag{6.2}
$$



and



$$
w_{\mathrm{far}}
=k+\frac{b-1}{2b}
=k+\frac12-\frac1{2b}.                                \tag{6.3}
$$



Both lie in the same cell (6.1), hence in $J_{n,L}\subset I_n$, and
both lie on the moving denominator grid $b^{-1}\mathbb Z$.
Their displayed denominators are primitive at the current row:



$$
\gcd(kb+1,b)=1,\qquad
\gcd\!\left(kb+\frac{b-1}{2},b\right)=1.              \tag{6.4}
$$



Their nearest-integer digit is $k$, so their centered numerators are



$$
\boxed{
r_{\mathrm{close}}=-1,\qquad
r_{\mathrm{far}}=-\frac{b-1}{2}.}                    \tag{6.5}
$$



For all rows in the theorem's range,



$$
1<\frac a2,\qquad \frac{b-1}{2}>\frac a2.             \tag{6.6}
$$



Thus the first state fails the half-bound and the second satisfies it.

The inverse affine maps preserve the denominator grids exactly. If



$$
w_j=\frac{N_j}{q_j},
$$



then



$$
\boxed{
w_{j-1}
=4q_{j-2}-\frac{q_j}{q_{j-1}}w_j
=
\frac{4q_{j-2}q_{j-1}-N_j}{q_{j-1}}.}                \tag{6.7}
$$



Since the two current states lie in $J_{n,L}$, their unique inverse
orbits lie in every corresponding strip $I_j$, and (6.7) places them
on every corresponding grid $q_j^{-1}\mathbb Z$.

The earlier displayed denominators may reduce. No claim of primitivity
at every level is made.

## 7. Exact scope of the no-go

Define a **depth-$L$ phase-blind affine-strip argument** to be one
whose admissible state class uses only:

1. the moving grids $w_j\in q_j^{-1}\mathbb Z$;
2. the strip memberships $w_j\in I_j$;
3. the affine relations $w_j=F_j(w_{j-1})$;
4. at most the rows $n-L,\ldots,n$;
5. no exact Turán numerator, seed-base identity, or additional
   congruence selecting one grid phase.

Sections 5-6 prove:



$$
\boxed{
L(n)=o(n)
\Longrightarrow
\text{this state class does not force the current half-bound}.}
                                                               \tag{7.1}
$$



The two model orbits satisfy every declared hypothesis and have
opposite conclusions.

This no-go does not apply to:

* the exact seed identity
  $T_j=q_jq_{j-2}-q_{j-1}^2$;
* a new congruence or nonlinear invariant selecting the actual phase;
* a history depth comparable to $n$, reaching the fixed base;
* an argument that proves primitivity or another arithmetic restriction
  at every intermediate row;
* a correctly rescaled arithmetic Lyapunov function outside the
  declared affine-strip class.

The first genuinely admissible remaining route is therefore a
seed-numerator or growing-depth phase invariant. The compact real state
$(\theta_n,y_n)$ alone is insufficient.

## 8. Proper targets and admission

For a proper de-overlapped target



$$
Q\mid b,\qquad Q>1,                                   \tag{8.1}
$$



the centered residue satisfies



$$
r_{n,Q}=\operatorname{cent}_Q(r_n),
\qquad
|r_{n,Q}|
\le\min\!\left\{|r_n|,\frac{Q-1}{2}\right\}.          \tag{8.2}
$$



Thus a full-$b$ lower bound would not transfer to $Q$. A full-$b$
upper construction would transfer, but Item 300 constructs only model
strip orbits, not the actual seed orbit.

Item 282's common coefficient/product baseline remains separate. Item
300 proves no proper-$Q$ bound, retained-capacity ceiling, or positive
weighted mass. Booking is zero.

## 9. Strict labels

### PROVED

* The normalized state equations (2.2)-(2.9).
* The exact strip width and margins (3.4), (3.8).
* The global digit-width theorem $|I_n|>2$ for $n\ge5$.
* The exact endpoint proof $F_n(I_{n-1})\subsetneq I_n$.
* The one-step transported width (4.12) and its $n\ge8$ lower bound.
* The depth-$L$ width formula (5.4).
* The explicit sublinear-depth divergence estimate (5.7)-(5.11).
* The two opposite current grid phases and inverse grid preservation.
* Proper-target lower-bound asymmetry and baseline separation.

### PROVED SCOPED NO-GO

* Sublinear-depth phase-blind affine-strip arguments, exactly as defined
  in Section 7, do not force the current half-bound on their declared
  model state class.
* This is a theorem about the declared model class, not an actual beta
  counterexample and not a general impossibility theorem.

### EXACT FINITE ONLY

* The checker replays bounded instances of the universal endpoint,
  inclusion, width, grid, inverse-orbit, and opposite-phase identities.
* It performs no actual half-bound scan, counterexample search, or
  exceptional-prime search.

### OPEN

* The all-$n$ actual half-bound.
* The stronger Item-295 inequality.
* An exact seed-numerator congruence or nonlinear phase invariant.
* A linear-depth or base-reaching phase argument.
* A large proper de-overlapped target residue theorem.
* The Item-282 product baseline and weighted-return cover.
* Route 1 and every conclusion about $e+\pi$.

### BOOKING



$$
\boxed{
\text{new Route-1 rate}=0,\qquad
\text{new beta capacity reduction}=0.}                \tag{9.1}
$$



## 10. Deterministic replay

From the archive root:

~~~text
python scripts/item300_beta_short_branch_strip_certificate.py ^
  --output results/item300_beta_short_branch_strip_certificate_replay.json
~~~

The checker uses only the Python standard library and exact integer or
rational comparisons. The canonical result and replay must be
byte-identical.
