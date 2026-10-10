> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 298 — exact centered beta dynamics and the primitive contraction obstruction

Checked: 2026-08-31 (Beijing time)

## 1. Capacity-first verdict

Let



$$
q_0=q_1=1,\qquad
q_n=(4n-2)q_{n-1}+q_{n-2}\quad(n\ge2).               \tag{1.1}
$$



For $n\ge3$, write



$$
A=4n-2,\qquad
a=q_{n-1},\quad b=q_n,\quad c=q_{n-2},\quad d=q_{n-3},
\qquad b=Aa+c.                                         \tag{1.2}
$$



Define the Turán numerators



$$
T_n=bc-a^2,\qquad T_{n-1}=ad-c^2.                    \tag{1.3}
$$



Item 295 proved



$$
T_n+T_{n-1}=4ac.                                      \tag{1.4}
$$



Let



$$
t_n=\operatorname{nint}\!\left(\frac{T_n}{b}\right),
\qquad
r_n=bt_n-T_n,\qquad \rho_n=|r_n|.                    \tag{1.5}
$$



Thus $r_n$ is the centered remainder, with



$$
-\frac b2<r_n<\frac b2.                               \tag{1.6}
$$



Item 298 proves four exact structural facts.

1. The pair $(r_n,t_n)$ factors through the single rational state
   $w_n=T_n/b$. The state has an exact affine update.
2. The induced centered two-coordinate update is an exact bijection,
   with an explicit inverse.
3. On the actual orbit, the natural forward carry is negative from
   $n=6$ onward and tends to $-\infty$. It cannot be discarded as
   a uniformly bounded centering error.
4. The affine update, even together with primitive denominators and a
   nearly maximal previous centered remainder, can produce the next
   remainder $r=-1$. Hence real contraction, the recurrence, and
   coprimality alone cannot prove the actual-family half-bound.

The fourth statement is a scoped method obstruction. Its witnesses are
not asserted to be the actual Bessel/Turán orbit: they need not satisfy
the short positive interval occupied by the actual digit $t_n$.

No proof or counterexample for



$$
\rho_n\ge\frac a2                                    \tag{1.7}
$$



is obtained. A full-$b$ lower bound would still not descend to a
proper de-overlapped divisor $Q\mid b$, and Item 282's product
baseline remains separate. Therefore



$$
\boxed{
\text{new Route-1 rate}=0,\qquad
\text{new beta capacity reduction}=0.}                \tag{1.8}
$$



## 2. Unique centering

Every $q_j$ is odd, and adjacent terms are coprime. In particular,



$$
\gcd(a,b)=\gcd(a,c)=1,\qquad
a,b,c\ \text{are odd}.                                \tag{2.1}
$$



If an integer divided by $a$ or $b$ were a strict half-integer,
an even integer would equal an odd integer. Hence all nearest integers
below are unique. Write



$$
\operatorname{cent}_M(x)
=x-M\operatorname{nint}(x/M)                          \tag{2.2}
$$



for the centered representative modulo an odd positive $M$.

The relation with Item 295's notation is exact. If



$$
\kappa_n=\operatorname{nint}(a^2/b),
$$



then $t_n=c-\kappa_n$, and



$$
bt_n-T_n
=b(c-\kappa_n)-(bc-a^2)
=a^2-\kappa_nb.                                      \tag{2.3}
$$



Thus (1.5) is precisely the same centered beta remainder.

## 3. One rational coordinate carries the pair

Put



$$
w_n=\frac{T_n}{b}.                                   \tag{3.1}
$$



Then



$$
\boxed{
t_n=\operatorname{nint}(w_n),\qquad
r_n=b(t_n-w_n),\qquad
w_n=t_n-\frac{r_n}{b}.}                               \tag{3.2}
$$



Consequently one rational coordinate, with its known moving
denominator $b$, carries both centered coordinates.

From (1.4),



$$
\boxed{
w_{n-1}
=4c-\frac ba w_n.}                                   \tag{3.3}
$$



Conversely,



$$
\boxed{
w_n=\frac ab(4c-w_{n-1}).}                            \tag{3.4}
$$



This is the smallest evident closed state: the two integer coordinates
are the nearest-integer digit and centered fractional part of one
rational number. No categorical minimality beyond this explicit
rank-one factorization is claimed.

The half-bound is an integer-distance condition. With



$$
\|x\|_{\mathbb Z}=\min_{m\in\mathbb Z}|x-m|,
\qquad \lambda_n=\frac ba=A+\frac ca,
$$



one has



