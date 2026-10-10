> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 320 — all-prefix complement resonance for the exact beta target

Checked: 2026-08-31 (Beijing time)

## 1. Strict verdict

Retain



$$
q_0=q_1=1,
\qquad
q_n=(4n-2)q_{n-1}+q_{n-2}\quad(n\ge2),
\tag{1.1}
$$



and, for $n\ge5$, put



$$
A=4n-2,\qquad
a=q_{n-1},\quad b=q_n,\quad c=q_{n-2},\quad d=q_{n-3}.
\tag{1.2}
$$



Item 316 proves that a centered half-bound failure is equivalent to an
exact canonical Ostrowski target



$$
\frac{a}{2c}\le R<\frac a2,
\qquad 0<|E|<c,
\qquad U=(-1)^n\operatorname{sgn}(E)a.
\tag{1.3}
$$



Item 320 does not exclude (1.3).  It proves the following genuinely
all-digit theorem about every hypothetical solution of (1.3).

> **PROVED — SUB-HALF-LINEAR COMPLEMENT-RESONANCE THEOREM.**
> Fix a rational $0\le\lambda<1/2$.  There is an explicit,
> effectively computable $N_\lambda$, defined in (6.1), such that for
> every $n\ge N_\lambda$, every canonical digit word satisfying the
> exact boundary (1.3), and every truncation depth
> $0\le r\le\lfloor\lambda n\rfloor$, the truncated prefix has
> 
> 

$$
> E_{m-r}=\sigma\bigl(Q_{m-r-1}-g_{m-r}\bigr),
> \qquad
> 0<g_{m-r}<Q_{m-r-1},
> \tag{1.4}
>
$$


> 
> with $\sigma=\operatorname{sgn}(E)$, and its appended dual target has
> the strict complementary form
> 
> 

$$
> |\mathscr U_{m-r-1}|
> =Q_{m-r-1}-G_{m-r},
> \qquad 0<G_{m-r}<Q_{m-r-1}.
> \tag{1.5}
>
$$


> 
> In fact, both $g_{m-r}$ and
> $Q_{m-r-1}-g_{m-r}$ are larger than every allowed digit.

Thus no literal prefix-truncation/complement descent of depth
$L(n)$ with



$$
\limsup_{n\to\infty}\frac{L(n)}n<\frac12
\tag{1.6}
$$



ever lands on an exact earlier Item-316 target.  It remains strictly
resonant on both sides of that target.

This closes only the declared descent class: truncate the canonical word,
carry its exact signed prefix determinant, and compare the resulting
appended dual coordinate to the earlier target.  It does not cover depth
$\lambda n$ with $\lambda\ge1/2$, a full base-reaching descent, an
arbitrary redigitization of the complement, a nonlinear invariant, or the
exact all-digit equality itself.  In particular, the centered half-bound
remains open.

The continuous center of every complement is a normalized Casoratian.
For depths $r\ge1$, it is exactly the Item-282 Casoratian family, but in
the reverse target orientation.  This identity supplies no de-overlapped
overlap, proper-target bound, or capacity reduction.  Booking is zero.

## 2. Exact target boundary and notation

Set



$$
m=n-2,
\qquad w_1=7,
\qquad w_j=4j+2\quad(j\ge2).
\tag{2.1}
$$



Thus $w_m=A-4$ and $w_{m+1}=A$.  Extend the continuant coordinates
through the appended coefficient:



$$
Q_{-1}=0,\quad Q_0=1,
\qquad
P_{-1}=1,\quad P_0=0,
\tag{2.2}
$$





$$
Q_j=w_jQ_{j-1}+Q_{j-2},
\qquad
P_j=w_jP_{j-1}+P_{j-2}.
\tag{2.3}
$$



Then



$$
Q_j=q_{j+1},\qquad
Q_m=a,\quad Q_{m-1}=c,\quad Q_{m-2}=d,\quad Q_{m+1}=b.
\tag{2.4}
$$



Let $\delta_1,\ldots,\delta_m$ be the canonical digits of $R$:



$$
R=\sum_{i=0}^{m-1}\delta_{i+1}Q_i,
\tag{2.5}
$$





