> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 165: noncentral singular beta primes and the moving-discriminant barrier

Date: 2026-08-29 (Beijing time)

## 1. Verdict

For the beta denominator



$$
q_0=q_1=1,\qquad q_n=(4n-2)q_{n-1}+q_{n-2},
$$



the noncentral singular condition has an exact continuant/discriminant
description.  Let $p=2c+1\ge5$ be prime, let



$$
1\le r<c,\qquad s=p-1-r,\qquad h=c-r-1,
$$



and suppose $p\mid q_r$.  Define the odd symmetric continuant



$$
\mathcal K_h(X)=[X-4h,X-4h+4,\ldots,X+4h]
              =X\mathcal L_h(X^2)
$$



and



$$
D_h:=\mathcal K_h'(0)=\mathcal L_h(0).
$$



Then the first index slope is



$$
\boxed{
\delta_p(r):={q_r-q_s\over p}
\equiv-2D_hq_{r-1}\pmod p.}
\tag{1.1}
$$



Since adjacent beta denominators are coprime, $q_{r-1}$ is a unit modulo
$p$.  Therefore



$$
\boxed{
r\text{ is noncentral singular}
\iff p\mid q_r\ \text{and}\ p\mid D_{(p-3)/2-r}.}
\tag{1.2}
$$



Moreover $D_h$ is literally a resultant and a distinguished factor of the
full discriminant:



$$
\boxed{
\operatorname {Res}_X(X,\mathcal L_h(X^2))=D_h,}
\tag{1.3}
$$





$$
\boxed{
\operatorname {Disc}_X(\mathcal K_h)
=(-1)^h4^hD_h^3\operatorname {Disc}_T(\mathcal L_h)^2.}
\tag{1.4}
$$



Thus a noncentral singular root is governed by the vanishing of the
distinguished $D_h^3$ factor, not by the formal derivative of the degree
$(p-1)/2$ polynomial representing only the values of the interpolation
modulo $p$.  The latter derivative can give the wrong answer because terms
which vanish as functions modulo $p$ can still contribute to the
$p$-adic derivative.

This characterization does **not** close the remaining matching gap.  At a
saddle-compatible $N=O(m/\log m)$ and a prime $p>3m$, one eventually has
$p>2N+1$, so $r=N$ and



$$
p\mid q_N,\qquad
p\mid D_{(p-3)/2-N}.
\tag{1.5}
$$



The second integer in (1.5) moves with $p$, and its logarithmic height is
$\Theta(p\log p)$.  A direct resultant-height estimate is therefore much
larger than the useful scale and leaves only the original bound from
$p\mid q_N$.  In particular, the present argument neither rules out the
needed $0.0196329836\ldots$ doubled-rate contribution above $3m$, nor
constructs it.

The new finite certificate checks 40 certified prime divisors $p\mid q_N$
with $N\le80$ and



$$
200000<p\le65{,}676{,}881.
$$



All 40 are ordinary.  The largest tested prime is more than 328 times the
old exhaustive cutoff.  This is targeted exact evidence, not an exhaustive
scan of every prime in that interval and not an all-prime theorem.

## 2. Exact transfer and singularity theorem — PROVED

For a list $t_1,\ldots,t_j$, use the plus continuant



$$
[\,]=1,\qquad [t_1]=t_1,\qquad
[t_1,\ldots,t_j]=t_j[t_1,\ldots,t_{j-1}]
                    +[t_1,\ldots,t_{j-2}].
$$



Put $C(t)=\left(\begin{smallmatrix}t&1\\1&0\end{smallmatrix}\right)$.
The transfer from $(q_r,q_{r-1})^{\mathsf T}$ to
$(q_s,q_{s-1})^{\mathsf T}$ is



$$
M_{p,r}=C(4s-2)C(4s-6)\cdots C(4r+2)
       =\begin{pmatrix}A&B\\ C&D\end{pmatrix}.
$$



