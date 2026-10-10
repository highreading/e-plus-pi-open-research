> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 364 — tied-phase carriers for the two fixed-$j=1$ saturation boundaries

Checked: 2026-09-01 (Beijing time)

## 1. Admission, capacity, and verdict

Retain the actual fixed-$j=1$ family



$$
p=4h+6s+3,
 \qquad
 M=3h+4s+2,
 \qquad h,s\geq1,
\tag{1.1}
$$



and Item 360's normalized full gate



$$
f_0=2x-\lambda y=0,
 \qquad
 f_1=2\alpha u-\beta\lambda v=0.
\tag{1.2}
$$



The two saturation boundaries are



$$
\mathcal B_{xy}=\{x=y=0\},
 \qquad
 \mathcal B_{uv}=\{u=v=0\}.
\tag{1.3}
$$



They are not new cells.  Each can matter only after intersection with the
same full gate (1.2), whose entire raw mass is



$$
{M\over6}+o(M)
\tag{1.4}
$$



at fixed $M$, or $1/36$ per $6M$.  The two boundaries and the
nonboundary chart are therefore nonadditive.

This item obtains three exact results.

> **PROVED — fixed-$h$ tied-phase carriers.**  Put
> 

$$
> \sigma_h=-{4h+3\over6}.
>
$$


> For every potentially prime ray $3\nmid h$, specialize the four exact
> terminating periods at $s=\sigma_h$, obtaining rational numbers
> $X_h,Y_h,U_h,V_h$.  On every actual row,
> 

$$
> (x,y,u,v)\equiv(X_h,Y_h,U_h,V_h)\pmod p.
>
$$


> Hence
> 

$$
> x=y=0\Longrightarrow p\mid G_h^{(0)},
> \qquad
> u=v=0\Longrightarrow p\mid G_h^{(1)},
>
$$


> where
> 

$$
> G_h^{(0)}=\gcd(\operatorname{num}X_h,\operatorname{num}Y_h),
> \qquad
> G_h^{(1)}=\gcd(\operatorname{num}U_h,\operatorname{num}V_h).
>
$$


> If the relevant rational pair is not identically zero at this phase,
> the corresponding fixed $h$ contains only finitely many possible
> boundary primes.  An exact-zero phase pair is retained as a separate
> exceptional stratum.  In either case, every fixed finite collection of
> $h$-rays has zero asymptotic mass.

> **PROVED — the genuine $h=2$ degeneracy is harmless.**  Here
> $K_1=(1-z^2)^4$, so $v=0$ identically, but
> 

$$
> u={4(64s^2+80s+27)\over9(3s+1)(3s+2)}.
>
$$


> If $u=0\pmod p$ on $p=6s+11$, then $p\mid859$.  The integer
> $859$ is prime and is $1\pmod6$, whereas every prime on this ray is
> $5\pmod6$.  Therefore $u=v=0$ never occurs on the actual $h=2$
> ray.

> **PROVED — complete fixed-strip boundary exclusion.**  Neither boundary
> occurs on any actual tied row with $1\leq h\leq8$.  This is an
> all-$s$ theorem on those rays, not a bounded prime scan.

The global weighted problem remains open.  The carrier heights satisfy



$$
\log\max(1,G_h^{(0)},G_h^{(1)})=O(h\log(h+2)),
\tag{1.5}
$$



but summing this pointwise bound over the fixed-$M$ row gives only
$O(M^2\log M)$, far above the $o(M)$ target.  An explicit order-one
comparison carrier shows rigorously that recurrence order and a bound of
the form (1.5), by themselves, cannot force even zero rate on a
positive-rate bulk.

Consequently



$$
\boxed{\text{new booking}=0},
 \qquad
 \boxed{\text{new capacity reduction}=0},
 \qquad
 \boxed{\text{full fixed-}j=1\text{ ceiling remains }1/36}.
\tag{1.6}
$$



Whether either boundary occurs for unbounded $h$ is **OPEN**.

## 2. Exact arithmetic meaning of the two boundaries

Use Item 218's four terminating periods



$$
\begin{aligned}
 x&=\operatorname{Odd}(K_0;s,2s),
 &y&=\operatorname{Odd}(K_0;h,2s),\\
 u&=\operatorname{Even}(K_1;s,2s-1),
 &v&=\operatorname{Odd}(K_1;h,2s-1),
\end{aligned}
\tag{2.1}
$$



where