$$
0\le\delta_1\le6,
\qquad
0\le\delta_j\le w_j\quad(2\le j\le m),
\tag{2.6}
$$





$$
\delta_j=w_j\Longrightarrow\delta_{j-1}=0.
\tag{2.7}
$$



The reversed digit word also obeys Item 316's exact half-language.  In
particular,



$$
0\le\delta_m\le\frac{w_m}{2}.
\tag{2.8}
$$



If equality holds in (2.8), the lower word represents at most
$(Q_{m-2}-1)/2$.  No other half-language assertion about a truncated
prefix is assumed.

Extend the digit word by



$$
\delta_{m+1}=0.
\tag{2.9}
$$



For $0\le j\le m+1$, define



$$
R_j=\sum_{i=0}^{j-1}\delta_{i+1}Q_i,
\qquad
Z_j=\sum_{i=0}^{j-1}\delta_{i+1}P_i,
\tag{2.10}
$$



and the prefix determinant



$$
\boxed{E_j=R_jP_j-Z_jQ_j.}
\tag{2.11}
$$



Thus $E_m=E$.  The appended unsigned error is $E_{m+1}$, and
Item 316's sign convention gives



$$
U=(-1)^nE_{m+1}.
\tag{2.12}
$$



Put



$$
\sigma=\operatorname{sgn}(E_m).
\tag{2.13}
$$



The exact target, and not an arbitrary digit state, supplies the two-point
boundary



$$
\boxed{E_{m+1}=\sigma Q_m,\qquad E_m=\sigma\kappa,}
\qquad \kappa=|E_m|.
\tag{2.14}
$$



By Item 316, $\kappa$ is the actual nearest quotient and
$1\le\kappa\le c-1$.  Every use of the high-error boundary below
depends on (2.14).  For an arbitrary canonical digit word, only the
universal recurrence in Section 4 remains valid.

## 3. The canonical top complement and Item 295

Define



$$
t=c-\kappa.
\tag{3.1}
$$



This is literally Item 295's defect $t_n=c-\kappa_n$; it is not a new
one-step descent variable.  If



$$
T_n=bc-a^2,
\tag{3.2}
$$



then



$$
t=\operatorname{nint}(T_n/b).
\tag{3.3}
$$



The complement has an exact canonical description at the previous
Ostrowski scale.  Put $e=q_{n-4}$, so



$$
c=(A-8)d+e.
\tag{3.4}
$$



Item 295 gives



$$
\frac{T_n}{b}>\frac{4c-d}{A}.
\tag{3.5}
$$



For $n\ge5$,



$$
\frac{4c-d}{A}>2d+\frac12,
\tag{3.6}
$$



because the cleared difference is



$$
(2A-33)d+4e-\frac A2>0.
\tag{3.7}
$$



Indeed, $A\ge18$, $d\ge7$, and $e\ge1$, so the left side is at
least $7(2A-33)+4-A/2>0$.

At the other endpoint, Item 295's
$T_n+T_{n-1}=4ac$ gives



$$
4bd-T_n=4(bd-ac)+T_{n-1}.
\tag{3.8}
$$



Now



$$
bd-ac=a(Ad-c)+cd,
\qquad Ad-c=8d-e>7d.
\tag{3.9}
$$



Thus $4bd-T_n>28ad>b/2$, since $56d>A+1$ and
$b<(A+1)a$.  The inequality $56d>A+1$ holds at $n=5$ and
persists immediately under the beta recurrence.  Consequently



$$
\frac{T_n}{b}<4d-\frac12.
\tag{3.10}
$$



Nearestness in (3.3) therefore proves



$$
\boxed{2d<t<4d.}
\tag{3.11}
$$



For $n\ge9$, (3.5) improves to



$$
\frac{T_n}{b}>3d+\frac12,
\tag{3.12}
$$



because the cleared difference is



$$
(A-33)d+4e-\frac A2>0.
\tag{3.13}
$$



Here $A\ge34$, and $d>A/2$ at $n=9$ and thereafter by induction,
so (3.13) is strict.