$$
\boxed{
\rho_n=b\|w_n\|_{\mathbb Z},\qquad
\rho_n\ge\frac a2
\iff
\|w_n\|_{\mathbb Z}\ge\frac1{2\lambda_n}.}            \tag{3.5}
$$



Equation (3.4) is a contraction on the real line, with slope
$a/b<1$. But the required quantity in (3.5) is distance from the
moving integer lattice, not ordinary real distance.

## 4. Exact two-coordinate centered map

For any centered integer pair



$$
(r,t)\in\mathcal S_b
:=\{(r,t)\in\mathbb Z^2:|r|<b/2\},                    \tag{4.1}
$$



define



$$
m=\operatorname{nint}\!\left(\frac{r-ct}{a}\right).  \tag{4.2}
$$



The backward centered update is



$$
\boxed{
\Phi_n(r,t)
=\bigl(ct-r+am,\;4c-At+m\bigr).}                     \tag{4.3}
$$



For the actual pair, this is exactly



$$
\Phi_n(r_n,t_n)=(r_{n-1},t_{n-1}).                   \tag{4.4}
$$



Indeed, (3.3) and (3.2) give



$$
\begin{aligned}
w_{n-1}
&=4c-\frac ba\left(t-\frac rb\right)\\
&=4c-At+\frac{r-ct}{a}.
\end{aligned}                                         \tag{4.5}
$$



Taking the nearest integer proves the second coordinate of (4.3),
and subtracting (4.5) from that integer and multiplying by $a$
proves the first.

The inverse is explicit. For



$$
(R,S)\in\mathcal S_a,
$$



put



$$
t=\operatorname{nint}\!\left(
\frac{4ac-aS+R}{b}\right),                            \tag{4.6}
$$



and



$$
r=bt-4ac+aS-R.                                        \tag{4.7}
$$



Then $|r|<b/2$, and direct substitution gives



$$
\boxed{
\Phi_n^{-1}(R,S)
=\left(
bt-4ac+aS-R,\ t
\right).}                                             \tag{4.8}
$$



Therefore



$$
\boxed{
\Phi_n:\mathcal S_b\longrightarrow\mathcal S_a
\quad\text{is a bijection}.}                         \tag{4.9}
$$



The pair map does not lose the branch digit. Its exact lattice
equivariance also shows the ambient expansion:



$$
\boxed{
\Phi_n(r,t+a)=\Phi_n(r,t)+(0,-b).}                    \tag{4.10}
$$



Here nearest-integer translation by the integer $-c$ changes
$m$ to $m-c$.

## 5. The actual forward carry is unbounded

The inverse formula gives a useful actual-family update. Write



$$
t_-=t_{n-1},\qquad r_-=r_{n-1}.                       \tag{5.1}
$$



Then



$$
\boxed{
T_n=a(4c-t_-)+r_-,\qquad
t_n=\operatorname{nint}\!\left(
\frac{a(4c-t_-)+r_-}{b}
\right).}                                             \tag{5.2}
$$



Define the integral forward carry



$$
u_n=At_n-4c+t_-.                                      \tag{5.3}
$$



Equation (4.7) becomes



$$
\boxed{
r_n=au_n+ct_n-r_-.}                                   \tag{5.4}
$$



This is a closed exact update once the moving ratio state is retained.
The carry is not bounded. To prove this without extrapolation, set



$$
x_n=\frac{T_n}{b},\qquad
\epsilon_n=t_n-x_n=\frac{r_n}{b},
\qquad |\epsilon_n|<\frac12.                          \tag{5.5}
$$



Dividing (1.4) by $a$ gives



$$
Ax_n-4c+x_{n-1}=-\frac ca x_n.                        \tag{5.6}
$$



Therefore



$$
\boxed{
u_n=-\frac ca x_n+A\epsilon_n+\epsilon_{n-1}.}        \tag{5.7}
$$



The actual interval in (8.2) and
$a=(A-4)c+d$, $0<d<c$, imply



$$
x_n>\frac{4c-d}{A}>\frac{3c}{A},
\qquad
\frac ca>\frac1{A-3}.                                \tag{5.8}
$$



Using (5.5) in (5.7),



$$
\boxed{
u_n<\frac{A+1}{2}-\frac{3c}{A(A-3)}.}                 \tag{5.9}
$$



For $n=7$, $A=26$, $c=q_5=18089$, so



$$
6c>A(A-3)(A+1).                                       \tag{5.10}
$$



This inequality persists. At the next row $A'=A+4$ and
$c'=a>(A-4)c$, while, for $A\ge26$,