$$
K_0=(1-z)^{2h}(1+z),
 \qquad
 K_1=(1-z)^{2h}(1+z)^4.
\tag{2.2}
$$



If $H_\nu(N)=[z^N]P_\nu(z)\log(1+z^2)$, the exact tail reduction is



$$
\begin{array}{ll}
 H_0(T)=\mathsf A x,&H_0(L_0)=\mathsf B y,\\
 H_1(T)=\mathsf C u,&H_1(L_1)=\mathsf D v,
\end{array}
\tag{2.3}
$$



with



$$
T=2h+6s+2,
 \qquad
 L_0=4h+4s+2,
 \qquad
 L_1=4h+4s+3.
\tag{2.4}
$$



Every prefactor in (2.3) is a $p$-unit.  Therefore



$$
\boxed{
 \mathcal B_{xy}\iff H_0(T)=H_0(L_0)=0\pmod p,}
\tag{2.5}
$$



and



$$
\boxed{
 \mathcal B_{uv}\iff H_1(T)=H_1(L_1)=0\pmod p.}
\tag{2.6}
$$



Thus each boundary means that the two endpoint tails of one original
divided coordinate vanish separately.  It is stronger than vanishing of
their prescribed linear combination.

This distinction must not be confused with the full collision.  On
$\mathcal B_{xy}$, the equations $f_0=H=0$ are automatic, but an
actual collision still requires



$$
f_1=2\alpha u-\beta\lambda v=0.
\tag{2.7}
$$



Similarly, on $\mathcal B_{uv}$, an actual collision still requires



$$
f_0=2x-\lambda y=0.
\tag{2.8}
$$



The boundary supports studied below therefore overcount full collisions.
This is safe for an upper bound but cannot create a new booking.

## 3. Exact tied-phase specialization

For a polynomial $K(z)=\sum_jK_jz^j$, recall



$$
\operatorname{Odd}(K;a,q)
 =\sum_{t\geq0}(-1)^t{(a+1)_t\over(q+a+2)_t}K_{2t+1},
\tag{3.1}
$$



and



$$
\operatorname{Even}(K;a,q)
 =\sum_{t\geq0}(-1)^t{(a)_t\over(q+a+1)_t}K_{2t}.
\tag{3.2}
$$



Both sums terminate.  For fixed $h$, regard their $s$-dependence as
rational functions over $\mathbb Q(s)$.  The tied identity in (1.1)
gives



$$
\boxed{s\equiv\sigma_h:=-{4h+3\over6}\pmod p.}
\tag{3.3}
$$



If $3\mid h$, then $p\equiv h\equiv0\pmod3$; since $p>3$, no
actual prime exists.  Hence assume $3\nmid h$, and define



$$
\begin{aligned}
 X_h&=\operatorname{Odd}(K_0;\sigma_h,2\sigma_h),
 &Y_h&=\operatorname{Odd}(K_0;h,2\sigma_h),\\
 U_h&=\operatorname{Even}(K_1;\sigma_h,2\sigma_h-1),
 &V_h&=\operatorname{Odd}(K_1;h,2\sigma_h-1).
\end{aligned}
\tag{3.4}
$$



Every denominator in the original positive-$s$ sums is strictly between
$0$ and $p$.  Substitution of (3.3) therefore commutes with reduction
modulo $p$.  In particular, the denominators of the reduced rational
numbers in (3.4) are $p$-units on any row on which they are used.  Thus



$$
\boxed{(x,y,u,v)\equiv(X_h,Y_h,U_h,V_h)\pmod p.}
\tag{3.5}
$$



Write a rational number in lowest terms and define, with
$\gcd(0,0)=0$,



$$
G_h^{(0)}
 =\gcd\bigl(|\operatorname{num}X_h|,
            |\operatorname{num}Y_h|\bigr),
\tag{3.6}
$$





$$
G_h^{(1)}
 =\gcd\bigl(|\operatorname{num}U_h|,
            |\operatorname{num}V_h|\bigr).
\tag{3.7}
$$



Equations (3.5)–(3.7) prove



$$
\boxed{
 \mathcal B_{xy}\Longrightarrow p\mid G_h^{(0)},
 \qquad
 \mathcal B_{uv}\Longrightarrow p\mid G_h^{(1)}.}
\tag{3.8}
$$



