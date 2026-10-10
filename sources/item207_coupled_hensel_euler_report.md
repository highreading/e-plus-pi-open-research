> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 207: the actual Hensel and Euler filters are independent unit coordinates

Date: 2026-08-30 (Beijing time)

## 1. Verdict

Retain the actual sequences



$$
q_0=q_1=1,\qquad q_n=(4n-2)q_{n-1}+q_{n-2},
$$





$$
P_0=1,\quad P_1=3,\quad
P_n=(4n-2)P_{n-1}+P_{n-2},
$$





$$
b_0=0,\quad b_1=4,\quad
b_n=(4n-2)b_{n-1}+b_{n-2}+4q_{n-1}.
$$



For a prescribed large prime, write



$$
p=2N+2h+3>2N+1,\qquad s=p-1-N=N+2h+2,                  \tag{1.1}
$$



and assume $p\mid q_N$.  Let $D_h$ be the symmetric-continuant
derivative from Items 165, 198, and 202, and let



$$
T_N\in\{0,\ldots,q_N-1\},\qquad P_NT_N\equiv b_N\pmod {q_N}. \tag{1.2}
$$



Put, in $\mathbb F_p$,



$$
\lambda={q_N\over p},\qquad
\lambda_s={q_s\over p},\qquad
\rho=L_p-T_N,\qquad
E_N=P_NL_p-b_N,                                         \tag{1.3}
$$



where $L_p=\sum_{j=0}^{p-1}j!$.  Finally, let $\tau$ be the canonical
reverse-Bessel Hensel digit: if $A_N(-1)=q_N$ is Item 204's monic
reverse-Bessel realization, then



$$
A_N(-1+p\tau)\equiv0\pmod {p^2}.                         \tag{1.4}
$$



The two previously separate filters are related by an exact **unit
diagonal change of coordinates**:



$$
\boxed{\tau=(-1)^NP_N\lambda,}                            \tag{1.5}
$$





$$
\boxed{D_h={(-1)^{N-1}P_N^2\over4}\rho.}                 \tag{1.6}
$$



Its determinant is



$$
\boxed{-{P_N^3\over4}\ne0\pmod p.}                       \tag{1.7}
$$



Thus the Hensel and Euler/continuant coordinates do not collapse into one
new condition.  They are exactly two independent first-Witt coordinates.
In particular,



$$
\boxed{p^2\mid q_N\iff\tau=0,\qquad
       p\mid D_h\iff \rho=0\iff L_p\equiv T_N\pmod p.}    \tag{1.8}
$$



The complete coupled equivalence is



$$
\boxed{
\begin{aligned}
p^2\mid q_N\ \hbox{and}\ p^2\mid q_s
&\iff \tau=D_h=0\\
&\iff \tau=\rho=0\\
&\iff p^2\mid q_N\ \hbox{and}\ L_p\equiv T_N\pmod p.
\end{aligned}}                                            \tag{1.9}
$$



This is an exact all-prime classification.  It does not prove that the
conditions occur or fail.

The two-dimensional geometry also identifies every natural first-Witt
line.  With the lower and upper paired invariants $I_N,I_s$,



$$
\boxed{
\begin{array}{c|c}
\text{condition}&\text{line in }(\tau,D_h)\\ \hline
p^2\mid q_N&\tau=0\\
p^2\mid q_s&\tau=4D_h\\
I_N=0&\tau=-2D_h\\
I_s=0&\tau=6D_h.
\end{array}}                                              \tag{1.10}
$$



All four lines are distinct for $p\ge7$, and any two meet only at the
coupled origin.  However, a single line is not the origin.  The actual
normalized seed supplies the exact prescribed-range witness



$$
(p,N,h)=(7,2,0),\qquad (\tau,D_h,\rho,I_N)=(5,1,6,0).      \tag{1.11}
$$



Thus $I_N$ vanishes by the nonzero cancellation
$\tau=-2D_h$, even though neither the square condition nor the Euler
condition holds.  This is an actual-seed counterexample, not a formal CRT
model.  It proves a sharply scoped no-go: replacing the two-coordinate
gate by the single known invariant $I_N=0$ is invalid even in the target
range.

No global exclusion or zero-rate bound follows.  For the coupled radical



$$
R_N=\prod_{\substack{p>2N+1\\p^2\mid q_N\\L_p\equiv T_N\ (p)}}p,
$$