Reflection of the coefficient list gives the exact reductions



$$
M_{p,r}\equiv
\begin{pmatrix}1&0\\4r+2&1\end{pmatrix}\pmod p,
\qquad
B=\mathcal K_h(2p).
\tag{2.1}
$$



The list defining $\mathcal K_h$ has odd length and is changed into its
reversal after $X\mapsto-X$ and negation of every entry.  Hence
$\mathcal K_h$ is odd and



$$
{B\over p}={\mathcal K_h(2p)\over p}\equiv2D_h\pmod p.
\tag{2.2}
$$



The first row of the transfer gives



$$
q_s=Aq_r+Bq_{r-1}.
$$



Under $p\mid q_r$, the contribution of $(A-1)q_r/p$ vanishes modulo
$p$, because both $A-1$ and $q_r$ are divisible by $p$.  Equations
(2.1)--(2.2) therefore give (1.1).

Running the recurrence backwards preserves the gcd of two adjacent terms,
so



$$
\gcd(q_r,q_{r-1})=\gcd(q_1,q_0)=1.
$$



This proves (1.2).  If additionally $q_r/p\not\equiv0\pmod p$, the
singular root is dead and has exact valuation one on every first-level lift.

## 3. Resultant, discriminant, and exact formulas — PROVED

Write



$$
\mathcal K_h(X)=X\mathcal L_h(X^2).
$$



Then $\mathcal L_h(0)=\mathcal K_h'(0)=D_h$, immediately proving
(1.3).  To prove (1.4), work first over a splitting field and write



$$
\mathcal L_h(T)=\prod_{j=1}^h(T-\alpha_j).
$$



The roots of $\mathcal K_h$ are $0$ and the pairs
$\pm\sqrt{\alpha_j}$.  At zero its derivative is $D_h$; at either root
above $\alpha_j$, its derivative is
$2\alpha_j\mathcal L_h'(\alpha_j)$.  Multiplying all derivative values,
and using



$$
D_h=(-1)^h\prod_j\alpha_j,
$$



gives (1.4), including its sign.  Since both sides are integral polynomial
identities, the splitting-field calculation proves it over $\mathbb Z$.

Three further exact forms are useful.  First, the terminating Lommel sum is



$$
\boxed{
D_h=\sum_{a=0}^h(-16)^a(a!)^2
             \binom{h+a+1}{2a+1}.}
\tag{3.1}
$$



Second, put



$$
P_{h,j}=[4(j+1),4(j+2),\ldots,4h],
\qquad P_{h,h}=1.
$$



Diagonal cofactors of the symmetric tridiagonal determinant give



$$
\boxed{
D_h=(-1)^h\left(P_{h,0}^2
       +2\sum_{j=1}^h(-1)^jP_{h,j}^2\right).}
\tag{3.2}
$$



This evaluates $D_h\bmod p$ in $h$ exact constant-memory steps through



$$
P_{h,j-1}=4jP_{h,j}+P_{h,j+1}.
\tag{3.3}
$$



Third, if $G(z)=\sum_{h\ge0}D_hz^h$, then



$$
G(z)={1\over(1-z)^2}
\sum_{a\ge0}(a!)^2
\left({-16z\over(1-z)^2}\right)^a.
\tag{3.4}
$$



The identity $A(w)-w(\vartheta+1)^2A(w)=1$ for
$A(w)=\sum(a!)^2w^a$ yields, by substitution in (3.4), the exact
five-lag recurrence



$$
\begin{aligned}
0={}&D_n+(16n^2+1)D_{n-1}-2(8n^2-7)D_{n-2}\\
&-2(8n^2-48n+65)D_{n-3}
 +(16n^2-96n+145)D_{n-4}+D_{n-5}
\end{aligned}
\tag{3.5}
$$



for $n\ge5$, starting with



$$
D_0=1,\quad D_1=-14,\quad D_2=963,\quad
D_3=-141468,\quad D_4=36590277.
$$



