> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 272 — complete-row translation dynamics admission for the ordinary $j=2$ gate

Checked: 2026-08-31 (Beijing time)

## 1. Verdict

Fix one of the two actual prime phases



$$
p=6q+e,\qquad e\in\{5,1\}.
$$



The natural same-prime row shift is



$$
\sigma(\delta)=\delta+2,\qquad
\sigma(r)=r+6,\qquad
\sigma(s)=s-2,\qquad \sigma(q)=q,                 \tag{1.1}
$$



where



$$
\begin{array}{c|c|c|c}
e&r&s&\text{actual odd cutoffs}\\ \hline
5&3\delta-2&q-\delta+1&\delta\ge1,\\
1&3\delta-4&q-\delta+1&\delta\ge3.
\end{array}                                                \tag{1.2}
$$



The shift is used only while $s\ge3$.  It preserves the prime, the
phase, $\epsilon=(2/p)$, and the sign $\sigma_m=(-1)^m$, since
$m=q-\delta$ changes by $-2$.

> **PROVED — a rank-seven partial translation module.**  The exact
> coordinates
> 

$$
> 1,\quad c=2^{2s},\quad B_s,\quad \kappa_r,\quad
> \tau_{r,s},\quad D_\delta,\quad
> \Delta_\delta=D_{\delta+2}-D_\delta                   \tag{1.3}
>
$$


> form a rank-seven rational translation-difference module over
> $\mathbb Q(q,\delta)$.  Its update is displayed in Section 3.

> **PROVED SCOPED NO-GO — the hard Item-250 block is not another
> same-complexity rank-one summand.**  In either phase, none of
> 

$$
> f_0,f_1,P_0^\flat,P_1^\flat,H_0^\flat,H_1^\flat        \tag{1.4}
>
$$


> satisfies a nonzero scalar relation
> 

$$
> A(n)a_n+B(n)a_{n+1}=0,qquad
> A,B\in\mathbb Q[n],\quad \deg A,\deg B\le7,             \tag{1.5}
>
$$


> along $r=r_e+6n$.  The exact modular-rank certificate in Section 5
> proves this class exclusion.  Degree seven is the natural complexity
> envelope of the already proved $D_\delta$ recurrence.  This theorem
> does **not** exclude a higher-rank module or a higher-degree scalar
> recurrence.

> **OPEN — complete-row closure.**  No exact bounded-rank update is
> constructed for
> 

$$
> W=(f_0,f_1,U_0,U_1),qquad
> U_\nu=P_\nu^\flat c+H_\nu^\flat,                         \tag{1.6}
>
$$


> or, equivalently, for the coefficient refinement (1.4).  Therefore the
> full two-row matrix remains external to the proved rank-seven state.

There is consequently no new lisse/crystalline realization, monodromy
theorem, local-density estimate, or strict retained ceiling.  The raw
ordinary-$j=2$ capacity is still



$$
\boxed{\frac{2}{35}\text{ per }M
=\frac{1}{105}\text{ per }6M},\qquad
\boxed{\text{new Route-1 booking}=0}.                       \tag{1.7}
$$



The bounded row replays are **EXACT FINITE ONLY**.  The finite modular
matrices in Section 5 prove the stated bounded-complexity class exclusion;
they are not used to extrapolate a recurrence or a zero density.

## 2. The complete matrix and the entries that must move

Retain Item 269's exact vector



$$
x_p=(1,H_q,h_q)^{\mathsf T}.
$$



Put



$$
\alpha_r=\frac{9\kappa_r}{2},\qquad
A_s=\sigma_m\{\epsilon(H_q-D_\delta h_q)-1\}.              \tag{2.1}
$$



Then



$$
Z=B_s(\alpha_rA_s-\tau_{r,s})=z_{r,s}x_p,                  \tag{2.2}
$$



where



$$
z_{r,s}=B_s
\left(
-\alpha_r\sigma_m-\tau_{r,s},
\alpha_r\sigma_m\epsilon,
-\alpha_r\sigma_m\epsilon D_\delta
\right).                                                    \tag{2.3}
$$



The two exact rows are



$$
R_{\nu,r,s}=f_\nu z_{r,s}+(U_\nu,0,0),\qquad \nu=0,1,     \tag{2.4}
$$



and the full collision is



$$
G_0=G_1=0
\quad\Longleftrightarrow\quad
R_{r,s}x_p=0.                                               \tag{2.5}
$$



Thus the requested complete-row list is exactly



$$
f_0,f_1,U_0,U_1,B_s,\kappa_r,\tau_{r,s},D_\delta.          \tag{2.6}
$$



