> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 202: the actual squarefull radical has a canonical Euler filter, but no new product bound

Date: 2026-08-30 (Beijing time)

## 1. Verdict

Let



$$
q_0=q_1=1,\qquad q_n=(4n-2)q_{n-1}+q_{n-2},
$$



and retain the actual companion and jet-correction sequences



$$
P_0=1,\quad P_1=3,\quad
P_n=(4n-2)P_{n-1}+P_{n-2},                         \tag{1.1}
$$





$$
b_0=0,\quad b_1=4,\quad
b_n=(4n-2)b_{n-1}+b_{n-2}+4q_{n-1}.                 \tag{1.2}
$$



Here $b_n$ is the Euler jet-correction sequence, not the mixed
coefficient called $b_m$ in the later matching problem.

The actual normalization gives a genuinely new all-index restriction.
For every $N\geq1$,



$$
\boxed{\gcd(P_N,q_N)=1}.             \tag{1.3}
$$



Consequently there is a unique canonical residue



$$
\boxed{T_N\in\{0,\ldots,q_N-1\},\qquad P_NT_N\equiv b_N\pmod {q_N}.}
                                                                    \tag{1.4}
$$



Let



$$
L_p:=\sum_{j=0}^{p-1}j!\in\mathbb Z
$$



be the integer left factorial.  If



$$
p=2N+2h+3>2N+1
$$



is prime and $p\mid q_N$, then the symmetric-continuant derivative
$D_h$ satisfies the exact fixed-seed congruence



$$
\boxed{
4(-1)^{N-1}D_h\equiv P_N^2(L_p-T_N)\pmod p.}          \tag{1.5}
$$



Since $P_N$ is a unit modulo every divisor of $q_N$, this is also the
gcd/resultant identity



$$
\boxed{
\gcd(p,D_h)=\gcd(p,L_p-T_N),}                          \tag{1.6}
$$



where $D_h=\operatorname {Res}_X(X,\mathcal L_h(X^2))$ for
$\mathcal K_h(X)=X\mathcal L_h(X^2)$.  Thus the actual paired all-lift
condition has the exact prescribed-index classification



$$
\boxed{
p^2\mid q_N\ \hbox{and}\ p\mid D_h
\iff
p^2\mid q_N\ \hbox{and}\ L_p\equiv T_N\pmod p.}     \tag{1.7}
$$



This is stronger information than the bare divisibility
$R_N^2\mid q_N$: every square divisor admitted to the all-lift radical
must also pass one canonical actual-seed Euler residue.  It is not,
however, a smaller numerical upper bound for $R_N$.

Pushing the square condition through the first Witt digit gives one more
exact formula.  When $p^2\mid q_N$ and $L_p\equiv T_N\pmod p$, define



$$
\ell_{p,N}:={L_p-T_N\over p}\pmod p.
$$



Then



$$
\boxed{
{P_NL_p-b_N\over p}\equiv P_N\ell_{p,N}\pmod p.}     \tag{1.8}
$$



The $p^2\mid q_N$ hypothesis kills the otherwise present carry from
the chosen representative $T_N$.  It does **not** determine
$\ell_{p,N}$.

For the canonical $p$-adic Euler sum



$$
\mathcal E_p=\sum_{j\geq0}j!\in\mathbb Z_p,
$$



one has the all-prime second-digit identity



$$
\boxed{\mathcal E_p\equiv(1-p)L_p\pmod {p^2}.}         \tag{1.9}
$$



Hence, under the hypotheses of (1.8),



$$
\boxed{
{P_N\mathcal E_p-b_N\over p}
\equiv P_N(\ell_{p,N}-T_N)\pmod p.}                   \tag{1.10}
$$



No separate Wilson or Fermat quotient appears in this direct first-Witt
push.  The new datum is precisely the prime-dependent lifted
left-factorial digit $\ell_{p,N}$.  No nonvanishing, density, or product
theorem for that digit is proved here.

Finally, the local identities are sharp in a rigorously limited sense.
Once only the first residue $L_p\equiv T_N\pmod p$ is retained, every
formal next digit $L_p=T_N+pz_p\pmod {p^2}$ is compatible with it, and
(1.8) ranges through every residue because $P_N$ is a unit.  CRT allows
arbitrary $z_p$'s at any finite collection of primes.  This is a
**scoped local-data countermodel**, not a model of the actual factorials
and not an actual Bessel all-lift example.  It proves only that the
first-residue bridge and square divisibility, by themselves, cannot
improve the full large-prime squarefull-radical ceiling.

