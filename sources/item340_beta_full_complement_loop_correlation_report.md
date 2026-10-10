> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 340 — the full canonical complement loop and the remaining beta correlation

Checked: 2026-09-01 (Beijing time)

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
A=4n-2,
\qquad
a=q_{n-1},\quad b=q_n,\quad c=q_{n-2},\quad d=q_{n-3},
\qquad m=n-2.
\tag{1.2}
$$



Let



$$
\kappa=\operatorname{nint}(a^2/b),
\qquad
r=a^2-\kappa b=\epsilon R,
\qquad
\epsilon\in\{\pm1\},\quad R=|r|,
\tag{1.3}
$$



and define the seed complement and Turan determinant



$$
t=c-\kappa,
\qquad
T=bc-a^2.
\tag{1.4}
$$



Item 316 says that an actual half-bound failure supplies the canonical
Ostrowski word $\delta$ of $R$, with



$$
\frac{a}{2c}\le R<\frac a2,
\qquad
E(\delta)=\sigma\kappa,
\qquad
U(\delta)=\epsilon a,
\qquad
\sigma=(-1)^n\epsilon.
\tag{1.5}
$$



Item 337 attaches the exact overlap-normalized cofactor tower



$$
\Lambda(\delta)
=\operatorname{lcm}_{\substack{3\le j\le m\\
\mathfrak z_j\ne0}}|\mathfrak z_j|,
\qquad
\mathfrak z_j
=\epsilon(\delta_j-w_j\delta_{j-1}),
\tag{1.6}
$$



and, for a declared de-overlapped target divisor $Q\mid b$,



$$
\Gamma_Q(\delta)=\log\gcd(Q,\Lambda(\delta)).
\tag{1.7}
$$



Item 340 imposes the actual seed complement and closes the natural **full
canonical complement loop**.

> **PROVED — FULL COMPLEMENT-INVERSE RESONANCE.**  Canonically
> redigitize $t$ at the previous scale, form $\kappa=c-t$, apply the
> exact dual inverse modulo $a$, and canonically redigitize the returned
> residue.  For every $n\ge5$, this loop returns
>
> 

$$
> \boxed{\overline R=R\bmod a,\qquad 0\le\overline R<a.}
> \tag{1.8}
>
$$


>
> Its exact dual coordinates are
>
> 

$$
> \boxed{
> \overline E=\sigma\kappa,
> \qquad
> \overline U=\epsilon a-h,
> \qquad
> h=\frac{R-\overline R}{a}=\left\lfloor\frac Ra\right\rfloor,
> \qquad 0\le h\le\frac A2.}
> \tag{1.9}
>
$$



Under a hypothetical Item-316 failure, $R<a/2<a$, so $h=0$,
$\overline R=R$, and uniqueness of canonical expansion gives



$$
\boxed{
\overline\delta=\delta,
\qquad
\overline{\mathfrak z}_j=\mathfrak z_j,
\qquad
\overline\Lambda=\Lambda.}
\tag{1.10}
$$



Thus the full value-preserving complement redigitization does not create a
second target or a second cofactor tower.  It returns the original tower
exactly on the actual family.  Off target, its only equality defect is the
small Euclidean quotient $h$, whose nonzero divisor mass is at most
$\log(A/2)=o(\log b)$.

There is also an exact all-composite-modulus collapse.  If $t_\theta$
is the value of a formal complement digit word and $R_\delta$ the value
of a formal target word, then for every $Q\mid b$, after adjoining the
actual small-error and appended target defects
$\mathcal E_\sigma(\delta)$ and
$\mathcal D_\epsilon(\delta)$,



$$
\boxed{
(Q,\mathcal E_\sigma,\mathcal D_\epsilon,
b t_\theta-T-\epsilon R_\delta)
=(Q,\mathcal E_\sigma,\mathcal D_\epsilon,
a^2-\epsilon R_\delta).}
\tag{1.11}
$$



Hence direct reduction of the complete complement incidence modulo $Q$
forgets every complement digit and gives only the old signed-square ray.
The corresponding exact quotient lift is



$$
\boxed{
t\equiv\ell\pmod Q
\iff
T+\epsilon R\equiv b\ell\pmod{bQ}.}
\tag{1.12}
$$



The complement quotient itself is not low height.  For $n\ge9$,



$$
\boxed{
\frac{3b}{2A^3}<t<
\frac{4b}{A(A-4)(A-8)},
\qquad
\log t=\log b-3\log A+O(1).}
\tag{1.13}
$$



Therefore Item 340 is a scoped no-go, not a capacity reduction.  It closes
the natural value-preserving complement loop and its undivided
$Q$-level congruence class.  It does **not** close a genuinely joint,
non-value-preserving statistic of the complement digits and the original
cofactor tower, or arithmetic after the $bQ$ lift.

