> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 193: paired actual-seed classification of the Witt invariant

Date: 2026-08-30 (Beijing time)

## 1. Verdict

Item 192 introduced, at an actual beta root, the first-Witt seed invariant



$$
I_x=\delta_x+2\lambda_x,
 \qquad
 \lambda_x={q_x\over p},
 \qquad
 \delta_x={-q_{x+p}-q_x\over p}\pmod p.                     \tag{1.1}
$$



This note gives the strongest unconditional all-prime classification now
available for $I_x$.  It does **not** prove that every actual-root
invariant is nonzero: the ordinary root $(p,x)=(7,2)$ is a genuine
counterexample.

Let $p=2c+1\geq7$, let



$$
1\leq r<c,\qquad s=p-1-r,
$$



and suppose $p\mid q_r$, where



$$
q_0=q_1=1,\qquad q_n=(4n-2)q_{n-1}+q_{n-2}.
$$



The exact reflection transfer also gives $p\mid q_s$.  Put



$$
\lambda_r={q_r\over p},\qquad
 \lambda_s={q_s\over p}\pmod p.
$$



Then the two index slopes have the exact orientations



$$
\boxed{\delta_r=\lambda_r-\lambda_s,\qquad
        \delta_s=\lambda_s-\lambda_r=-\delta_r.}             \tag{1.2}
$$



Consequently



$$
\boxed{I_r=3\lambda_r-\lambda_s,\qquad
        I_s=3\lambda_s-\lambda_r.}                           \tag{1.3}
$$



The determinant of this pair of linear forms is $8$, a unit for
$p\geq7$.  Therefore



$$
\boxed{I_r=I_s=0
 \iff \lambda_r=\lambda_s=0
 \iff \text{the actual reflection pair is already all-lift}.} \tag{1.4}
$$



This proves a paired noncollapse theorem:

- a dead singular pair has
  $\lambda_r=\lambda_s\ne0$, and both invariants equal
  $2\lambda_r\ne0$;
- an ordinary pair can have at most one zero invariant;
- every pair which is not actually all-lift has at least one nonzero
  invariant.

The result is sharp.  At $(p,r,s)=(7,2,4)$,



$$
(\lambda_r,\lambda_s,\delta_r,\delta_s,I_r,I_s)
 =(1,3,5,2,0,1)\pmod7.                                      \tag{1.5}
$$



Thus a universal one-sided theorem $I_r\ne0$ is false.

For the lower member, Item 165's symmetric-continuant derivative gives the
exact obstruction



$$
\boxed{I_r=2\bigl(\lambda_r-D_hq_{r-1}\bigr),\qquad
 h={p-3\over2}-r.}                                          \tag{1.6}
$$



Equivalently,



$$
I_r=0
 \iff \lambda_s=3\lambda_r
 \iff q_s\equiv3q_r\pmod {p^2}
 \iff \lambda_r\equiv D_hq_{r-1}\pmod p.                    \tag{1.7}
$$



Item 166 converts the same condition into a shifted prescribed residue for
the left factorial:



$$
\boxed{
 I_r=0
 \iff
 !p\equiv\bigl(b_r+2\lambda_r\bigr)P_r^{-1}\pmod p.}         \tag{1.8}
$$



Here $P_0=1,P_1=3$ is the companion beta solution and $b_r$ is the
canonical jet-correction sequence from Item 166.  Equation (1.8) is an
exact reduction only.  It is **not** an avoidance theorem or a density
bound for the primes in question.

At a balanced application one needs the lower member $r=N$, while its
mate $s=p-1-N$ is generally far outside the saddle window.  The fact that
one of $I_r,I_s$ is nonzero therefore cannot be booked as content at the
required index.  The one-sided obstruction (1.7), its logarithmic mass,
mixed-coefficient divisibility, same-index matching, and the small moving
CRT representative all remain separate open problems.

## 2. Reflection signs and orientations — PROVED

The orientation in (1.2) is important, so it is derived explicitly.

For $x=r,s$, the frozen signed affine law is



$$
{(-1)^tq_{x+tp}\over p}
 \equiv\lambda_x+t\delta_x\pmod p.                           \tag{2.1}
$$



Take $0\leq t<p$ and put



$$
t'=p-1-t\equiv-1-t\pmod p.
$$