## 2. The canonical actual-seed target -- PROVED

The discrete Wronskian from Items 166 and 198 is



$$
P_Nq_{N-1}-P_{N-1}q_N=2(-1)^{N-1}.                    \tag{2.1}
$$



Both $P_N$ and $q_N$ are odd: their initial values are odd and their
recurrence coefficient is even.  Any common divisor of $P_N,q_N$
therefore is odd, while (2.1) says it divides $2$.  This proves (1.3)
and hence the existence and uniqueness of $T_N$.

Equation (2.1) also gives a useful explicit description:



$$
\boxed{
T_N\equiv {(-1)^{N-1}b_Nq_{N-1}\over2}\pmod {q_N}.}   \tag{2.2}
$$



Division by $2$ in (2.2) means multiplication by the inverse of $2$
modulo the odd integer $q_N$.  Put



$$
C_N={P_NT_N-b_N\over q_N}\in\mathbb Z.                \tag{2.3}
$$



The exact Euler-residual bridge at a tied actual root is



$$
P_NL_p-b_N\equiv2D_hq_{N-1}\pmod p.                   \tag{2.4}
$$



On the other hand, (2.3) and $p\mid q_N$ give



$$
P_NL_p-b_N
=P_N(L_p-T_N)+C_Nq_N
\equiv P_N(L_p-T_N)\pmod p.                            \tag{2.5}
$$



Multiply (2.4) by $P_N$ and use (2.1) modulo $p$.  Comparison with
(2.5) proves (1.5).  Since $P_N$, $q_{N-1}$, $2$, and $4$ are all
units modulo a root prime, (1.6) and (1.7) follow.

This identifies exactly what the normalization $q_0=q_1=1$ adds to
Item 198's transfer countermodel.  An arbitrary recurrence solution still
has a transfer continuant, adjacent coprimality, and a unit-Wronskian
companion, but it does not inherit the distinguished Euler jet
$P_NL_p-b_N$ or the canonical target (1.4).  Thus the normalization is
arithmetically meaningful.  Its current consequence is a filter, not a
product estimate.

## 3. Square divisibility and the first lifted digit -- PROVED

Assume $p^2\mid q_N$ and $L_p\equiv T_N\pmod p$.  Write



$$
L_p-T_N=p\ell
$$



with $\ell\in\mathbb Z$.  The exact identity behind (2.5) is



$$
P_NL_p-b_N=P_Np\ell+C_Nq_N.                             \tag{3.1}
$$



After division by $p$, the second term is still divisible by $p$.
Reduction modulo $p$ proves (1.8).

This is the complete consequence of $p^2\mid q_N$ for the first
left-factorial quotient in the present architecture.  The condition
removes $C_Nq_N/p$, but $\ell_{p,N}$ remains an independent actual
arithmetic value.  In particular, neither of the invalid implications



$$
p^2\mid q_N\Longrightarrow L_p\equiv T_N\pmod p,
$$



or



$$
p^2\mid q_N, L_p\equiv T_N\pmod p
\Longrightarrow \ell_{p,N}=\hbox{a fixed residue}
$$



is used.

The same point appears in the first-Witt invariant.  At a root put



$$
\lambda_N={q_N\over p},\qquad
E_{p,N}=P_NL_p-b_N\pmod p.
$$



Items 192--193 give



$$
I_p(N)=2\lambda_N-E_{p,N}.                              \tag{3.2}
$$



The square condition sets $\lambda_N=0$, so



$$
I_p(N)=-E_{p,N}=-P_N(L_p-T_N)\pmod p.                   \tag{3.3}
$$



Thus the square condition does not eliminate the Euler coordinate; it
isolates it.  All-lift is exactly the additional vanishing in (1.7).

## 4. The next Euler digit and the absence of a Wilson term -- PROVED

Modulo $p^2$, all terms $j!$ with $j\geq2p$ vanish.  For
$0\leq k<p$,



$$
(p+k)!=p!(p+1)\cdots(p+k)\equiv p!k!\pmod {p^2}.       \tag{4.1}
$$



Wilson's congruence is enough at this precision:



$$
p!=p(p-1)!\equiv-p\pmod {p^2}.                         \tag{4.2}
$$



Consequently



$$
\begin{aligned}
\mathcal E_p
&\equiv\sum_{j=0}^{p-1}j!+
       \sum_{k=0}^{p-1}(p+k)!\\
&\equiv L_p-pL_p=(1-p)L_p\pmod {p^2},
\end{aligned}                                           \tag{4.3}
$$



which proves (1.9).  If



