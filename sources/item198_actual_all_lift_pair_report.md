> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 198: exact common-valuation criterion for actual noncentral beta pairs

Date: 2026-08-30 (Beijing time)

## 1. Verdict

Let



$$
q_0=q_1=1,\qquad q_n=(4n-2)q_{n-1}+q_{n-2},
$$



let $p\geq7$ be prime, and put



$$
1\leq r<{p-1\over2},\qquad
 s=p-1-r,\qquad
 h={p-3\over2}-r.
$$



For the odd symmetric continuant



$$
{\cal K}_h(X)=[X-4h,X-4h+4,\ldots,X+4h]
               =D_hX+E_hX^3+\cdots,
$$



the transfer from $(q_r,q_{r-1})$ to $(q_s,q_{s-1})$ has upper-right
entry



$$
B_{p,r}={\cal K}_h(2p).
$$



The first new result is the exact integer identity



$$
\boxed{\gcd(q_r,q_s)=\gcd(q_r,{\cal K}_h(2p)).}             \tag{1.1}
$$



It refines the prime-level singularity criterion into common-valuation
statements.  If $p\mid q_r$, then



$$
\boxed{
 p^2\mid q_r\ \hbox{and}\ p^2\mid q_s
 \iff
 p^2\mid q_r\ \hbox{and}\ p\mid D_h.}                     \tag{1.2}
$$



Thus an actual noncentral reflection pair is all-lift exactly when its
lower actual value is already divisible by $p^2$ and the moving
continuant derivative vanishes modulo $p$.  This is an all-prime exact
classification, not a finite extrapolation.

There is also a third-power refinement:



$$
\boxed{
 p^3\mid q_r\ \hbox{and}\ p^3\mid q_s
 \iff
 p^3\mid q_r\ \hbox{and}\ p^2\mid D_h.}                   \tag{1.3}
$$



Under the hypotheses in (1.2), the exact next paired digit is



$$
\boxed{
 {q_s\over p^2}\equiv {q_r\over p^2}
       +2{D_h\over p}q_{r-1}\pmod p.}                      \tag{1.4}
$$



The Pad\'e companion $P_0=1,P_1=3$ satisfies



$$
P_rq_{r-1}-P_{r-1}q_r=2(-1)^{r-1}.                       \tag{1.5}
$$



Consequently $q_{r-1}$ is a unit at every root prime.  Equations
(1.1)--(1.4) therefore lose no hidden factor through the adjacent value.
They do **not**, however, prove that the simultaneous conditions in (1.2)
never occur for the actual seed.

At one prescribed lower index $N$, let ${\cal A}_N$ be any set of
actual noncentral all-lift primes and put



$$
R_N=\prod_{p\in{\cal A}_N}p.
$$



Then



$$
\boxed{R_N^2\mid q_N.}                                    \tag{1.6}
$$



This is only a capacity ceiling; it gives no positive lower bound for
$R_N$.  It is also sharp for the transfer/continuant/Wronskian data
alone.  A modified recurrence solution can realize simultaneous paired
square divisibility with $u_N=R^2$, while possessing a unit-Wronskian
companion.  A concrete example simultaneously realizes the primes
$7,97,107$.  It is **not** the actual seed $(1,1)$, so it is not an
actual all-lift example.

The actual all-lift existence problem remains open.  Even its resolution
would be only the first local arithmetic stage: actual mixed-coefficient
valuation, divided matching, saddle synchronization, and a sufficiently
small moving-CRT representative remain separate requirements.

## 2. Exact transfer gcd — PROVED

Write



$$
C(t)=\begin{pmatrix}t&1\\1&0\end{pmatrix},
$$



and form the transfer matrix



$$
M_{p,r}=C(4s-2)C(4s-6)\cdots C(4r+2)
        =\begin{pmatrix}A&B\\C&D\end{pmatrix}.              \tag{2.1}
$$



The symmetric-continuant calculation gives



$$
B={\cal K}_h(2p),\qquad A\equiv1\pmod p.                 \tag{2.2}
$$



The first row of (2.1) is



$$
q_s=Aq_r+Bq_{r-1}.                                       \tag{2.3}
$$



Running the recurrence backwards preserves the gcd of adjacent terms, so



$$
\gcd(q_r,q_{r-1})=\gcd(q_1,q_0)=1.                       \tag{2.4}
$$



Taking the gcd of (2.3) with $q_r$, and using (2.4), proves (1.1):



$$
\gcd(q_r,q_s)
 =\gcd(q_r,Bq_{r-1})
 =\gcd(q_r,B).
$$



More generally, for every prime $\ell$,



$$
\boxed{
 \min\{v_\ell(q_r),v_\ell(q_s)\}
 =\min\{v_\ell(q_r),v_\ell({\cal K}_h(2p))\}.}            \tag{2.5}
$$



Identity (1.5) independently shows that, at an odd root prime, both
$q_{r-1}$ and $P_r$ are units.  The continuant entry $B$, rather
than an untracked adjacent factor, carries the whole common valuation.

