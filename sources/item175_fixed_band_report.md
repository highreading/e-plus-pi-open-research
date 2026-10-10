> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 175 — no structural fixed-band collapse of the first circular gate

Date: 2026-08-29

## 1. Scope and verdict

Retain Item 172's rank-one cell



$$
F_j={u^{3j+2}\over Q^{2j+2}},\qquad
 u=x(1-x),\qquad Q=(1+x)(1+x^2),\qquad j\ge1,
$$



and its five-divisor first-Bockstein formulas.  Write



$$
v_j=\operatorname {coord}(F_jdx)=(R_j,L_j,E_j),
 \qquad
 z_{j,a}=\operatorname {coord}\left({F_j\over x-a}dx\right).
$$



The fixed coordinate weights are



$$
w^A_{j,a}=R_jL_{j,a}-L_jR_{j,a},\qquad
 w^B_{j,a}=E_jL_{j,a}-L_jE_{j,a}.                 \tag{1.1}
$$



The conclusions are deliberately separated by status.

**PROVED — no structural collapse of the first circular functional.**  For
every integer $j\ge1$,



$$
\boxed{w^B_{j,1}\ne0.}                              \tag{1.2}
$$



Consequently, for fixed $j$, the coefficient of $\bar T(1)$ in the
five-divisor formula for $B_0$ is nonzero modulo every prime outside a
finite $j$-dependent set.  Thus the ambient $B_0$ linear functional is
not the zero form in the five divisor values on any fixed band.  There is
no exceptional structural-collapse band.  This does not exclude an
identity after restriction to the actual constrained $\bar T$-value locus.

The use of $a=1$ is essential here.  Regardless of the $a=0$ weight,
the chosen primitive has $\bar T(0)=0$ identically, so that coordinate
cannot certify that the realized five-value form is nontrivial.

**PROVED — exact/reduced scalar convention.**  The Bockstein primitive must
be formed from the exact integer coefficients



$$
\widetilde\gamma_\nu=[x^{p-1}]P_\nu\in\mathbb Z,       \tag{1.3}
$$



not merely from canonical representatives of their reductions.  With
$\widetilde\gamma_\nu$, the resonant coefficient cancels exactly.  With
arbitrary congruent lifts it is generally a nonzero multiple of $p$, and
the primitive must include the resulting $x^p$ term.  Section 2 gives an
exact numerical witness.  This corroborates the repaired convention in
the current Item 172 report.

**EXPERIMENTAL FINITE — the relative $A_0$ form.**  Exact rational and
Gaussian partial fractions find every $w^A_{j,a}$ and $w^B_{j,a}$
nonzero for $1\le j\le12$ and all five divisors.  They also find
$w^A_{j,1}\ne0$ and $w^B_{j,1}\ne0$ through $j\le24$.  Equation
(1.2), but not its $A$-analogue, is proved for all $j$.

**OPEN — actual moving cancellations.**  The values $\bar T(a)$ are not
five free variables.  They are the constrained high-degree evaluations
coming from $P_0,P_1,p,s$.  The nonzero coefficient (1.2) rules out a
geometric identity; it does not prove that the actual sum for $B_0$ is
nonzero, nor that any actual solution set is thin.  No new content exponent
and no conclusion about $e+\pi$ is claimed.

## 2. Exact coefficients versus Cartier reductions

On the $\kappa=1$ cell put



$$
P_0=u^{p-3s-3}Q^{2s+1},\qquad
 P_1=u^{p-3s-3}Q^{2s}.
$$



There are two related but different objects:



$$
\widetilde\gamma_\nu=[x^{p-1}]P_\nu\in\mathbb Z,
 \qquad
 \bar\gamma_\nu=\widetilde\gamma_\nu\pmod p.           \tag{2.1}
$$



Define



$$
\widetilde\Theta=
 \widetilde\gamma_1P_0-\widetilde\gamma_0P_1.           \tag{2.2}
$$



Then



$$
[x^{p-1}]\widetilde\Theta
 =\widetilde\gamma_1\widetilde\gamma_0
  -\widetilde\gamma_0\widetilde\gamma_1=0              \tag{2.3}
$$



over the integers.  Hence the zero-constant primitive



$$
\widetilde T=
 \sum_{q\ne p-1}{[x^q]\widetilde\Theta\over q+1}x^{q+1} \tag{2.4}
$$