The certificate checks (3.1)--(3.2) through $h=18$, (3.5) through
$n=18$, and the discriminant factorization (1.4) through $h=5$, all
with exact integer arithmetic.

## 4. Why the moving resultant gives no mass bound — PROVED, scoped no-go

The positive tails satisfy



$$
P_{h,j}=4(j+1)P_{h,j+1}+P_{h,j+2}.
$$



Because $0<P_{h,j+2}\le P_{h,j+1}$, iteration gives



$$
4^hh!\le P_{h,0}\le\prod_{j=1}^h(4j+1).
\tag{4.1}
$$



The lower recurrence inequality also gives
$P_{h,j}\le P_{h,0}/(4^j j!)$.  Thus (3.2) and
$2\sum_{j\ge1}16^{-j}(j!)^{-2}<2/15$ give the uniform real bounds



$$
{13\over15}P_{h,0}^2
<(-1)^hD_h
<{17\over15}P_{h,0}^2.
\tag{4.2}
$$



Consequently



$$
\boxed{\log|D_h|=2h\log h+O(h).}
\tag{4.3}
$$



For $p>3m$ and $N=O(m/\log m)$, equation (1.5) has
$h=(p-3)/2-N\asymp p$.  Thus the integer detecting the extra singularity
has logarithmic height $\Theta(p\log p)$, much larger than the $m$-scale
ledger.  Worse, a different prime uses a different $D_h$, so the primes
cannot be collected as divisors of one fixed small eliminant.  Bounding a
candidate prime by $|D_h|$ is vacuous in this range.

Let $\mathcal S_{m,N}^{>}$ be the distinct noncentral **dead** singular
primes above (3m) at one index, and put



$$
R_{m,N}^{>}=\prod_{p\in\mathcal S_{m,N}^{>}}p.
$$



Deadness gives $v_p(q_N)=1$, hence



$$
\boxed{R_{m,N}^{>}\mid q_N.}
\tag{4.4}
$$



The elementary recurrence estimate gives



$$
q_N<4^{N-1}N!,\qquad
\log R_{m,N}^{>}\le N\log N+O(N).
\tag{4.5}
$$



At the archived balanced beta saddle,



$$
{\log q_N\over6m}\longrightarrow
\theta=1.1685311871794864979\ldots.
$$



To fill only the residual doubled-rate gap
$0.01963298366943179388\ldots$ above the optimistic $3m$ support
ceiling, it would suffice to have



$$
\log R_{m,N}^{>}
>3(0.01963298366943179388\ldots)m
=0.0588989510082953816\ldots m.
\tag{4.6}
$$



This is only $0.0084007101\ldots$ of the asymptotic $\log q_N$ budget.
Therefore (4.4)--(4.5) are far too weak to exclude closure of the gap.
Equations (4.1)--(4.6) prove a sharply scoped no-go: the direct
continuant-resultant height plus the fact $R\mid q_N$ cannot settle the
mass question.  They do not prove that the required primes exist.

## 5. Exact comparison family — PROVED, but not the Bessel seed

The obstruction is not excluded by the recurrence and transfer structure
alone.  Let $h\ge0$, and let an odd prime $p>2h+3$ divide $D_h$.  Put



$$
N={p-2h-3\over2}.
$$



Modulo $p^2$, prescribe a recurrence solution by



$$
u_{N-1}=1,\qquad u_N=p,
$$



and run the recurrence backwards to obtain its initial pair.  The transfer
matrices are unimodular, so this is always possible and unique modulo
$p^2$.  Equations (1.1)--(1.2), which depend only on the recurrence, give



$$
{u_N-u_{p-1-N}\over p}\equiv0\pmod p,
\qquad {u_N\over p}\equiv1\pmod p.
$$



Thus this modified solution has a noncentral dead singular root.

An explicit example is



$$
h=2,\qquad D_2=963=3^2\cdot107,qquad p=107,\qquad N=50.
$$