## 3. Square and cube criteria — PROVED

Oddness of the symmetric continuant gives the integral expansion



$$
{\cal K}_h(2p)
 =2pD_h+8p^3E_h+32p^5F_h+\cdots.                           \tag{3.1}
$$



Because $p$ is odd,



$$
p^2\mid{\cal K}_h(2p)\iff p\mid D_h,                     \tag{3.2}
$$



and



$$
p^3\mid{\cal K}_h(2p)\iff p^2\mid D_h.                  \tag{3.3}
$$



Combine (2.5) with (3.2) and (3.3) to obtain (1.2) and (1.3).
At prime level, (3.2) is the singularity criterion from Item 165.  The
new content here is the exact common-gcd formulation and its prime-square,
prime-cube, and next-digit bookkeeping.

Assume now that $p^2\mid q_r$ and $p\mid D_h$.  Divide (2.3) by
$p^2$.  From (2.2), $A\equiv1\pmod p$, while (3.1) gives



$$
{{\cal K}_h(2p)\over p^2}\equiv2{D_h\over p}\pmod p.
$$



This proves (1.4).  In particular, if $p^3\mid q_r$, then the upper
member also reaches $p^3$ exactly when $p^2\mid D_h$, in agreement
with (1.3).

No equally simple statement at every higher power follows merely by
replacing $D_h$ with a higher divisibility condition: starting at the
fourth power, the $E_h$ term in (3.1) can contribute to the decision.

## 4. Relation to reflection and the shifted left-factorial criterion

For the actual beta seed, prime-square reflection gives



$$
q_{p^2-1-n}\equiv q_n\pmod {p^2}.                         \tag{4.1}
$$



Together with the first affine lift, it pairs the root classes $r,s$
and identifies a singular all-lift fibre with the simultaneous square
condition in (1.2).  The transfer proof above supplies an exact integer
gcd beneath that reflection congruence.

Item 166 expresses $p\mid D_h$, under $p\mid q_r$, as the prescribed
left-factorial residue



$$
!p\equiv b_rP_r^{-1}\pmod p.                              \tag{4.2}
$$



Therefore (1.2) can also be written



$$
p^2\mid q_r,q_s
 \iff
 p^2\mid q_r\quad\hbox{and}\quad
 !p\equiv b_rP_r^{-1}\pmod p.                             \tag{4.3}
$$



Equation (1.1) removes the Euler residue from the local common-valuation
calculation and extends it to the cube threshold.  It does not prove an
avoidance theorem: the remaining integer ${\cal K}_h(2p)$ still moves
with $p$, and its height is on the ineffective $\Theta(p\log p)$
scale.

## 5. Prescribed-index product ledger — PROVED ceiling, OPEN mass

Fix $N$, and restrict to primes $p>2N+1$, so that $N$ is the lower
member of its noncentral reflection pair.  Every actual all-lift prime in
${\cal A}_N$ satisfies $p^2\mid q_N$; multiplication over distinct
primes proves (1.6).  Equivalently,



$$
R_N\mid \prod_{\ell:\,v_\ell(q_N)\ge2}\ell,
 \qquad
 \log R_N\leq{1\over2}\log q_N.                           \tag{5.1}
$$



At the archived balanced beta saddle,



$$
{\log q_N\over6m}\longrightarrow
 \theta=1.1685311871794864979\ldots.                       \tag{5.2}
$$



The residual post-$3m$ doubled-rate gap is



$$
G=0.01963298366943179388\ldots.                            \tag{5.3}
$$



If this branch books only an $R_N^2$ gain, filling that gap would require



$$
\log R_N>3Gm
 =0.05889895100829538164\ldots\,m.                         \tag{5.4}
$$



The ceiling (5.1) is vastly larger than (5.4), but a ceiling gives no
lower bound at all.  Hence this branch is neither constructed nor excluded.
In particular, (1.6) cannot be booked as positive content.

The logical stages are:

1. **Actual root existence:** an actual prime must divide the fixed
   denominator at the prescribed lower index.
2. **Local all-lift:** the two extra conditions in (1.2) must hold.
3. **Mixed-coefficient valuation:** the actual coefficient must be
   divisible by at least the same $p^2$ required for equal-level
   matching.
4. **Divided matching:** the normalized coefficient congruence must hold
   at that same $(m,N,p)$.
5. **Saddle and CRT:** the simultaneous residue system must have a
   representative inside the shrinking saddle window.

No item in this list implies the next.

## 6. Sharp structural countermodel — PROVED, not the actual seed

Fix an index $N\geq1$, and let ${\cal S}$ be any finite set of odd
primes



$$
p=2N+2h_p+3
 \quad\hbox{with}\quad p\mid D_{h_p}.                       \tag{6.1}
$$



Put $R=\prod_{p\in{\cal S}}p$.  Define an integral solution $u_n$ of
the same recurrence by prescribing



$$
u_{N-1}=1,\qquad u_N=R^2,                                 \tag{6.2}
$$



and running the recurrence backwards to its initial pair and forwards at
larger indices.  For $s_p=p-1-N$, the transfer formula gives