the only new product statement remains



$$
\boxed{R_N^2\mid q_N.}                                    \tag{1.12}
$$



The coordinate repackaging contributes **zero new divisibility exponent**
beyond this square-capacity bound.  The reverse-Bessel discriminant is a
unit at every target prime; $D_h$ and $L_p$ move with $p$; and no new fixed
integer of controlled height collects their second coordinate.  This
rules out only the direct rank-one/discriminant/resultant-height strategy.
It does not rule out new arithmetic controlling the joint actual values.

## 2. The unit coordinate theorem -- PROVED

The actual Wronskian is



$$
P_Nq_{N-1}-P_{N-1}q_N=2(-1)^{N-1}.                        \tag{2.1}
$$



At a root $p\mid q_N$, both $P_N$ and $q_{N-1}$ are units and



$$
P_Nq_{N-1}=2(-1)^{N-1}\pmod p.                            \tag{2.2}
$$



Item 204 gives



$$
\tau=-2\lambda q_{N-1}^{-1}\pmod p.                       \tag{2.3}
$$



Equation (2.2) implies



$$
q_{N-1}^{-1}={(-1)^{N-1}P_N\over2}\pmod p.
$$



Substitution in (2.3) proves (1.5).

By the definition of the canonical target,



$$
E_N=P_N(L_p-T_N)=P_N\rho\pmod p.                           \tag{2.4}
$$



The actual-seed Euler/continuant bridge of Item 202 is



$$
4(-1)^{N-1}D_h=P_N^2(L_p-T_N)\pmod p.                     \tag{2.5}
$$



Since a sign is its own inverse, (2.5) proves (1.6).  Equations
(1.5)--(1.6) are the diagonal map



$$
\binom{\tau}{D_h}=
\begin{pmatrix}
(-1)^NP_N&0\\
0&(-1)^{N-1}P_N^2/4
\end{pmatrix}
\binom{\lambda}{\rho}.                                   \tag{2.6}
$$



Its determinant is (1.7), a unit because $p\nmid2P_N$.  Hence the ideals
generated by the two coordinate pairs agree:



$$
(\tau,D_h)=(\lambda,\rho)\quad\text{inside }\mathbb F_p.  \tag{2.7}
$$



This proves both one-coordinate equivalences in (1.8).  It also proves
that combining the two identities supplies an invertible relabelling,
not a third relation between the coordinates.

## 3. Reflected square and invariant line geometry -- PROVED

The exact reflected slope orientation from Items 193 and 198 is



$$
\lambda-\lambda_s=-2D_hq_{N-1}.                           \tag{3.1}
$$



Equation (2.3) also gives



$$
\lambda=-{\tau q_{N-1}\over2}.
$$



Therefore



$$
\boxed{\lambda_s=q_{N-1}\left(-{\tau\over2}+2D_h\right).} \tag{3.2}
$$



Since $q_{N-1}$ is a unit, $\lambda_s=0$ exactly when
$\tau=4D_h$.  This proves the upper-square line in (1.10).  The lower
square line is (1.8).

For the lower invariant, use



$$
I_N=2\lambda-E_N.                                         \tag{3.3}
$$



Equations (1.5), (1.6), and (2.4) yield two equivalent forms:



$$
\boxed{
I_N=2(-1)^NP_N^{-1}(\tau+2D_h)
   =-q_{N-1}(\tau+2D_h).}                                 \tag{3.4}
$$



Thus $I_N=0$ is the line $\tau=-2D_h$.  The paired formula
$I_s=3\lambda_s-\lambda$ and (3.2) similarly give



$$
\boxed{I_s=q_{N-1}(-\tau+6D_h),}                          \tag{3.5}
$$



so $I_s=0$ is the line $\tau=6D_h$.

For $p\ge7$, the slopes $0,4,-2,6$ are pairwise distinct.  Hence each of
the following is equivalent to $\tau=D_h=0$:

1. both lower and upper square conditions;
2. the lower square condition and $I_N=0$;
3. the singular/Euler condition and $I_N=0$;
4. both paired invariants vanishing.

The first equivalence is Item 198's paired square theorem, and the fourth
is Item 193's paired-invariant theorem.  Equations (2.6) and (3.2)--(3.5)
put all of them in one coordinate diagram and prove (1.9).