is $p$-integral and really satisfies
$\widetilde T'=\widetilde\Theta$.

Now choose arbitrary integer lifts



$$
g_\nu=\widetilde\gamma_\nu+pk_\nu.                    \tag{2.5}
$$



For $\Theta_g=g_1P_0-g_0P_1$, the resonant coefficient is



$$
[x^{p-1}]\Theta_g
 =p(k_1\widetilde\gamma_0-k_0\widetilde\gamma_1).       \tag{2.6}
$$



Thus a $p$-integral primitive made from these lifts must contain



$$
(k_1\widetilde\gamma_0-k_0\widetilde\gamma_1)x^p.      \tag{2.7}
$$



It is incorrect to use reduced representatives in (2.2) while omitting
(2.7).  Reduction should occur only after the exact primitive has been
formed.

The certificate's exact control is



$$
(p,s)=(107,15),qquad
 (\widetilde\gamma_0,\widetilde\gamma_1)
 =(103402679403168,34844059107936),                     \tag{2.8}
$$



whose canonical reductions are $(2,75)$.  If those two small
representatives are used directly, the $x^{106}$ coefficient is



$$
75\widetilde\gamma_0-2\widetilde\gamma_1
 =7685512837021728
 =107\cdot71827222775904.                               \tag{2.9}
$$



The omitted $x^{107}$ coefficient would therefore be
$71827222775904\equiv61\pmod {107}$, visibly nonzero.  With the exact
coefficients in (2.8), (2.3) is exactly zero.

## 3. The fixed-band nonidentity theorem

### 3.1 Residue coordinates

Let $\phi=F_jdx$ and $\psi=F_jdx/(x-1)$.  Both are real proper rational
differentials, with poles only at $-1,i,-i$.  If $\rho$ is the residue
at $-1$ and $\sigma$ the residue at $i$, properness and conjugation
give



$$
\rho+\sigma+\bar\sigma=0,
 \qquad L=2\rho,
 \qquad E=-4\operatorname {Im}\sigma.                  \tag{3.1}
$$



Thus $(L,E)=(0,0)$ is equivalent to the vanishing of every simple
residue, and hence to rational exactness.  More generally, if the two
vectors $(L(\phi),E(\phi))$ and
$(L(\psi),E(\psi))$ are proportional, some
$\psi-\lambda\phi$ has every residue zero and is exact.  The base vector
is nonzero; the same argument below, applied to $\phi$ itself, rules out
its exactness.

Therefore (1.2) follows once rational exactness of



$$
\left({1\over x-1}-\lambda\right)F_jdx                 \tag{3.2}
$$



is ruled out for every $\lambda\in\mathbb Q$.

### 3.2 Cayley transform and degree obstruction

Use



$$
y={x+1\over1-x},\qquad x={y-1\over y+1},\qquad
 D(y)=y(1+y^2).                                         \tag{3.3}
$$



Put



$$
A=3j+2,\qquad K=2j+2.                                  \tag{3.4}
$$



The balancing identity $3K-2A-2=0$ gives, up to a nonzero rational
constant,



$$
F_jdx={ (1-y)^A\over D(y)^K},dy.                       \tag{3.5}
$$



Since



$$
{1\over x-1}=-{y+1\over2},                             \tag{3.6}
$$



(3.2) becomes



$$
{N_\lambda(y)\over D(y)^K},dy,
 \qquad
 N_\lambda=(1-y)^A\left(-{y+1\over2}-\lambda\right).   \tag{3.7}
$$



Suppose it were exact.  A rational primitive, after subtracting its value
at infinity, must have the form



$$
H(y)={R(y)\over D(y)^{K-1}}.                            \tag{3.8}
$$



Equation (3.7) decays at least as $y^{-3j-3}dy$ at infinity, so



$$
\deg R\le3j+1=A-1.              \tag{3.9}
$$



At $y=1$, the numerator in (3.7) vanishes to order at least $A$; when
$\lambda=-1$ it vanishes to order $A+1$.  Hence



$$
H(y)-H(1)\quad\hbox{is divisible by }(y-1)^{A+1}.       \tag{3.10}
$$



Writing $C=H(1)$, equations (3.8)--(3.10) say



$$
R(y)-C D(y)^{K-1}\quad\hbox{is divisible by }(y-1)^{A+1}. \tag{3.11}
$$



Set $t=y-1$.  One has



$$
D(1+t)=2+4t+3t^2+t^3.                                  \tag{3.12}
$$