Hence the canonical expansion of $t<Q_{m-1}=c$, in the previous
basis $Q_0,\ldots,Q_{m-2}$, has leading digit



$$
\boxed{
\left\lfloor\frac td\right\rfloor=
\begin{cases}
2,&5\le n\le8,\\
3,&n\ge9.
\end{cases}}
\tag{3.14}
$$



The four base values are



$$
(t,d)=(16,7),(181,71),(2771,1001),(53034,18089).
\tag{3.15}
$$



Digits $2$ and $3$ lie strictly below the allowed top coefficient
$A-8$, so this canonical redigitization creates no Markov carry.
It does not identify the lower digits with a coordinatewise complement
of $(\delta_m,\ldots,\delta_1)$.  Sections 4-7 analyze the literal
prefix/complement chain; an arbitrary redigitization of $t$ is outside
the scoped no-go.

## 4. The all-prefix determinant recurrence

The prefix determinants satisfy an exact inhomogeneous recurrence.
The convergent determinant is



$$
Q_jP_{j-1}-P_jQ_{j-1}=(-1)^j.
\tag{4.1}
$$



Using (2.10) and the fact that the new digit adds
$\delta_{j+1}(Q_j,P_j)$ gives, for $1\le j\le m$,



$$
\boxed{
E_{j+1}=w_{j+1}E_j+E_{j-1}+(-1)^j\delta_{j+1}.}
\tag{4.2}
$$



The bottom values are literal:



$$
E_0=0,\qquad E_1=\delta_1.
\tag{4.3}
$$



Normalize the target sign by



$$
k_j=\sigma E_j.
\tag{4.4}
$$



Backward recurrence from (2.14) reads



$$
\boxed{
k_{j-1}=k_{j+1}-w_{j+1}k_j
-\sigma(-1)^j\delta_{j+1}.}
\tag{4.5}
$$



The first step is precisely Item 295:



$$
k_m=\kappa,
\qquad
k_{m-1}=a-A\kappa=:h.
\tag{4.6}
$$



Thus



$$
g_m:=Q_{m-1}-k_m=t,
\qquad
g_{m-1}:=Q_{m-2}-k_{m-1}=4c-At.
\tag{4.7}
$$



Equations (4.2)-(4.7) explicitly reconcile the new all-prefix chain
with Item 295.  The new content is the arbitrary-depth forced recurrence
and its uniform interior theorem, not the already-known one-step defect.

For $1\le j\le m$, let $\mathscr U_{j-1}$ be the appended dual sum
formed from the lower digits $\delta_1,\ldots,\delta_{j-1}$ and the
truncated word $w_1,\ldots,w_j$.  Directly separating the top digit in
$E_j$ gives



$$
\boxed{
\mathscr U_{j-1}=(-1)^{j+1}E_j-\delta_j.}
\tag{4.8}
$$



This formula includes every sign and carry term.  Dropping the
$-\delta_j$ term would incorrectly turn a near-target into an exact
earlier target.

Every lower prefix of a canonical word still satisfies (2.6)-(2.7), so
it is canonical for its truncated basis and represents a number below
$Q_{j-1}$.  No normalization carry is performed in (4.8).  The prefix
need not satisfy the earlier half-language, and no such claim is used.

## 5. The Casoratian center

The homogeneous real solution matching the top boundary is



$$
x_j=\frac{aQ_j}{b}\qquad(0\le j\le m+1).
\tag{5.1}
$$



It obeys the same coefficient recurrence as $Q_j$.  Define



$$
z_j=k_j-x_j,
\qquad
g_j=Q_{j-1}-k_j,
\qquad
\gamma_j=Q_{j-1}-x_j.
\tag{5.2}
$$



Then



$$
g_j=\gamma_j-z_j.
\tag{5.3}
$$



The exact target gives



$$
z_{m+1}=0,
\qquad
z_m=\kappa-\frac{a^2}{b}=-\epsilon\frac Rb,
\tag{5.4}
$$



where



$$
\epsilon=(-1)^n\sigma
\tag{5.5}
$$



is the sign of the actual centered remainder.  Hence