## 4. Actual-seed rank-one no-go -- PROVED, SHARPLY SCOPED

At $p=7,N=2,h=0,s=4$, the actual integer data are



$$
q_2=7,\quad q_4=1001,\quad P_2=19,\quad b_2=28,
\quad T_2=0,
$$





$$
L_7=\sum_{j=0}^6j!=874\equiv6\pmod7,
\qquad D_0=1.
$$



Consequently



$$
(\lambda,\lambda_s,\rho,\tau,D_0,E_N,I_N,I_s)
=(1,3,6,5,1,2,0,1)\pmod7.                                \tag{4.1}
$$



In particular,



$$
\tau+2D_0=5+2=0\pmod7,                                   \tag{4.2}
$$



while $\tau,D_0,\rho$ are nonzero.  Also $7>2\cdot2+1$, so this is a
genuine prescribed lower-index row.  It proves that the kernel line of
the single invariant (3.4) contains a nonzero point realized by the
actual seed.

There is a second useful actual line witness.  At $(p,N,h,s)=(13,4,1,8)$,



$$
(\tau,D_h)=(9,12),\qquad \tau=4D_h\pmod {13}.              \tag{4.3}
$$



Thus $13^2\mid q_8$ but $13^2\nmid q_4$.  This is an upper-square row,
not a prescribed lower-square row.  It shows concretely why the finite
census must keep lower and reflected upper square conditions separate.

The rigorous no-go is exactly this:

> The actual-seed first-Witt identities give an invertible two-coordinate
> system.  The known scalar invariant has a one-dimensional kernel, and
> the actual prescribed row $(7,2,0)$ realizes a nonzero point of that
> kernel.  Therefore a proof may not replace the conjunction
> $\tau=D_h=0$ by the single condition $I_N=0$, nor infer square or Euler
> vanishing from that invariant alone.

This is stronger and more relevant than Item 202's formal CRT model in
one respect: the counterexample is the actual normalization
$q_0=q_1=1$.  Its scope is narrower in another respect: it rules out the
rank-one collapse, not every possible global theorem about the joint
coordinates.  No actual coupled row is constructed.

## 5. Why the combined identities add zero rate

Let $\mathcal R_N$ be the coupled prime set in (1.12).  Multiplication of
the lower-square conditions gives



$$
R_N^2\mid q_N.                                            \tag{5.1}
$$



The Euler/continuant condition selects a subset of these primes but does
not raise their valuation in $q_N$.  In particular, it does not imply
$p^3\mid q_N$, so it contributes no third copy to (5.1).

The three available eliminants do not improve this direct ledger:

1. Item 204's reverse-Bessel discriminant has no prime factor
   $p>2N+1$.  This certifies a simple polynomial root and hence the unique
   Hensel coordinate; it supplies no divisor containing $R_N$.
2. The symmetric-continuant integer $D_h$ changes with
   $h=(p-3)/2-N$.  Item 165's exact estimate
   $\log|D_h|=2h\log h+O(h)$ is much larger than the useful scale, and
   distinct primes use distinct moving integers.
3. The equality $D_h=0\pmod p\iff L_p=T_N\pmod p$ replaces that moving
   divisor by a different prime-dependent factorial value.  It does not
   collect the primes into a second fixed integer of controlled height.

Finally, the diagonal determinant (1.7) is a unit.  Passing from
$(\lambda,\rho)$ to $(\tau,D_h)$ therefore changes no valuation and adds
no exponent.  The exact rate contribution of the repackaging itself is
zero.

At the archived balanced beta saddle, an $R_N^2$ gain would still require



$$
\log R_N>0.05889895100829538164\ldots\,m.                  \tag{5.2}
$$



Neither (5.1) nor the filters above give a zero-rate estimate
$\log R_N=o(m)$, a below-threshold bound, or any positive mass statement.
This is a proved accounting obstruction for the displayed direct
divisibility/resultant-height architecture.  It is not a theorem that a
new cross-prime or $p$-adic method cannot succeed.

Item 200's normalized-common-log analysis exhibits an analogous warning:
a local scalar recurrence can leave a projective kernel even when all
local identities are exact.  Item 207 does not import Item 200's
coefficient theorem; it applies the same rank audit to the actual beta
coordinates and finds the explicit kernel witness (4.1).