The actual shared mass $\Gamma_Q$ remains open.  Booking is zero.

## 2. Continuants, signs, and the seed complement

Put



$$
w_1=7,
\qquad
w_j=4j+2\quad(2\le j\le m),
\tag{2.1}
$$



and define



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
Q_m=a,
\qquad Q_{m-1}=c,
\qquad Q_{m-2}=d,
\qquad S:=P_m.
\tag{2.4}
$$



The convergent determinant at depth $m-1$ gives



$$
\boxed{cS-P_{m-1}a=(-1)^{m-1}=(-1)^{n-3}.}
\tag{2.5}
$$



In particular, $S$ is a unit modulo $a$.

The definitions (1.3)-(1.4) give the unconditional seed identity



$$
\boxed{bt=T+\epsilon R.}
\tag{2.6}
$$



Indeed,



$$
b(c-\kappa)
=bc-b\kappa
=(bc-a^2)+(a^2-b\kappa).
\tag{2.7}
$$



For $n\ge5$, Item 295 gives



$$
0<\kappa<c,
\qquad
0<t<c.
\tag{2.8}
$$



Thus $t$ has a unique canonical Ostrowski expansion in the previous
basis:



$$
t=t_\theta
=\sum_{i=1}^{m-1}\theta_iQ_{i-1}.
\tag{2.9}
$$



This word is seed-only: it exists for every $n$, whether or not the
half-bound fails.  Under a target it is canonically forced, but it is not
a second independently chosen period.

## 3. Exact evaluation of the full complement loop

The square remainder identity gives, modulo $a$,



$$
\epsilon R\equiv-\kappa c\pmod a.
\tag{3.1}
$$



Multiplying by $S$ and using (2.5),



$$
\begin{aligned}
\epsilon RS
&\equiv-\kappa cS\pmod a\\
&\equiv-\kappa(-1)^{n-3}\pmod a\\
&\equiv(-1)^n\kappa\pmod a.
\end{aligned}
\tag{3.2}
$$



Since $\sigma=(-1)^n\epsilon$, this is



$$
\boxed{RS\equiv\sigma\kappa\pmod a.}
\tag{3.3}
$$



Now perform the natural full complement loop.  Starting from the canonical
word $\theta$, recover its value $t$, put $\kappa=c-t$, and define



$$
\boxed{
\overline R
=\operatorname{res}_{[0,a)}
\bigl(\sigma\kappa S^{-1}\bmod a\bigr).}
\tag{3.4}
$$



Equation (3.3) proves (1.8):



$$
\overline R=R-a\left\lfloor\frac Ra\right\rfloor.
\tag{3.5}
$$



Let $\overline\delta$ be the unique canonical word for
$\overline R$, and let $\overline E$ be its exact dual error.  The
dual-error lemma gives



$$
\overline E\equiv\overline RS
\equiv\sigma\kappa\pmod a,
\qquad
-S<\overline E<a-S.
\tag{3.6}
$$



Both possible signed values $\sigma\kappa$ lie in the same open
interval.  Indeed, Item 316 gives



$$
S>c,
\qquad
a>S+c,
\tag{3.7}
$$



and (2.8) then gives



$$
-S<-\kappa<0<\kappa<a-S.
\tag{3.8}
$$



Two congruent integers in an interval of length $a$ are equal, so



$$
\boxed{\overline E=\sigma\kappa.}
\tag{3.9}
$$



The exact master identity is



$$
a\overline U=(-1)^n b\overline E+\overline R.
\tag{3.10}
$$



Substituting (3.9), using $(-1)^n\sigma=\epsilon$, and multiplying
$a^2=b\kappa+\epsilon R$ by $\epsilon$, one obtains



$$
\begin{aligned}
a\overline U
&=\epsilon b\kappa+\overline R\\
&=\epsilon a^2-R+\overline R\\
&=\epsilon a^2-ha,
\end{aligned}
\tag{3.11}
$$



where



$$
h=\frac{R-\overline R}{a}
=\left\lfloor\frac Ra\right\rfloor.
\tag{3.12}
$$



This proves (1.9).

The quotient is uniformly small.  Since $R<b/2$, $c<a$, and
$b=Aa+c<(A+1)a$,



$$
0\le h<\frac{A+1}{2}.
\tag{3.13}
$$



Because $A$ is even,



$$
\boxed{0\le h\le A/2.}
\tag{3.14}
$$



No finite row or asymptotic guess enters this theorem.

## 4. Consequence on the actual Item-316 family

Assume now that the half-bound fails.  Then Item 316 gives



$$
R<\frac a2<a.
\tag{4.1}
$$



Equations (3.5) and (3.12) become



$$
\overline R=R,
\qquad h=0.
\tag{4.2}
$$



Canonical Ostrowski expansion is unique, hence