$$
|z_m|<\frac{a}{2b}<1.
\tag{5.6}
$$



Subtracting the homogeneous recurrence from (4.5) gives



$$
\boxed{
z_{j-1}=z_{j+1}-w_{j+1}z_j
-\sigma(-1)^j\delta_{j+1}.}
\tag{5.7}
$$



For $j=m-r$, put $N=n-r-1$.  Since $Q_j=q_N$ and
$Q_{j-1}=q_{N-1}$,



$$
\boxed{
\gamma_{m-r}
=\frac{q_nq_{n-r-2}-q_{n-1}q_{n-r-1}}{q_n}
=\frac{\mathcal C_{r+1}(n-r-2)}{b}.}
\tag{5.8}
$$



This is the exact Casoratian resonance.

Let



$$
\alpha_s=\frac{q_s}{q_{s-1}}.
\tag{5.9}
$$



Then



$$
4s-2<\alpha_s<4s-1,
\tag{5.10}
$$



and



$$
\frac{\gamma_{m-r}}{Q_{m-r-1}}
=1-\frac{\alpha_{n-r-1}}{\alpha_n}.
\tag{5.11}
$$



Therefore, whenever $n-r-1\ge2$,



$$
\boxed{
\frac{4r+3}{4n-2}\,Q_{m-r-1}
<\gamma_{m-r}
<\frac{4r+5}{4n-1}\,Q_{m-r-1}.}
\tag{5.12}
$$



These bounds are exact rational inequalities.  No finite fit enters
(5.8) or (5.12).

## 6. Uniform deviation and the explicit threshold

Fix a rational $0\le\lambda<1/2$.  For each $n$, define



$$
L_\lambda(n)=\lfloor\lambda n\rfloor,
\qquad
s_\lambda(n)=n-L_\lambda(n)-2.
\tag{6.1a}
$$



Put



$$
\eta=1-2\lambda,
\qquad
\boxed{
N_\lambda=
\left\lceil
\max\left\{8,
\exp\!\left(\frac{4\log4+4}{\eta}\right)
\right\}
\right\rceil.}
\tag{6.1}
$$



This is an explicit effective threshold.  For every integer
$n\ge N_\lambda$,



$$
s_\lambda(n)\ge2,
\qquad
2^{s_\lambda(n)-1}s_\lambda(n)!
>(4n)^{L_\lambda(n)+2}.
\tag{6.2}
$$



Indeed, $n\ge8$ gives $s\ge n/4$, and the elementary integral bound
$\log(s!)\ge s\log s-s$ gives



$$
\begin{aligned}
\log\!\left(2^{s-1}s!\right)
-(L+2)\log(4n)
&\ge(\eta n-4)\log n\\
&\quad -(2\log4+1)n-2\log4>0.
\end{aligned}
\tag{6.3}
$$



The final strict inequality follows from (6.1); after inserting its
lower bound for $\log n$, the right side is at least
$(2\log4+3)n-4\log n-2\log4>0$ for $n\ge8$.
Also, from $q_s>(4s-2)q_{s-1}$,



$$
q_s>\prod_{v=2}^{s}(4v-2)>2^{s-1}s!.
\tag{6.4}
$$



The deviation bound is uniform.  Since $w_j\le A<4n$, every digit in
the reached range is at most $A$, and (5.4), (5.7) give by induction



$$
\boxed{
|z_{m-r}|<(4n)^{r+1}
\qquad(0\le r\le m-1).}
\tag{6.5}
$$



Indeed, the two previous bounds and the digit term sum to strictly less
than the next power of $4n=A+2$.  The case $r=0$ is (5.6), and the
first backward step has $\delta_{m+1}=0$.

Now take $n\ge N_\lambda$ and $0\le r\le L_\lambda(n)$.  Monotonicity
of $q_j$, (5.12), and (6.2)-(6.4) give



$$
\gamma_{m-r}
>\frac3{4n}Q_{m-r-1}
>3(4n)^{L_\lambda(n)+1}.
\tag{6.6}
$$



Combining (5.3), (6.5), and (6.6),