This is stronger than taking a resultant of two numerator polynomials in
$s$: the actual linear phase has already been imposed before the gcd is
formed.  If $G_h^{(i)}\ne0$, only its finitely many prime divisors can
support that boundary on the fixed $h$-ray.  If $G_h^{(i)}=0$, both
phase values vanish exactly in characteristic zero and the entire ray must
instead be retained as an exact-zero exceptional stratum.  No theorem
excluding such $h$ globally is claimed.  Regardless of this dichotomy,
every fixed finite collection of $h$-rays contributes only
$O(\log M)=o(M)$ at fixed $M$.

## 4. The $h=2$ degenerate face

At $h=2$, the second kernel becomes



$$
K_1=(1-z)^4(1+z)^4=(1-z^2)^4.
\tag{4.1}
$$



It has no odd coefficients, hence



$$
\boxed{v=0\quad\text{for every }s.}
\tag{4.2}
$$



The even sum has only five terms.  Exact simplification gives



$$
\boxed{
 u=\sum_{t=0}^{4}{4\choose t}{(s)_t\over(3s)_t}
 ={4(64s^2+80s+27)\over9(3s+1)(3s+2)}.}
\tag{4.3}
$$



All denominator factors in (4.3) are $p$-units.  On the tied ray
$p=6s+11$, substitution $s\equiv-11/6$ gives



$$
U_2={13744\over5103}
 ={16\cdot859\over3^6\cdot7}.
\tag{4.4}
$$



The integer $859$ is prime.  Thus $u=v=0\pmod p$ would force
$p=859$.  But



$$
p=6s+11\equiv5\pmod6,
 \qquad
 859\equiv1\pmod6,
\tag{4.5}
$$



a contradiction.  This proves the all-$s$ exclusion on the only ray
where one entire boundary coordinate vanishes identically.

## 5. Complete all-$s$ boundary exclusion through $h=8$

The tied-phase carriers on the potentially prime rays through $h=8$
are



$$
\begin{array}{c|c|c}
 h&G_h^{(0)}&G_h^{(1)}\\ \hline
 1&2&2^2\\
 2&2&2^4\cdot859\\
 4&2\cdot7&2\\
 5&2&2^3\\
 7&2\cdot13&2^2\\
 8&2&1.
\end{array}
\tag{5.1}
$$



For $h=3,6$, every tied value of $p$ is a composite multiple of $3$.
For every other row in (5.1), no prime factor of either carrier has the
form



$$
p=4h+6s+3,
 \qquad s\geq1.
\tag{5.2}
$$



The only carrier factor larger than the immediate lower bound is the
(859) in (4.4), and (4.5) excludes it.  Hence



$$
\boxed{
 \mathcal B_{xy}=\mathcal B_{uv}=\varnothing
 \quad\text{on every actual row with }1\leq h\leq8.}
\tag{5.3}
$$



The certificate stores the exact four rational phase values behind every
entry of (5.1).  These six fixed-$h$ rows were declared in advance and
are not a prime scan.  Equation (5.3) is an all-$s$ consequence of the
carrier factorization.

## 6. Height, recurrence, and resultant scope

Each expression in (3.4) contains at most $h+3$ terms.  After replacing
$s$ by $\sigma_h$, every Pochhammer factor is a rational linear factor
of size $O(h)$ with denominator dividing a power of $6$.  The nested
denominator chains admit one common product of $O(h)$ such factors.
Together with



$$
\max_j|[z^j]K_0|\leq2^{2h+1},
 \qquad
 \max_j|[z^j]K_1|\leq2^{2h+4},
\tag{6.1}
$$



this proves



$$
\log\max\bigl(
 |\operatorname{num}X_h|,|\operatorname{num}Y_h|,
 |\operatorname{num}U_h|,|\operatorname{num}V_h|,
 \operatorname{den}X_h,\ldots,\operatorname{den}V_h
 \bigr)
 =O(h\log(h+2)).
\tag{6.2}
$$



In particular, (1.5) follows, with the convention $G_h^{(i)}=0$ on an
exact-zero pair.  But at fixed $M$,



$$
h=3M-2p,
 \qquad
 p={3M-h\over2},
 \qquad
 1\leq h\leq{M-6\over3}.
\tag{6.3}
$$



The direct product estimate supplied by (6.2) is only



$$
\sum_{h\ll M}\log\max\bigl(1,G_h^{(0)}G_h^{(1)}\bigr)
 =O(M^2\log M),
\tag{6.4}
$$



whereas a useful boundary closure needs $o(M)$.  Fixed-$h$ resultants
and their pointwise height therefore do not reach the ledger scale.