$$
(A-4)A(A-3)>(A+4)(A+5).                              \tag{5.11}
$$



The difference is


$$
A^3-8A^2+3A-20,
$$


which is positive at $A=26$; its forward difference
$3A^2-13A-4$ is also positive for every $A\ge26$.
Hence (5.9) is negative for every $n\ge7$. The exact preceding
row uses



$$
T_5=282318,\quad t_5=16,\qquad
T_6=72146038,\quad t_6=181,                            \tag{5.12}
$$



where direct comparison with the two adjacent half-integer multiples
of $q_5=18089$ and $q_6=398959$ proves the nearest integers.
Therefore



$$
u_6=22\cdot181-4\cdot1001+16=-6.                     \tag{5.13}
$$



Finally,



$$
c=q_{n-2}
>7\prod_{j=3}^{n-2}(4j-2)                            \tag{5.14}
$$



for $n\ge5$, by repeated use of (1.1). Thus the negative term in
(5.9) dominates every polynomial in $A$, and



$$
\boxed{
u_n<0\quad(n\ge6),\qquad u_n\longrightarrow-\infty.} \tag{5.15}
$$



This is an actual-family obstruction to treating the forward carry as
a bounded rounding error. It does not rule out a rescaled state which
retains $c/A^2$, the ratio $c/a$, or another growing coordinate.

## 6. A primitive-denominator collapse family

The real contraction (3.4) cannot by itself transmit a lower bound on
distance from integers, even if both rational states are required to
have their full primitive denominators.

Fix $n\ge4$. Since $a$ is odd and $\gcd(a,c)=1$, choose an
integer $k$ satisfying



$$
kc+1\equiv\frac{a-1}{2}\pmod a.                      \tag{6.1}
$$



Define



$$
x=4c-\frac{kb+1}{a},
\qquad
y=k+\frac1b.                                          \tag{6.2}
$$



Then the forward affine update maps $x$ to $y$:



$$
\boxed{
\frac ab(4c-x)=y.}                                    \tag{6.3}
$$



Both denominators are primitive. Since $b\equiv c\pmod a$,



$$
4ac-kb-1
\equiv-kc-1
\equiv-\frac{a-1}{2}\pmod a.                         \tag{6.4}
$$



Also



$$
\gcd\!\left(\frac{a-1}{2},a\right)=1,
\qquad
\gcd(kb+1,b)=1.                                       \tag{6.5}
$$



Thus $x$ has exact denominator $a$, $y$ has exact denominator
$b$, and



$$
\boxed{
\|x\|_{\mathbb Z}=\frac{a-1}{2a},
\qquad
\|y\|_{\mathbb Z}=\frac1b.}                           \tag{6.6}
$$



The first distance is the largest possible nonzero centered distance
on the denominator-$a$ lattice. But the second corresponds to



$$
r=-1,\qquad |r|=1<\frac a2.                           \tag{6.7}
$$



This gives the exact scoped obstruction.

> **PROVED PRIMITIVE CONTRACTION OBSTRUCTION.**
> The affine Turán update, primitive moving denominators, and even a
> nearly maximal previous centered remainder do not imply the next
> half-bound. A one-step denominator-compatible orbit can land at
> $r=-1$.

The construction is not an actual counterexample. Its integer digit
$k$ is selected modulo $a$ and need not lie in the short positive
interval occupied by the actual $t_n$. Therefore this theorem rules
out only recurrence/coprimality/contraction arguments which ignore the
actual seed-specific branch.

## 7. No fixed-norm contraction of the ambient pair map

There is also a direct two-coordinate witness. For $n\ge4$, one has



$$
c\ge7,\qquad a>2c.                                    \tag{7.1}
$$



The two centered points



$$
z_1=(c,1),\qquad z_2=(c,2)                            \tag{7.2}
$$



have $m=0$ in (4.2), because the two arguments are $0$ and
$-c/a$, with $c/a<1/2$. Hence



$$
\Phi_n(z_1)=(0,4c-A),
\qquad
\Phi_n(z_2)=(c,4c-2A),                                \tag{7.3}
$$



and



$$
\boxed{
z_2-z_1=(0,1),\qquad
\Phi_n(z_2)-\Phi_n(z_1)=(c,-A).}                     \tag{7.4}
$$



For every fixed norm $N$ on $\mathbb R^2$,



$$
\frac{N(c,-A)}{N(0,1)}\longrightarrow\infty          \tag{7.5}
$$



because $c=q_{n-2}\to\infty$. Thus the ambient centered pair maps
have no row-uniform finite Lipschitz constant in any fixed unscaled
norm, much less a fixed-norm contraction.