$$
\overline\delta=\delta.
\tag{4.3}
$$



Every adjacent cofactor and every function of the complete digit word is
therefore literally reproduced.  In particular,



$$
\overline{\mathfrak z}_j=\mathfrak z_j
\quad(3\le j\le m),
\qquad
\overline\Lambda=\Lambda.
\tag{4.4}
$$



This is stronger than a rank or congruence comparison: the two canonical
words are identical integers digit by digit.  Consequently it is invalid
to book the returned tower as an independent copy of Item 337's bulk
invariant.

The theorem closes precisely the following operation:

1. canonically redigitize the exact seed complement $t$;
2. recover $\kappa=c-t$;
3. apply the exact dual inverse modulo $a$; and
4. canonically redigitize the returned least residue.

It does not assert that every nonlinear statistic comparing the two digit
tapes is trivial.  Such a statistic is outside the value-preserving loop
and must be justified separately from the actual collision.

## 5. Capacity audit of the loop and of the complement value

If $h\ne0$, its entire prime-power mass is



$$
\sum_pv_p(h)\log p=\log h\le\log(A/2)=O(\log n).
\tag{5.1}
$$



Since



$$
\log b=n\log n+O(n),
\tag{5.2}
$$



the loop defect has zero beta rate.  On an actual target $h=0$, but
that zero is the old exact target equality and cannot be treated as an
integer with an infinite divisor reservoir.

The complement value $t$ itself has the opposite capacity profile.
For $n\ge9$, Item 320 gives



$$
3d<t<4d.
\tag{5.3}
$$



Writing $e=q_{n-4}$, the recurrences give



$$
c=(A-8)d+e,
\qquad
a=(A-4)c+d,
\qquad
b=Aa+c,
\qquad 0<e<d.
\tag{5.4}
$$



Thus



$$
b<2A^3d,
\qquad
b>A(A-4)(A-8)d.
\tag{5.5}
$$



Combining (5.3)-(5.5) proves (1.13).  In particular, $t$ retains one
full beta-scale logarithmic copy up to only $O(\log n)$.

This does not make $t$ bookable.  The sequence $t_n$, and therefore
its canonical word $\theta$, is defined for every seed row independently
of whether the target exists.  A theorem about $t$ alone must first be
coupled to the actual cofactor hit before it can affect $\Gamma_Q$.

The capacity decision is therefore exact:



$$
\begin{array}{c|c|c}
\text{object}&\text{raw beta-scale height}&\text{incremental status}\\ \hline
h&0&\text{zero-rate loop defect}\\
t&1&\text{seed-only; correlation missing}\\
\overline\Lambda&\text{same as }\Lambda&\text{exact duplicate on target}.
\end{array}
\tag{5.6}
$$



## 6. Exact mod-$Q$ collapse of the complement incidence

Let $R_\delta$ denote the value of formal target digits and let
$t_\theta$ denote the value of formal complement digits.  Work in the
integer polynomial ring in both digit sets.  Let



$$
\mathcal E_\sigma(\delta)=E(\delta)-\sigma\kappa,
\qquad
\mathcal D_\epsilon(\delta)=U(\delta)-\epsilon a
\tag{6.0}
$$



be the exact Item-316 small-error and appended target defects; on the
actual family they vanish.

Define the complement incidence



$$
F=b t_\theta-T-\epsilon R_\delta.
\tag{6.1}
$$



Since $T=bc-a^2$,



$$
F=b(t_\theta-c)+a^2-\epsilon R_\delta.
\tag{6.2}
$$



For every integer divisor $Q\mid b$, the polynomial
$b(t_\theta-c)$ belongs to the ideal $(Q)$.  Hence



$$
(Q,\mathcal E_\sigma,\mathcal D_\epsilon,F)
=(Q,\mathcal E_\sigma,\mathcal D_\epsilon,
a^2-\epsilon R_\delta),
\tag{6.3}
$$



which proves (1.11) over every composite modulus, with all prime powers
retained.

Modulo $Q$, the complete complement word is therefore algebraically
free over the old target quotient ring.  The only surviving condition
from (6.1) is



$$
R_\delta\equiv\epsilon a^2\pmod Q,
\tag{6.4}
$$



the signed-square ray already present before redigitization.

Canonical digit inequalities are not polynomial ideal relations.  They
can still create a nontrivial arithmetic correlation.  Equation (6.3)
proves only that such progress cannot come from reducing the undivided
incidence modulo $Q$.

To retain the quotient, one must lift before dividing.  From (2.6), for
every integer $\ell$,



$$
\begin{aligned}
T+\epsilon R\equiv b\ell\pmod{bQ}
&\iff b(t-\ell)\equiv0\pmod{bQ}\\
&\iff t\equiv\ell\pmod Q.
\end{aligned}
\tag{6.5}
$$