$$
u_{s_p}=A_{p,N}R^2+{\cal K}_{h_p}(2p).                    \tag{6.3}
$$



Both terms on the right are divisible by $p^2$, by (6.1), (3.2), and
$p^2\mid R^2$.  Thus



$$
\boxed{p^2\mid u_N,u_{s_p}\quad(p\in{\cal S}).}           \tag{6.4}
$$



Adjacent gcds are invariant under the unimodular recurrence steps, so
$\gcd(u_0,u_1)=\gcd(1,R^2)=1$.  Choose an integral companion solution
$v_n$ with



$$
v_1u_0-v_0u_1=1.
$$



Its discrete Wronskian then satisfies



$$
v_nu_{n-1}-v_{n-1}u_n=(-1)^{n-1}.                         \tag{6.5}
$$



Therefore recurrence transfer, the symmetric continuant, adjacent
coprimality, and a unit Wronskian are jointly compatible with simultaneous
paired square divisibility whose full product $R^2$ already occurs in
the lower value.

A concrete **FINITE EXPLICIT FIXTURE** takes



$$
N=1,\qquad {\cal S}=\{7,97,107\},\qquad
 R=72653,qquad R^2=5278458409.                             \tag{6.6}
$$



The tied continuant rows in this finite fixture are



$$
(p,h)=(7,1),(97,46),(107,51),
$$



and exact recurrence evaluation gives $p\mid D_h$ in all three rows.
For the seed $(u_0,u_1)=(1,R^2)$, the paired indices are



$$
(p,s_p)=(7,5),(97,95),(107,105),
$$



and $p^2\mid u_1,u_{s_p}$ in every row.  Taking
$(v_0,v_1)=(0,1)$ gives the unit Wronskian (6.5).

This finite fixture is deliberately **not** evidence for actual-seed
existence:
$u_1=R^2\ne1=q_1$, and it need not satisfy the global actual-seed
anti-period/reflection normalization.  It proves the scoped no-go that
transfer, continuants, adjacent coprimality, and Wronskians alone cannot
improve the universal $R^2\mid q_N$ ceiling.  An actual exclusion must
use additional arithmetic of the fixed seed.

## 7. Exact replay and finite scope

The deterministic certificate verifies:

1. oddness of ${\cal K}_h$, its derivative $D_h$, and the transfer
   identity $B={\cal K}_h(2p)$ on an exact regression grid;
2. the integer gcd identity (1.1) on that grid;
3. the square, cube, and next-digit criteria on every actual root for the
   **finite diagnostic range** $7\leq p\leq251$;
4. the three explicit tied continuant witnesses in (6.6), their exact
   valuations, all three paired square divisibilities, and the unit
   Wronskian.

The finite actual-root list is a regression test only.  Its absence of an
actual all-lift row is labelled **EXPERIMENTAL FINITE** and is not used in
any all-prime proof.

## 8. Status ledger

### PROVED

- The exact common-gcd and common-valuation identities (1.1), (2.5).
- The actual paired square criterion (1.2), cube criterion (1.3), and
  second divided digit (1.4).
- The prescribed-index ceiling $R_N^2\mid q_N$, with no inferred lower
  mass.
- The simultaneous modified-seed countermodel (6.1)--(6.5), including the
  exact $\{7,97,107\}$ fixture.
- The separation of root, local lift, coefficient, matching, and CRT
  stages.

### EXPERIMENTAL FINITE

- The actual-root identity replay through $p\leq251$, including its
  finite absence of an actual all-lift row.

### OPEN

- Existence of any actual noncentral all-lift beta pair.
- An all-prime exclusion or a product bound for its prescribed-index
  radical below the threshold (5.4).
- Positive logarithmic mass of actual useful primes.
- The actual mixed-coefficient valuation, divided matching, saddle
  synchronization, and small moving-CRT representative.
- Irrationality, rationality, or transcendence of the target constant.

## 9. Artifacts and dependencies

The source, script, canonical result, replay result, and manifest archive as

```text
sources/item198_actual_all_lift_pair_report.md
scripts/item198_actual_all_lift_pair_certificate.py
results/item198_actual_all_lift_pair_certificate.json
results/item198_actual_all_lift_pair_certificate.replay.json
results/item198_actual_all_lift_pair_hashes.sha256
```

From the archive root, replay with

```text
python scripts/item198_actual_all_lift_pair_certificate.py \
  --output results/item198_actual_all_lift_pair_certificate.replay.json
```

The all-prime proofs use the following frozen inputs:

```text
d7b4475d2adfeff9a5f1c70a9c6b318d0c2b140bf90b194aa9acb6fdddcc2650  sources/item165_noncentral_singular_report.md
2a8f1c84b91fa7d18fb02417cf480baae819afa795968375e5a3767fc0f52f76  sources/item166_actual_singular_report.md
f02b4b936c2ca810299f037e158e7406214e89ef77e8ca98dcd67b2a9bd00911  sources/bessel_denominator_all_lift_branching_wieferich_barrier.md
```