The limitation is not merely that the constant in (6.2) is loose.  Define
the comparison integer



$$
\mathcal C_h={ (18h)!\over(4h)!}=(4h+1)_{14h}.
\tag{6.5}
$$



It has the first-order hypergeometric recurrence



$$
{\mathcal C_{h+1}\over\mathcal C_h}
 ={\prod_{j=1}^{18}(18h+j)\over
   \prod_{j=1}^{4}(4h+j)},
\tag{6.6}
$$



and



$$
\log\mathcal C_h=O(h\log(h+2)).
\tag{6.7}
$$



Nevertheless, on the positive-rate bulk $M/12\leq h\leq M/3$,



$$
4h<p={3M-h\over2}<18h,
\tag{6.8}
$$



so every actual candidate prime divides $\mathcal C_h$.  That bulk is
the prime interval



$$
{4M\over3}\leq p\leq{35M\over24},
\tag{6.9}
$$



with raw Chebyshev mass $M/8+o(M)$, or capacity $1/48$ per $6M$.
Indeed, every odd prime in this interval, apart from $O(1)$ endpoint
adjustments, gives integral
$h=3M-2p$ and $s=(3p-4M-1)/2$; the prime number theorem therefore
applies to the whole interval rather than to a thinner progression.
Thus even an order-one recurrence plus pointwise $O(h\log h)$ height can
carry positive linear mass.

The comparison family is not asserted to resemble the actual periods.
It proves only the scoped statement



$$
\boxed{
 \text{generic recurrence order and pointwise height alone cannot prove
 weighted zero rate for (3.8).}}
\tag{6.10}
$$



A target-specific unit Casoratian, a large-prime-factor restriction, or an
average-gcd theorem for the actual $G_h^{(i)}$ could still succeed.

## 7. Exact remaining weighted target

Let $h$ run through the fixed-$M$ congruence class for which $s$ in
(1.1) is integral, and put $p_h=(3M-h)/2$.  Define the exact-zero sets



$$
\mathcal Z_0=\{h:X_h=Y_h=0\text{ in }\mathbb Q\},
 \qquad
 \mathcal Z_1=\{h:U_h=V_h=0\text{ in }\mathbb Q\}.
\tag{7.1}
$$



A sufficient boundary estimate is



$$
\boxed{
 \sum_{\substack{h\text{ actual at }M\\p_h\text{ prime}}}
 (\log p_h)
 \left(
  1_{h\in\mathcal Z_0\cup\mathcal Z_1}
  +1_{G_h^{(0)}G_h^{(1)}\ne0}\,
   1_{p_h\mid G_h^{(0)}G_h^{(1)}}
 \right)
 =o(M).}
\tag{7.2}
$$



Equation (7.2) would make both saturation boundaries zero rate.  It would
not by itself remove the whole $1/36$ cell: the nonboundary part of the
full gate remains.  Its role would be to justify using the saturated
codimension-two chart outside an $o(M)$ exceptional set.

No estimate of the form (7.2), no classification of the exact-zero sets,
no actual unbounded-$h$ boundary example, and no global nonoccurrence
theorem is proved here.  The rigorous outcome is therefore a fixed-ray
localization with exact-zero stratification and a method-class barrier,
not a capacity saving.

## 8. Strict labels and deterministic replay

### PROVED

- the endpoint-tail meaning (2.5)–(2.6);
- the full-gate residual conditions (2.7)–(2.8);
- the all-parameter tied-phase bridge (3.3)–(3.8);
- fixed-$h$ zero rate;
- the all-$s$ $h=2$ degeneracy and exclusion;
- complete all-$s$ exclusion of both boundaries through $h=8$;
- the height bound (6.2);
- the comparison obstruction (6.5)–(6.10);
- zero booking and retention of the shared $1/36$ ceiling.

### EXACT FINITE ONLY

- six predeclared fixed-$h$ carrier controls;
- four predeclared comparison rows;
- no prime scan, collision census, or extrapolation.

### OPEN

- occurrence or nonoccurrence of either boundary for unbounded $h$;
- the exact-zero phase sets and the weighted estimate (7.2);
- a target-specific unit Casoratian, large-prime-factor theorem, or
  average-gcd theorem;
- any strict fixed-$j=1$ capacity reduction, Route 1, and every conclusion
  about $e+\pi$.

The ledger remains at booking (0), reduction (0), and a shared full-cell
ceiling $1/36$ per $6M$.