$$
\boxed{g_{m-r}>2(4n)^{L_\lambda(n)+1}>A.}
\tag{6.7}
$$



At the other endpoint,



$$
\frac{x_{m-r}}{Q_{m-r-1}}
=\frac{\alpha_{n-r-1}}{\alpha_n}
>\frac14
\tag{6.8}
$$



for $n\ge8$ and $r<n/2$.  Equations (6.2), (6.4), and (6.5)
give



$$
x_{m-r}>\frac14(4n)^{L_\lambda(n)+2}
=n(4n)^{L_\lambda(n)+1}
>|z_{m-r}|+A,
\tag{6.8a}
$$



and therefore



$$
\boxed{k_{m-r}=x_{m-r}+z_{m-r}>A.}
\tag{6.9}
$$



Since $Q_{m-r-1}=k_{m-r}+g_{m-r}$, (6.7) and (6.9) prove



$$
\boxed{
A<k_{m-r}<Q_{m-r-1}-A,
\qquad
A<g_{m-r}<Q_{m-r-1}-A.}
\tag{6.10}
$$



This proves the advertised uniform interior estimate with all constants
and quantifiers explicit.

## 7. Exact complement defect at every truncation

Let $j=m-r$.  From (4.8), (4.4), and (6.10), put



$$
\tau_j=(-1)^{j+1}\sigma=(-1)^{r+1}\epsilon.
\tag{7.1}
$$



Then



$$
\mathscr U_{j-1}=\tau_jk_j-\delta_j.
\tag{7.2}
$$



Because $k_j>A\ge\delta_j$ and
$g_j>A\ge\delta_j$, the sign in (7.2) cannot cross zero or the target
endpoint.  Define



$$
\boxed{
G_j=g_j+\tau_j\delta_j
=g_j+(-1)^{r+1}\epsilon\delta_j.}
\tag{7.3}
$$



A direct two-sign check gives



$$
\boxed{
|\mathscr U_{j-1}|=Q_{j-1}-G_j,
\qquad 0<G_j<Q_{j-1}.}
\tag{7.4}
$$



For $\tau_j=1$, the defect is $g_j+\delta_j$; for
$\tau_j=-1$, it is $g_j-\delta_j$.  These are the only two cases.

At the first truncation, (7.3) reads



$$
\boxed{G_m=t-\epsilon\delta_m.}
\tag{7.5}
$$



Thus the familiar Item-295 defect $t$ is corrected by the exact top
Ostrowski digit and remainder sign.  At every later truncation, (7.3)
is the corresponding exact Markov-carry-aware complement.

An exact earlier Item-316 target would require
$|\mathscr U_{j-1}|=Q_{j-1}$.  Equation (7.4) excludes this throughout
the stated range.  The theorem does not assert that the lower prefix is
in the earlier half-language; even if it is, its appended equality is
strictly missed.

This proves the scoped no-go:



$$
\boxed{
\limsup L(n)/n<1/2
\Longrightarrow
\text{literal prefix/complement descent never closes by target inheritance.}}
\tag{7.6}
$$



It is a no-go only for a descent whose terminal contradiction requires
an exact inherited Item-316 target.  The positive gaps themselves retain
arithmetic information and could, in principle, enter a new nonlinear or
full-depth invariant.

## 8. Endpoints, signs, carries, and scope audit

* **Actual target versus arbitrary digits.**  Recurrences (4.2), (4.8),
  and (5.7) are universal.  The top boundary (2.14), initial deviation
  (5.4), and every conclusion in (6.7)-(7.6) require the exact Item-316
  target.  No arbitrary digit state is promoted to an actual state.
* **Signs.**  The actual remainder sign is
  $\epsilon=(-1)^n\sigma$.  Equation (7.1) audits its alternation at
  every depth.  Both signs are handled separately in deriving (7.4).
* **Markov carries.**  Prefix truncation preserves all digit bounds and
  implications in (2.6)-(2.7).  Equation (4.8) retains the boundary digit
  $-\delta_j$; it is not silently discarded or normalized.  The
  independent canonical expansion of $t$ has interior leading digit
  $2$ or $3$, so it creates no top carry.