Every coefficient of $D(1+t)^{K-1}$ is strictly positive.  In
particular,



$$
[t^A]D(1+t)^{K-1}>0.                                   \tag{3.13}
$$



But (3.9) makes $[t^A]R=0$, while divisibility in (3.11) forces the
coefficient through degree $A$ to vanish.  Equations (3.11)--(3.13)
therefore give $C=0$.  Then (3.11) makes $R$ divisible by a polynomial
of degree $A+1$, whereas $\deg R\le A-1$; hence $R=0$.  This would
make (3.7) zero, a contradiction.

Thus (3.2) is never exact.  Its two residue vectors are never proportional,
and (1.2) follows for every $j\ge1$.

## 4. Consequence for the five-divisor formula

With the repaired exact convention and
$\chi_4(p)=(-1)^{(p-1)/2}$, Item 172 gives



$$
B_0=\chi_4(p)\sum_{a\in\{0,1,-1,i,-i\}}
 \tau_p\bigl(n_a\bar T(a)\bigr)w^B_{j,a}\pmod p,        \tag{4.1}
$$



where



$$
n_0=n_1=3j+2,\qquad n_{-1}=n_i=n_{-i}=-(2j+2).         \tag{4.2}
$$



At $a=1$, inverse Frobenius is trivial and (1.2) shows that the
coefficient is



$$
\chi_4(p)(3j+2)w^B_{j,1}.             \tag{4.3}
$$



Apart from the displayed quadratic unit, this is a fixed nonzero rational
number.  For a fixed band, let $\mathcal E_j$ contain primes dividing its
numerator or denominator and primes dividing $3j+2$.  Then (4.3) is nonzero modulo every
$p\notin\mathcal E_j$.  Hence (4.1) is a genuinely nonzero formal linear
constraint for every sufficiently large prime in that band.

This is the sharp fixed-polynomial obstruction supplied by the item.  An
identity $B_0\equiv0$ on the actual mixed-cubic rows would now have to
come from a nontrivial relation among the moving values $\bar T(a)$, not
from degeneration of the fixed coordinate weights.  Nothing here proves
that such a relation cannot occur.

The relative gate



$$
A_0=\sum_a\tau_p(n_a\bar T(a))w^A_{j,a}\pmod p         \tag{4.4}
$$



has the same formal shape.  The certificate finds no fixed-band
degeneration in its exact finite range, but the proof in Section 3 uses
only the residue pair $(L,E)$ and does not establish an all-$j$ theorem
for the relative pair $(R,L)$.

## 5. Deterministic certificate

The standard-library checker

`scripts/item175_fixed_band_certificate.py`

performs the following exact tasks.

1. It computes the complete principal parts at $-1,i,-i$ over
   $\mathbb Q(i)$, reconstructs $(R,L,E)$, and evaluates every weight in
   (1.1) for all five divisors through $j=12$.
2. It extends the exact $a=0,1$ coordinate check through $j=24$.
3. It replays the coefficient recurrence for
   $DR'-(K-1)D'R=N_\lambda$ through $j=200$; every finite obstruction
   resultant is positive.  This is a diagnostic replay of the all-$j$
   degree proof, not its logical basis.
4. It checks the positive coefficient in (3.13) through $j=200$.
5. It verifies every integer in (2.8)--(2.9), including the nonzero
   missing $x^p$ coefficient $61\pmod {107}$.

Two canonical executions are required to be byte-identical before
integration.

## 6. Status ledger

### PROVED

- The exact/reduced Cartier-scalar convention and arbitrary-lift correction.
- The all-band theorem $w^B_{j,1}\ne0$ for every $j\ge1$.
- Formal nonidentity of the $B_0$ five-divisor linear form outside a finite
  set of primes in every fixed band.

### EXPERIMENTAL FINITE

- Nonvanishing of all ten $A/B$ weights for all five divisors through
  $j=12$.
- Nonvanishing of the $a=0,1$ $A/B$ weights through $j=24$.
- Positive recurrence resultants and degree-obstruction coefficients through
  $j=200$.

### OPEN

- An all-$j$ nonidentity theorem for the relative $A_0$ form.
- Nonvanishing or thinness of the actual constrained moving-value sum (4.1).
- Any positive-mass cubic family or improved Route-1 content exponent.
- The rationality, irrationality, or transcendence of $e+\pi$.