Exact beta reflection modulo $p^2$, with



$$
p^2-1-(r+tp)=s+t'p,
$$



gives



$$
q_{s+t'p}\equiv q_{r+tp}\pmod {p^2}.                        \tag{2.2}
$$



Both sides of (2.2) are divisible by $p$.  Also $t'$ and $t$ have
the same parity because $p-1$ is even.  Divide (2.2) by $p$, use
(2.1), and reduce $t'$ modulo $p$:



$$
\lambda_r+t\delta_r
 =\lambda_s+(-1-t)\delta_s\pmod p.                           \tag{2.3}
$$



Comparison of the coefficient of $t$ and the constant term gives



$$
\delta_r=-\delta_s,\qquad
 \lambda_r=\lambda_s-\delta_s.
$$



These are exactly (1.2).  In particular,



$$
\delta_r={q_r-q_s\over p},\qquad
 \delta_s={q_s-q_r\over p}\pmod p,                           \tag{2.4}
$$



which fixes both signs in the notation of Item 165.  This proof uses the
exact prime-square reflection and the signed affine law, not the derivative
of a polynomial which merely represents the values modulo $p$.

Now substitute (1.2) into $I_x=\delta_x+2\lambda_x$ to obtain (1.3).
If both invariants vanish, then



$$
\begin{pmatrix}3&-1\\-1&3\end{pmatrix}
 \binom{\lambda_r}{\lambda_s}=0.
$$



The determinant is $8$, so for $p\geq7$ both divided values vanish.
Conversely, if both divided values vanish, (1.2) gives both slopes and
both invariants equal to zero.  This proves (1.4).

For completeness, a central root $r=s=c$ has reflection slope
$\delta_c=0$, hence $I_c=2\lambda_c$.  It has a zero invariant exactly
when it is already all-lift.  The paired theorem is needed only for
noncentral roots.

## 3. The continuant obstruction — PROVED

With



$$
h=c-r-1={p-3\over2}-r,
$$



Item 165 defines the odd symmetric continuant



$$
{\cal K}_h(X)
 =[X-4h,X-4h+4,\ldots,X+4h]
 =X{\cal L}_h(X^2)
$$



and



$$
D_h={\cal K}'_h(0).
$$



Its exact transfer calculation gives, in the orientation fixed above,



$$
\delta_r=-2D_hq_{r-1}\pmod p.                              \tag{3.1}
$$



Substitution into $I_r=2\lambda_r+\delta_r$ proves (1.6).
Because $2$ and $q_{r-1}$ are units at a root prime, this is a genuine
one-congruence obstruction.  It is not a structural nonvanishing theorem:
$D_h$ moves with $p$, has logarithmic height
$\Theta(p\log p)$, and the finite row (1.5) satisfies the congruence
exactly with $h=0$ and $D_0=1$.

The equality $I_r=3\lambda_r-\lambda_s$ also proves



$$
I_r=0\iff q_s\equiv3q_r\pmod {p^2}.
$$



This is useful as an exact test but again involves the moving reflected
index $s=p-1-r$.

## 4. The shifted Euler-residual bridge — EXACT REDUCTION, NOT AVOIDANCE

Use Item 166's companion and jet sequences



$$
P_0=1,\quad P_1=3,\quad
 P_n=(4n-2)P_{n-1}+P_{n-2},
$$





$$
b_0=0,\quad b_1=4,\quad
 b_n=(4n-2)b_{n-1}+b_{n-2}+4q_{n-1}.
$$



At an actual root, the Wronskian



$$
P_xq_{x-1}-P_{x-1}q_x=2(-1)^{x-1}                         \tag{4.1}
$$



makes $P_x$ a unit.  The canonical Euler-jet identity gives



$$
E_{p,x}:=P_x(!p)-b_x=-\delta_x\pmod p.                     \tag{4.2}
$$



Therefore



$$
I_x=2\lambda_x-E_{p,x}.                                    \tag{4.3}
$$



Solving $I_x=0$ in (4.3) proves



$$
!p\equiv(b_x+2\lambda_x)P_x^{-1}\pmod p,                   \tag{4.4}
$$



and (1.8) is its lower-member specialization.

The singularity criterion of Item 166 is the unshifted residue



$$
!p\equiv b_xP_x^{-1}\pmod p.
$$



For a dead singular root, $\lambda_x\ne0$, so the unshifted and shifted
residues are distinct; this is the Euler-residual version of Item 192's
seed-rigidity theorem.  They coincide only when $\lambda_x=0$, the
all-lift case.

No uniform distribution or avoidance statement for the moving residue
(4.4) is proved here.  In particular, (4.4) cannot be promoted from an
exact equivalence to an assertion that only finitely many primes satisfy
it.

## 5. Arithmetic scope at the saddle

For primes $p>2N+1$ at one chosen lower index, $r=N$ and every
candidate prime divides the fixed integer $q_N$.  The paired theorem says
that if $I_N=0$, then the remote mate $s=p-1-N$ has nonzero invariant
unless the pair is actually all-lift.  It does not move that nonzero value
back to $N$.

Thus the only unconditional radical bound remains the capacity bound



$$
\prod_{p\in{\cal S}_N}p\mid q_N.                            \tag{5.1}
$$



There is no new positive lower bound.  In the $R_m^2$ ledger, closing the
post-$3m$ gap would still require



$$
\log R_m>0.05889895100829538164\ldots\,m.                   \tag{5.2}
$$



The following implications are all invalid and are not used:

1. existence of a root or an $I$-zero prime does not imply positive
   logarithmic mass;
2. such mass does not imply the required valuation of the actual mixed
   coefficient $b_m$;
3. coefficient divisibility does not imply the divided matching
   congruence at the same saddle index;
4. local congruences do not imply a sufficiently small simultaneous CRT
   representative.

The notation $b_m$ in this application is the mixed coefficient of the
linear form; it is distinct from the jet-correction sequence $b_x$ in
Section 4.

## 6. Exact replay and finite evidence

The deterministic certificate reconstructs the actual beta denominator
modulo $p^2$ for every prime $7\leq p\leq20000$.  On every noncentral
reflection pair it checks:

- the full prime-square reflection and signed affine fibre laws for every
  prime through $251$, including every lift digit;
- both orientations in (1.2), directly from the two index slopes and the
  two divided reflection quotients;
- both invariant formulas (1.3) and the determinant classification (1.4);
- the differentiated-continuant formula (1.6);
- the Wronskian, Euler residual (4.2), and shifted residue (4.4) at both
  members.

The census contains 2,267 actual roots: 1,133 noncentral reflection pairs
and the central root $(79,39)$.  It finds:

- no noncentral singular or all-lift pair;
- exactly one pair with a zero invariant, the ordinary $p=7$ row (1.5);
- no pair with both invariants zero.

These absence statements are **EXPERIMENTAL FINITE**.  The algebraic
identities and paired theorem are all-prime results proved in Sections
2--4.

## 7. Status ledger

### PROVED

- The two slope orientations (1.2).
- The paired invariant formulas (1.3).
- The equivalence (1.4) and noncollapse of every non-all-lift pair.
- The continuant obstruction (1.6)--(1.7).
- The shifted Euler-residual equivalence (1.8)/(4.4).
- The capacity-only saddle scope (5.1) and separation of all downstream
  requirements.

### EXPERIMENTAL FINITE

- The exact census through $p\leq20000$, including the sole one-sided
  zero at $p=7$.

### OPEN

- An all-prime exclusion or a logarithmic-mass upper bound for one-sided
  $I_r=0$ at a prescribed lower/saddle index.
- Existence of any actual noncentral singular or all-lift beta pair.
- Positive logarithmic mass at the useful index.
- The actual mixed-coefficient valuation, divided matching, and small-CRT
  synchronization needed for content.
- Irrationality, rationality, or transcendence of the target constant.

## 8. Artifacts and replay

The source, script, canonical result, and replay result archive as

    sources/item193_actual_seed_invariant_report.md
    scripts/item193_actual_seed_invariant_certificate.py
    results/item193_actual_seed_invariant_certificate.json
    results/item193_actual_seed_invariant_certificate.replay.json

From the archive root, replay with

    python scripts/item193_actual_seed_invariant_certificate.py --output results/item193_actual_seed_invariant_certificate.replay.json

The no-argument output is portable: beside the script in work/, and in
../results/ after archival under scripts/.  The manifest uses
archive-relative keys and pins the Item 164/165/166/169/192 inputs.