* **Endpoints.**  All target and half-language inequalities are strict at
  $R=a/2$.  Since $a,b$ are odd, no nearest-integer tie exists.
  The strict inequalities in (6.10) exclude both $0$ and the exact
  earlier target endpoint.
* **Indices.**  For $n\ge N_\lambda\ge8$ and
  $r\le\lambda n<n/2$, all reached indices satisfy
  $n-r-1\ge2$.  No negative-index continuant or empty-prefix shortcut
  occurs in the theorem.
* **Small rows.**  The half-bound is exact for $n=2,3,4$.  At $n=5$,
  $(a,b,\kappa,R)=(1001,18089,55,7106)$, so there is no failure.
  Rows $5$ through $8$ in (3.15) are exact endpoint handling for the
  canonical top-complement theorem, not a half-bound extrapolation.

## 9. Item 282, proper targets, and capacity

For $r\ge1$, equation (5.8) uses the same scalar Casoratian family as
Item 282:



$$
\mathcal C_{r+1}(n-r-2)
=q_{n-r-2}q_n-q_{n-r-1}q_{n-1}.
\tag{9.1}
$$



The orientation matters.  Item 320 divides (9.1) by the latest full
denominator $b=q_n$ to locate a real complement center.  Item 282's
overlap theorem instead starts with a declared de-overlapped target
dividing the earliest denominator and compares its primitive return.
No division by $b$ is available in that modular problem, and the digit
phase $z_j$ remains present.

Accordingly, (5.8) proves no statement about



$$
\gcd(Q,P_{r+1}(n-r-2))
\tag{9.2}
$$



for any proper de-overlapped target $Q$, and it supplies no weighted
short-return mass.  Item 282's product baseline and proper-target
distinction are unchanged.

Even a future proof of the full-$b$ half-bound would not automatically
descend as a lower bound to a proper divisor $Q\mid b$.  Item 320 proves
neither result.

### PROVED

* The exact all-prefix determinant recurrence (4.2) and target boundary
  (2.14).
* The identity of $c-|E|$ with Item 295's $t_n$.
* The canonical complement theorem (3.11)-(3.15).
* The normalized Casoratian center and sharp bounds (5.8)-(5.12).
* The uniform deviation estimate (6.5) with the explicit threshold
  (6.1).
* The all-prefix high-error and strict complement classification
  (6.10), (7.3)-(7.4).

### PROVED SCOPED NO-GO

* Literal canonical prefix-truncation/complement descent through every
  depth with $\limsup L(n)/n<1/2$ cannot close by inheriting an exact
  earlier Item-316 target.
* This does not cover $\lambda\ge1/2$, full-depth descent, arbitrary
  complement redigitization, nonlinear arithmetic invariants, or direct
  exclusion of the original target.

### EXACT FINITE ONLY

* The deterministic replay's declared recurrence, sign, Casoratian,
  canonical-complement, and small-index control rows.
* They verify exact identities and endpoints; they are not promoted into
  a half-bound theorem or an actual counterexample search.

### OPEN

* The exact all-digit exclusion (1.3) and the centered half-bound.
* Complement/redigitization methods outside the literal prefix chain.
* Depth $\lambda n$ for $\lambda\ge1/2$ and full base-reaching
  arithmetic.
* Growing/full 2-adic, odd-modulus, or nonlinear square invariants.
* Every proper-target consequence and beta capacity reduction.
* Item 282's actual-family weighted return cover, Route 1, and every
  conclusion about $e+\pi$.

### BOOKING



$$
\boxed{
\text{new beta capacity reduction}=0,
\qquad
\text{new Route-1 rate}=0.}
\tag{9.3}
$$



No canonical, master, status, or research-log file is edited by this work
package.

## 10. Deterministic replay

From the archive root:

~~~text
python work/item320_beta_complement_resonance_certificate.py ^
  --output work/item320_beta_complement_resonance_certificate.replay.json
~~~

The checker uses only the Python standard library and exact integer or
rational arithmetic.  It performs no half-bound scan and promotes no
bounded row.