This proves the quotient bridge (1.12).  Equivalently, for every prime
$p\mid Q$,



$$
\boxed{
v_p(T+\epsilon R)=v_p(b)+v_p(t).}
\tag{6.6}
$$



The extra valuation is genuine transverse information, but no density or
gcd theorem for it is proved here.

## 7. Exact isolation of the missing $\Gamma_Q$ correlation

Assume the actual Item-316 target and put



$$
G_Q=\gcd(Q,\Lambda),
\qquad
H_Q=\gcd(G_Q,t),
\qquad
K_Q=G_Q/H_Q.
\tag{7.1}
$$



Then



$$
\boxed{
\Gamma_Q
=\log H_Q+\log K_Q.}
\tag{7.2}
$$



The first term is the valuation mass covered simultaneously by the target,
the cofactor tower, and the complement quotient.  The second is the exact
remaining cofactor valuation after the multiplicity available from $t$
has been removed.  In particular,



$$
0\le\log H_Q\le\log\gcd(Q,t)\le\log t,
\tag{7.3}
$$



while



$$
0\le\log K_Q\le\log Q.
\tag{7.4}
$$



By (1.13), neither upper bound is sublinear on the beta scale.  The
complement loop supplies no relation forcing $K_Q=1$, and the quotient
bridge supplies no bound for $H_Q$.

Thus the smallest remaining target-specific problem is now explicit.  A
Closer must prove, after every old denominator factor is removed, enough of



$$
\log H_Q=o(\log b),
\qquad
\log K_Q=o(\log b)
\tag{7.5}
$$



to reduce $\Gamma_Q$.  A Builder must prove a positive-linear lower
bound for one of these terms on the actual family.  A result about the
seed-only complement word, the duplicated loop tower, or bounded rows does
not satisfy either requirement.

Equivalently, any successful complement argument must use a genuinely
joint statistic of



$$
\boxed{
p^e\mid Q,
\qquad
p^e\mid\mathfrak z_j(\delta)\text{ for some }j,
\qquad
\theta=\operatorname{Ost}_{m-1}(t),}
\tag{7.6}
$$



through the canonical digit map or the $bQ$ quotient lift.  This is the
missing correlation; it is not contained in the old target ideal.

## 8. Strict labels

### PROVED

* The unconditional seed identity $bt=T+\epsilon R$.
* The exact full complement-inverse return
  $\overline R=R\bmod a$.
* The exact returned dual coordinates
  $\overline E=\sigma\kappa$ and
  $\overline U=\epsilon a-h$.
* The uniform quotient bound $0\le h\le A/2$.
* Conditional on an Item-316 failure, digitwise identity of the returned
  word, the original word, and their complete cofactor towers.
* The zero-rate bound for every nonzero loop defect $h$.
* The full raw height of $t$, equation (1.13).
* The all-composite-modulus ideal identity (1.11).
* The exact $bQ$ quotient and valuation bridges (1.12), (6.6).
* The exact complement-covered/excess decomposition (7.2).

### PROVED SCOPED NO-GO

* Full value-preserving canonical redigitization of the seed complement,
  followed by the exact dual inverse, returns the original target word and
  cannot be booked as an independent bulk invariant.
* Its only off-target equality defect has zero beta rate.
* Direct undivided reduction of the complete complement incidence modulo
  any $Q\mid b$ adds no condition beyond the old signed-square ray.
* This no-go does not include non-value-preserving joint digit statistics
  or arithmetic after the $bQ$ lift.

### EXACT FINITE ONLY

* The deterministic replay's declared seed rows, canonical
  redigitizations, loop identities, quotient bridges, and lcm/gcd
  decompositions.
* The rows verify exact identities only.  They perform no half-bound census
  and are never promoted to an actual target theorem.

### OPEN

* The original Item-316 all-digit exclusion and centered half-bound.
* Any weighted correlation between the actual $\delta$-cofactor tower
  and the seed complement digits $\theta$.
* Bounds or positive lower estimates for $H_Q$, $K_Q$, or
  $\Gamma_Q$.
* Distribution of the quotient lift modulo $bQ$.
* Removal of every old denominator reservoir on the actual family.
* Beta capacity, Route 1, and every conclusion about $e+\pi$.

### BOOKING



$$
\boxed{
\text{new beta capacity reduction}=0,
\qquad
\text{new Route-1 rate}=0.}
\tag{8.1}
$$



No canonical, master, status, checkpoint, or research-log file is edited
by this work package.

## 9. Deterministic replay

From the archive root:

~~~text
python work/item340_beta_full_complement_loop_correlation_certificate.py ^
  --output work/item340_beta_full_complement_loop_correlation_certificate.replay.json
~~~

The checker uses only the Python standard library and exact integer
arithmetic.  It performs no half-bound scan and promotes no bounded row.