## 6. Exact replay and finite evidence

The deterministic standard-library checker performs the following.

1. It verifies the actual Wronskian, adjacent and companion units, and
   canonical target through $N=100$.
2. It replays the exact actual-seed witness (4.1), including the integer
   value $L_7=874$ and the nonzero coordinate determinant.
3. For every prime $7\le p\le20000$, it reconstructs $q_n$ modulo $p^2$
   and $P_n,b_n$ modulo $p$, then checks (1.5)--(1.10) at every prescribed
   lower root $1\le N<(p-1)/2$.
4. It independently evaluates the symmetric-continuant derivative at all
   such roots through $p\le251$.

The bounded census has 1,133 prescribed lower-root rows.  It finds:

- no lower square row;
- the one upper square row $(p,N,s)=(13,4,8)$;
- no singular/Euler row;
- the one lower-invariant zero row $(p,N)=(7,2)$;
- no upper-invariant zero, paired-invariant zero, or coupled row.

Every nonoccurrence and uniqueness statement in this census is
**EXPERIMENTAL FINITE**.  In particular, absence of a lower square or
coupled row through $p\le20000$ is not an all-prime, density, or rate
theorem.  An upper square row means $p^2\mid q_s$ and must not be reported
as square divisibility at the prescribed lower index $N$.

## 7. Status ledger

### PROVED

- The unit diagonal coordinate theorem (1.5)--(1.7).
- The one-coordinate and complete coupled equivalences (1.8)--(1.9).
- The lower square, upper square, and paired-invariant line geometry
  (1.10), including the reflected divided-value formulas.
- The actual-seed nonzero cancellation witness (1.11)/(4.1).
- The scoped impossibility of collapsing the two-coordinate gate to the
  single invariant $I_N$.
- The direct rate ledger: the repackaging adds zero exponent and leaves
  only $R_N^2\mid q_N$.

### EXPERIMENTAL FINITE

- The actual prescribed-root census through $p\le20000$.
- The finite absence of lower square, singular, paired-invariant-zero, and
  coupled rows in that range.
- The finite uniqueness of the displayed lower-invariant and upper-square
  rows in that range.

### OPEN

- Whether any prescribed lower root has $p^2\mid q_N$.
- Whether any actual coupled all-lift row exists.
- A global exclusion, finiteness theorem, density theorem, or zero-rate
  bound for the coupled radical.
- Any arithmetic theorem controlling the joint actual coordinates
  $(\tau,L_p-T_N)$ across primes.
- All downstream mixed-coefficient valuation, divided matching, saddle,
  and moving-CRT requirements.
- Irrationality, rationality, or transcendence of the target constant.

## 8. Portable artifacts

The source, checker, canonical result, replay result, and manifest archive
as

```text
sources/item207_coupled_hensel_euler_report.md
scripts/item207_coupled_hensel_euler_certificate.py
results/item207_coupled_hensel_euler_certificate.json
results/item207_coupled_hensel_euler_certificate.replay.json
results/item207_coupled_hensel_euler_hashes.sha256
```

From the archive root, replay with

```text
python scripts/item207_coupled_hensel_euler_certificate.py \
  --prime-limit 20000 \
  --output results/item207_coupled_hensel_euler_certificate.replay.json
```

Canonical and replay JSON are byte-identical.  The pinned inputs are

```text
d7b4475d2adfeff9a5f1c70a9c6b318d0c2b140bf90b194aa9acb6fdddcc2650  sources/item165_noncentral_singular_report.md
85a0335501e5c81e6d45c2a33139fca2ac24be54324d40fe45d82f891cf51cb9  sources/item193_actual_seed_invariant_report.md
aad8ed39bd63717aae162d0cbcc60ec9d27c023b16c44e554442cd38d49ae749  sources/item198_actual_all_lift_pair_report.md
06003e9fd03f74b2406330a81d49493fa2f4390c82f359be39bf328184605c68  sources/item200_common_log_gcd_report.md
abbc68e283f16871798be0c6da8af5df55ba6bf865a5864eefc0f8e19fe88f62  sources/item202_actual_squarefull_filter_report.md
45ad273d407323902745095bd7abbc1fe5d17cf4d8da35737276eb3e6c7fc665  sources/item204_squarefull_discriminant_report.md
```