With residues modulo $107^2$, backward propagation gives



$$
(u_0,u_1)=(8349,11050),
$$



and exact modular forward replay gives the residues



$$
u_{49}=1,\qquad u_{50}=107,\qquad u_{56}=107.
$$



Hence $\lambda=1$ and $\delta=0$.  This is a rigorous countermodel to
any proposed exclusion using only the recurrence, reflection transfer, and
the discriminant factor.  It is **not** a counterexample for the actual
initial pair $(1,1)$: indeed $q_{50}\not\equiv0\pmod{107}$.  Any actual
exclusion theorem must use the fixed Bessel seed through additional
arithmetic information.

## 6. Extended exact search — EXPERIMENTAL FINITE

The certificate performs three independent finite diagnostics.

1. It directly reconstructs every noncentral beta root for primes
   $p\le2000$ modulo $p^2$.  It checks (1.1) at all 146 roots and finds
   no noncentral singular root.
2. It verifies 40 certified pairs $(p,N)$ with $p\mid q_N$, $N\le80$,
   and $200000<p\le65{,}676{,}881$.  For every pair it evaluates
   $D_{(p-3)/2-N}\bmod p$ by (3.2)--(3.3).  All 40 residues are nonzero,
   so every tested root is ordinary.
3. It replays the modified $(p,h,N)=(107,2,50)$ dead-singular comparison
   modulo $p^2$.

The targeted list is not a complete factorization of every $q_N$ for
$N\le80$, and it does not scan every prime below $65{,}676{,}881$.
Its legitimate conclusion is only the absence of a singular root among the
40 displayed certified large-prime divisors.  In particular, the finite
data do not prove density zero, finiteness, or all-prime absence.

Because none of the tested actual roots is singular, none supplies the
additional synchronized conditions $p\mid b_m$ and the final coefficient
congruence.  This is a null finite result, not a theorem that synchronization
cannot occur.

## 7. Status ledger

### PROVED

- The exact noncentral singularity criterion (1.2).
- The local resultant (1.3) and full discriminant factorization (1.4).
- The Lommel sum, alternating cofactor-square formula, and five-lag
  recurrence (3.1)--(3.5).
- The moving eliminant height $\log|D_h|=2h\log h+O(h)$.
- The radical bound $R_{m,N}^{>}\mid q_N$, and the conclusion that this
  bound is quantitatively incapable of excluding the $0.019633$ gap.
- The modified-initial-data dead-singular comparison family and the exact
  $p=107$ example.

### EXPERIMENTAL FINITE

- No noncentral singular root among 146 direct roots for $p\le2000$.
- No noncentral singular root among the 40 certified large-prime divisors,
  reaching $p=65{,}676{,}881$.
- Together with the prior exhaustive $p\le200000$ scan, all currently
  tested actual examples are consistent with an all-prime noncentral
  exclusion, but do not prove it.

### OPEN

- Whether the fixed beta seed $(q_0,q_1)=(1,1)$ has any noncentral
  singular prime at all.
- An all-prime product bound
  $\log R_{m,N}^{>}=o(m)$, or even a bound below
  $0.0588989510\ldots m$, at saddle-compatible $N$.
- A positive-logarithmic-mass family of actual noncentral dead singular
  primes above $3m$.
- Simultaneous divisibility by the actual $b_m$, the coefficient match,
  and an exceptionally small common root representative at one saddle
  index.
- Any useful contribution from deeper all-lift singular powers.

Nothing here proves irrationality, rationality, or transcendence of
$e+\pi$.

## 8. Replay

After copying the package into the research archive, run from the archive
root:

```text
node scripts/item165_noncentral_singular_certificate.js --output results/item165_noncentral_singular_certificate.json
```

For a byte-identical replay, direct `--output` to a temporary file and
compare it with `results/item165_noncentral_singular_certificate.json`.
The companion SHA-256 manifest pins the report, script, and JSON.