Sections 3–4 close the last four entries.  Section 5 isolates the first
four as the smallest missing block.  Tracking only the period line is
not sufficient: at the exact $e=5,\delta=1,r=1$ endpoint,



$$
f_0=0,\qquad U_0=-81c-33,\qquad
R_{0,r,s}=(U_0,0,0).                                       \tag{2.7}
$$



Hence the zeroth row is a genuine $U_0$ condition there and cannot be
replaced by a slope or period equation.

## 3. Exact rank-seven update

Write $h=(r-1)/2$.  Elementary factorial and Pochhammer cancellation
gives



$$
\frac{c'}c=\frac1{16},                                    \tag{3.1}
$$





$$
\frac{B_{s-2}}{B_s}
=
\frac{\prod_{j=1}^{6}(3s-j)}
{(2s-1)(2s-2)(2s-3)(2s-4)(s-1)(s-2)},                    \tag{3.2}
$$





$$
\frac{\kappa_{r+6}}{\kappa_r}
=
\frac{r(r+2)(r+4)(r+6)(2r+15)}
{27(2r+3)(2r+5)(2r+7)(2r+11)(2r+13)},                    \tag{3.3}
$$



and



$$
\frac{\tau_{r+6,s-2}}{\tau_{r,s}}
=-
\frac{(s-2)(s-1)(s+h+1)
(3s+h-1)(3s+h)(3s+h+1)}
{(3s-5)(3s-4)(3s-3)(3s-2)(3s-1)(3s)}.                   \tag{3.4}
$$



For clarity, the line break in (3.4) is multiplication: its numerator is
the product of all six displayed factors.

Let $b, k, t$ denote the rational multipliers in (3.2), (3.3),
and (3.4).  From Item 271 put



$$
d_e(\delta)=\frac{P_0^{(e)}(\delta)}{P_2^{(e)}(\delta)},
\qquad
\Delta_\delta=D_{\delta+2}-D_\delta,                       \tag{3.5}
$$



where the explicit $P_0^{(e)},P_2^{(e)}$ have degree seven.  Then



$$
Y_\delta=
(1,c,B_s,\kappa_r,\tau_{r,s},D_\delta,\Delta_\delta)^{\mathsf T}
$$



satisfies



$$
\sigma(Y)=
\begin{pmatrix}
1&0&0&0&0&0&0\\
0&1/16&0&0&0&0&0\\
0&0&b&0&0&0&0\\
0&0&0&k&0&0&0\\
0&0&0&0&t&0&0\\
0&0&0&0&0&1&1\\
0&0&0&0&0&0&d_e(\delta)
\end{pmatrix}Y.                                             \tag{3.6}
$$



This is one bounded-rank translation module, not merely a list of
unrelated recurrences.  Products needed in (2.3) lie in its finite tensor
closure.  They still do not supply $f_\nu$ or $U_\nu$.

## 4. Endpoint, unit, and singular-divisor audit

The identities follow directly from



$$
B_s=\frac{(2s-1)!(s-1)!}{(3s-1)!},                         \tag{4.1}
$$





$$
\kappa_r=
\frac{2(4h+5)}{9(4h+3)}(-1)^h
\frac{((5-2h)/6)_h}{(h+3/2)_h},                            \tag{4.2}
$$



and



$$
\tau_{r,s}=(-1)^{s+h}\frac23
\frac{(s)_{h+1}}{(3s+1)_{h+1}}.                            \tag{4.3}
$$



For example,



$$
\frac{(s-2)_{h+4}}{(s)_{h+1}}
=(s-2)(s-1)(s+h+1),                                       \tag{4.4}
$$



and cancellation of the two denominator Pochhammers leaves the final
three numerator and first six denominator factors in (3.4).  The sign
changes because $(s-2)+(h+3)=s+h+1$.

On a forward actual row $s\ge3$, all denominators in (3.1)–(3.4) are
positive and strictly below $p=2r+6s+3$, after multiplication by at
most the harmless fixed factors $2,3$.  The largest new $\kappa$
factor satisfies



$$
2r+13=p-(6s-10)<p.                                         \tag{4.5}
$$



The remaining inequalities are smaller.  Thus these four scalar updates
introduce no actual mod-$p$ pole in their forward range.

The $D$-block retains Item 271's singular divisor



$$
P_2^{(e)}(\delta)=0.                                       \tag{4.6}
$$



It can meet actual reductions even when the original slopes are defined;
the exact witnesses $(p,e,\delta)=(167,5,7)$ and $(241,1,11)$
remain in force.  Therefore even the proved partial module is not yet a
uniformly regular lisse candidate.

## 5. The smallest missing block and the scoped rank-one obstruction

Item 250 defines



$$
U_\nu=P_\nu^\flat c+H_\nu^\flat,
$$



with



$$
P_\nu^\flat=9\mathsf b_\nu,qquad
H_\nu^\flat=9\mathsf d_\nu-10u_\nu.                       \tag{5.1}
$$



All six coefficients in (1.4) are exact rational sequences of $r$,
but the sealed fixed-$r$ localization did not give their 

$$
r\mapsto
r+6
$$

 update.

The first natural admission attempt would adjoin each as a rank-one
scalar state with rational multiplier of complexity no larger than the
degree-seven $D$-recurrence.  This attempt fails exactly.  For each
phase and each sequence $a_n$ in (1.4), form the $27\times16$ matrix



$$
\mathcal M(a)=
\left(
n^j a_n\ \middle|\ n^j a_{n+1}
\right)_{
0\le n\le26,\ 0\le j\le7}.                                \tag{5.2}
$$



The certificate reconstructs every entry from the Item-250 formulas and
finds



$$
\operatorname{rank}\mathcal M(a)=16                         \tag{5.3}
$$



over each of $\mathbb F_{1000000007}$ and
$\mathbb F_{1000000009}$, for all twelve phase/sequence pairs.
Every reduced sequence denominator in (5.2) is a unit at both certificate
primes; this is checked before modular inversion.
If (1.5) existed, clearing denominators and making its integer
coefficient vector primitive would give a nonzero null vector modulo
either prime, contradicting (5.3).  This is a proof of a bounded class
exclusion, not a fitted nonrecurrence claim.

There is a second, literal-basis obstruction.  Item 250's affine chain
stores



$$
J_k=u_ke+v_kc+w_k,qquad 0\le k\le r+4,                     \tag{5.4}
$$



and the coefficient arrays of $(1-z)^r(1+z)$ and
$(1-z)^r(1+z)^4$.  Its displayed state dimension therefore grows with
$r$.  Moreover the overlap is not invariant: with
$\bar Q=-(2r+3)/3$,



$$
(u_{k+2},v_{k+2},w_{k+2})
=
\left(
-\frac{\bar Q+k}{3\bar Q+k}u_k,
\frac{1-(\bar Q+k)v_k}{3\bar Q+k},
-\frac{\bar Q+k}{3\bar Q+k}w_k
\right),                                                   \tag{5.5}
$$



while $r\mapsto r+6$ sends $\bar Q\mapsto\bar Q-4$.
Thus the literal Item-250 basis is not a bounded-rank invariant state.
This does not rule out a new creative-telescoping compression; finding
one for $W$ is the smallest exact open recurrence problem.

## 6. Fixed incidence, Frobenius admission, and capacity

If a bounded update for $W$ were constructed, adjoining it to (3.6)
would make every coefficient of (2.4) a rational function on one
finite-dimensional skew product, and (2.5) would be one fixed incidence
there.  At present this is conditional.  Merely adjoining the rows as
free coordinates is the tautological universal incidence of Item 269.

Even the conditional translation realization would not by itself be a
lisse or crystalline Frobenius realization.  The following remain open:

* an exact bounded update for $W=(f_0,f_1,U_0,U_1)$;
* regular treatment of the actual $D$-pole rows;
* a compatible integral lisse/crystalline object of uniform conductor;
* nontrivial geometric monodromy for the complete two-row collision; and
* a uniform local-density or large-sieve theorem.

Accordingly, no positive linear capacity passes the admission test.  No
part of the raw $2/35$ per $M$, equivalently $1/105$ per $6M$,
cell is removed.

## 7. Strict claim ledger

### PROVED

* The actual shift (1.1) and invariance of $q,e,\epsilon,\sigma_m$.
* The scalar ratios (3.1)–(3.4), including endpoints and units.
* The rank-seven module (3.6), using Item 271's proved $D$-block.
* The degree-seven rank-one class exclusion (5.3).
* The literal Item-250 state is growing and not invariant under the
  phase shift.
* The full row cannot be replaced by the period line, as (2.7) shows.

### EXACT FINITE ONLY

* Independent equality with the canonical Item-250 reconstruction on
  the bounded replay rows.
* The bounded rational ratio replays and output digests.

The modular ranks are exact certificates for the explicitly bounded
class (1.5); they are not an exceptional-prime or zero census.

### OPEN

* Any higher-rank or higher-degree update for the hard block $W$.
* Complete-row lisse/crystalline realization, uniform conductor,
  nontrivial monodromy, and a density theorem.
* Route 1 and every conclusion about $e+\pi$.

### BOOKING



$$
\boxed{\text{new Route-1 rate}=0,\qquad
\text{retained capacity}=\frac{2}{35}\text{ per }M
=\frac{1}{105}\text{ per }6M.}
$$