$$
W_p={(p-1)!+1\over p}
$$



is the Wilson quotient, then $p!=-p+p^2W_p$; its contribution vanishes
modulo $p^2$.  No Fermat quotient is introduced by (4.1).  This is a
statement about the direct two-digit expansion only, not a claim that no
alternative higher-order identity can ever involve such quotients.

Now divide



$$
P_N\mathcal E_p-b_N
\equiv(P_NL_p-b_N)-pP_NL_p\pmod {p^2}                  \tag{4.4}
$$



by $p$, use (1.8), and reduce $L_p$ to $T_N$ modulo $p$.  This
proves (1.10).  The direct first-Witt push therefore exposes a new lifted
left-factorial digit rather than closing the squarefull obstruction.

## 5. Scoped local-data no-go -- PROVED IN THE STATED MODEL ONLY

Fix $N$ and suppose a finite set $\mathcal S$ of distinct primes has
$p^2\mid q_N$.  Retain only the exact normalized data



$$
(q_N,P_N,b_N,T_N)
$$



and the first Euler condition $L_p\equiv T_N\pmod p$.  For arbitrary
$z_p\in\mathbb F_p$, set formal second-digit representatives



$$
L_p^{\rm form}\equiv T_N+pz_p\pmod {p^2}.              \tag{5.1}
$$



Every choice satisfies the first condition.  Equation (3.1) gives



$$
{P_NL_p^{\rm form}-b_N\over p}\equiv P_Nz_p\pmod p,   \tag{5.2}
$$



and $P_N$ is a unit.  Thus every next digit occurs.  Moreover the CRT
solves (5.1) simultaneously for all $p\in\mathcal S$, even if one
artificially insists that the formal representatives come from one common
integer.

This proves the following precise no-go:

> The data $p^2\mid q_N$, the canonical target $T_N$, the first
> residue equation, and unrestricted local/CRT lifting do not imply any
> proper upper bound on the participating subset of the full squarefull
> radical.

It does **not** say that the actual numbers $L_p=\sum_{j<p}j!$ may be
chosen freely.  It does not preserve the exact integers $D_h$ beyond
their first residue, and it is not an actual recurrence counterexample.
An improvement may still come from a theorem about the true left
factorials, the true moving continuants, or the squarefull part of the
actual $q_N$.  No such theorem is supplied here.

This scope also explains why the Item 198 modified-seed fixture and the
present normalized filter answer different questions.  Item 198 proves
sharpness of transfer/continuant/Wronskian capacity without the fixed
seed.  Item 202 proves that the fixed seed adds (1.5), then shows that the
resulting first-residue information still has no product consequence
unless the actual prime-dependent Euler values are controlled.

## 6. Radical and saddle ledger

Define the full large-prime squarefull radical and its actual all-lift
subradical by



$$
S_N=\prod_{\substack{p>2N+1\\p^2\mid q_N}}p,
\qquad
R_N=\prod_{\substack{p>2N+1\\p^2\mid q_N\\L_p\equiv T_N\pmod p}}p.
                                                               \tag{6.1}
$$



Equation (1.7) proves that the second product is exactly the prescribed
actual paired all-lift radical.  Unconditionally,



$$
\boxed{R_N\mid S_N,\qquad S_N^2\mid q_N,\qquad R_N^2\mid q_N.} \tag{6.2}
$$



No proper all-$N$ upper bound for $S_N$, or for the filtered $R_N$,
is proved.  The generic height bound can be made explicit: positivity and
monotonicity give



$$
q_n<(4n-1)q_{n-1},
$$



so, for $N\geq2$,



$$
\boxed{
\log R_N\leq{1\over2}\log q_N
<{1\over2}\sum_{n=2}^N\log(4n-1)
<{1\over2}\{(N-1)\log4+\log N!\}.}                   \tag{6.3}
$$



This is only the old capacity estimate in explicit all-index form.

At the archived balanced beta saddle,



$$
{\log q_N\over6m}\longrightarrow
1.1685311871794864979\ldots,                            \tag{6.4}
$$



while the residual post-$3m$ doubled-rate gap is



$$
G=0.01963298366943179388\ldots.                         \tag{6.5}
$$



An $R_N^2$ gain would have to satisfy



$$
\boxed{
\log R_N>3Gm
=0.05889895100829538164\ldots\,m.}                    \tag{6.6}
$$



Neither (1.7) nor (6.3) gives a positive lower bound, so no portion of
(6.6) can be booked.  The following stages remain separate:

1. an actual root at the prescribed lower index;
2. the square condition $p^2\mid q_N$;
3. the Euler/continuant condition $L_p\equiv T_N\pmod p$;
4. any required next lifted Euler digit;
5. the actual mixed-coefficient $p^2$-valuation;
6. divided matching at the same $(m,N,p)$;
7. saddle synchronization and a sufficiently small moving-CRT
   representative.

No stage implies the next.

## 7. Exact replay and finite evidence

The deterministic standard-library certificate checks:

1. the Wronskian, same-index coprimality, canonical target, carry, and
   formula (2.2) for every $1\leq N\leq100$;
2. the two-digit Euler identity (1.9) for every prime $p\leq251$;
3. carry cancellation (1.8) at every actual small-prime square divisor
   $p^2\mid q_N$ with $N\leq200,p\leq499$, using three formal lift
   digits per row;
4. every noncentral actual lower root for $p\leq20000$, including the
   canonical Euler filter, with a direct continuant cross-check through
   $p\leq251$.

The actual prescribed scan has 1,133 noncentral lower root rows.  It finds
no lower row with $p^2\mid q_N$, hence no actual all-lift row.  It does
find the known upper-member square row



$$
(p,N,s,h)=(13,4,8,1),\qquad 13^2\mid q_8,\quad 13^2\nmid q_4,
$$



which is ordinary because $D_1\not\equiv0\pmod {13}$.  Every
nonoccurrence statement in this paragraph is **EXPERIMENTAL FINITE**.
It proves neither an all-prime squarefreeness theorem nor an all-lift
exclusion.

The quotient fixtures include the actual normalized value $q_{79}$,
which is divisible by both $7^2$ and $31^2$.  Those primes are far
outside the prescribed lower range $p>2N+1$, and the fixture substitutes
formal residues for actual left factorials.  It is only a transparent
finite replay of the scoped algebra in Section 5.

## 8. Status ledger

### PROVED

- Same-index coprimality (1.3) and the canonical actual-seed target
  (1.4)/(2.2).
- The exact normalization/continuant congruence (1.5), gcd/resultant
  filter (1.6), and all-lift classification (1.7).
- Carry cancellation and the first lifted left-factorial digit (1.8).
- The two-digit $p$-adic Euler identity (1.9) and quotient (1.10), with
  no Wilson-quotient contribution at this precision.
- Exact identification (6.1) of the all-lift radical as a filtered subset
  of the large-prime squarefull radical.
- The local-data/CRT no-go of Section 5, only in its explicitly formal
  scope.
- The capacity and required-mass ledger (6.2)--(6.6).

### EXPERIMENTAL FINITE

- The actual-root and square scan through $p\leq20000$.
- The small-prime square-divisor quotient fixtures through
  $N\leq200,p\leq499$.

### OPEN

- Whether any $p>2N+1$ satisfies $p^2\mid q_N$ at a prescribed lower
  index.
- Whether any actual noncentral paired all-lift prime exists.
- A proper all-$N$ upper bound for $S_N$ or $R_N$, including any
  $o(m)$ or below-threshold bound at the saddle.
- A nonvanishing, density, or cross-prime theorem for
  $L_p\equiv T_N\pmod p$ or $\ell_{p,N}$.
- The actual mixed-coefficient valuation, divided matching, saddle
  synchronization, and small moving-CRT representative.
- Irrationality, rationality, or transcendence of the target constant.

## 9. Portable artifacts and dependencies

The source, checker, canonical result, replay result, and manifest archive
as

```text
sources/item202_actual_squarefull_filter_report.md
scripts/item202_actual_squarefull_filter_certificate.py
results/item202_actual_squarefull_filter_certificate.json
results/item202_actual_squarefull_filter_certificate.replay.json
results/item202_actual_squarefull_filter_hashes.sha256
```

From the archive root, replay with

```text
python scripts/item202_actual_squarefull_filter_certificate.py \
  --prime-limit 20000 \
  --output results/item202_actual_squarefull_filter_certificate.replay.json
```

Canonical and replay JSON must be byte-identical.  The proof uses these
frozen inputs:

```text
2a8f1c84b91fa7d18fb02417cf480baae819afa795968375e5a3767fc0f52f76  sources/item166_actual_singular_report.md
85a0335501e5c81e6d45c2a33139fca2ac24be54324d40fe45d82f891cf51cb9  sources/item193_actual_seed_invariant_report.md
aad8ed39bd63717aae162d0cbcc60ec9d27c023b16c44e554442cd38d49ae749  sources/item198_actual_all_lift_pair_report.md
```