This statement is deliberately narrow. It does not exclude a
row-dependent anisotropic norm, a small invariant region containing
only the actual orbit, or a new arithmetic Lyapunov function.

## 8. What remains actual-family specific

The actual state is not an arbitrary primitive rational orbit. It
satisfies all of



$$
w_n=\frac{bc-a^2}{b},
\qquad
t_n=\operatorname{nint}(w_n),
\qquad
r_n=bt_n-T_n,                                         \tag{8.1}
$$



together with the seed-specific interval from Item 295,



$$
\frac{4c-d}{A}
<w_n<
\frac{5c-d}{A+1}.                                     \tag{8.2}
$$



The primitive collapse family of Section 6 preserves the affine update
and exact denominators, but not necessarily (8.1)-(8.2). Hence the
smallest remaining admissible contraction lemma must use the actual
short branch, not merely the rational affine map.

One exact form of the missing assertion is



$$
\left\|
\frac ab\left(4c-\frac{T_{n-1}}a\right)
\right\|_{\mathbb Z}
\ge\frac{a}{2b}.                                      \tag{8.3}
$$



By (1.4), (8.3) is exactly the original half-bound, not a new theorem.
Item 298 supplies no invariant short-branch region which forces it.

The stronger open target from Item 295,



$$
A(2\rho_n-a)\ge2c,                                    \tag{8.4}
$$



also remains open. No bounded observation is used to support (8.4).

Classical real Turán positivity or log-convexity controls the size of
$T_n$, but not its centered remainder modulo $b$. The missing input
is arithmetic.

## 9. Proper targets and the product baseline

For a proper de-overlapped target



$$
Q\mid b,\qquad Q>1,                                   \tag{9.1}
$$



one has



$$
r_{n,Q}=\operatorname{cent}_Q(r_n),
\qquad
|r_{n,Q}|\le\min\!\left\{|r_n|,\frac{Q-1}{2}\right\}. \tag{9.2}
$$



Therefore a full-$b$ lower bound would not transfer to $Q$. A
full-$b$ upper construction would transfer, as recorded in Items 290,
292, and 295.

The additive centered quotient also remains separate from Item 282's
common coefficient/product baseline. The exact dynamics yields no
retained-capacity ceiling and no positive weighted mass. Booking is
zero.

## 10. Strict labels

### PROVED

* The rank-one rational factorization (3.2)-(3.4).
* The integer-distance formulation of the half-bound (3.5).
* The exact centered pair map and inverse (4.3), (4.8).
* Bijection of the centered strips (4.9).
* The lattice equivariance (4.10).
* The exact forward carry identities (5.2)-(5.7).
* The actual-family theorem $u_n<0$ for $n\ge6$ and
  $u_n\to-\infty$.
* The primitive-denominator collapse family (6.1)-(6.7).
* The ambient fixed-norm expansion witness (7.2)-(7.5).
* Proper-target lower-bound asymmetry and baseline separation.

### PROVED SCOPED METHOD OBSTRUCTION

* Affine recurrence, real contraction, and primitive denominators alone
  do not transmit a centered lower bound.
* The natural actual-family forward carry is not uniformly bounded.
* The ambient pair map is not a row-uniform contraction in any fixed
  unscaled norm.
* These statements do not apply to an invariant region or arithmetic
  Lyapunov function that retains the required growing scale and uses
  the actual short Turán branch.

### EXACT FINITE ONLY

* The checker replays bounded instances of the universal identities,
  inverse map, actual carry formula, explicit primitive collapse
  construction, and ambient expansion witnesses.
* It performs no half-bound scan, counterexample search, or
  exceptional-prime search.

### OPEN

* The all-$n$ half-bound (1.7).
* The stronger target (8.4).
* A closed invariant short-branch region for the actual Turán orbit.
* A row-dependent, correctly rescaled arithmetic Lyapunov function.
* A large proper de-overlapped target residue theorem.
* The Item-282 product baseline and weighted-return cover.
* Route 1 and every conclusion about $e+\pi$.

### BOOKING



$$
\boxed{
\text{new Route-1 rate}=0,\qquad
\text{new beta capacity reduction}=0.}                \tag{10.1}
$$



## 11. Deterministic replay

From the archive root:

~~~text
python scripts/item298_beta_centered_dynamics_certificate.py ^
  --output results/item298_beta_centered_dynamics_certificate_replay.json
~~~

The checker uses only the Python standard library and exact integer or
rational comparisons. The canonical result and replay must be
byte-identical.
