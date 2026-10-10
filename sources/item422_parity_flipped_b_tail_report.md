> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 422 — the parity-flipped upper-$B$ tail closes into the old $v$-column

Checked: 2026-09-01 (Beijing time)

Status: **ROOT-AUDITED CANONICAL PARITY-TAIL CLOSURE, ZERO BOOKING**

## 1. Scope, capacity first, and verdict

Retain an actual ordinary-$j=2$ source row



$$
p=2r+6s+3,
 \qquad r\geq1\text{ odd},
 \qquad 3\nmid r.
 \tag{1.1}
$$



Let $q>p$ be in the transverse residue class of Items 416 and 419.
Thus, with $k_*=2r+3$,



$$
q\not\equiv k_*\pmod6,
 \qquad
 Q=Q^\perp={2q-k_*\over3}\in2\mathbb Z+1,
 \qquad
 3Q+k_*=2q.
 \tag{1.2}
$$



Item 419 isolated the missing step: the ordinary upper-$B$ formula
cannot simply be evaluated at odd $Q$, because its matched coefficient
parity changes. This item performs the missing rederivation.

> **PROVED — exact parity-flipped finite tail.** The correct second-sheet
> upper target is
> 

$$
> T^\perp=2q-r-1=3Q+r+2.
> \tag{1.3}
>
$$


> It is even. Consequently the fixed polynomials contribute their even,
> not odd, coefficients, and the correct factorial parameter is
> 

$$
> \boxed{D^\perp={Q+r+2\over2}\in\mathbb Z.}
> \tag{1.4}
>
$$


> Thus the half-integer $(Q+r+1)/2$ in the unrederived ordinary formula
> is not an obstruction to a new tail; it is a warning that the old
> parity was being retained.

> **PROVED — the new tail is resonant with an old connection column.**
> Let $g^\perp=(g_0^\perp,g_1^\perp)$ be the specialized rational
> vector defined in Section 4. If $\Delta=(\Delta_0,\Delta_1)$ is the
> odd homogeneous $A$-chain vector of Item 349, then
> 

$$
> \boxed{\Delta_\nu=\kappa_r^\perp g_\nu^\perp\quad(\nu=0,1)}
> \tag{1.5}
>
$$


> for an explicit nonzero rational scalar $\kappa_r^\perp$. Since
> Item 349 gives $v=\beta_r\Delta$, the actual parity-flipped upper
> tail is, modulo $q$, a $q$-unit multiple of the already retained
> $v$-column.

> **PROVED — scoped target-bridge no-go.** After adjoining this tail,
> the ideal of $2\times2$ connection minors does not change. In
> particular, the new construction contains no source-$s$ target
> information and cannot distinguish the source target from source
> rejection. A new two-parameter identity involving the actual Item-409
> residual $T(r,s)$, or a direct weighted zero-density theorem, is still
> necessary.

The new formula is exact, but it is gate-only. It neither proves
$B_e^\perp(M)=o(M)$ nor improves Item 419's unconditional
$O(M^2/\log M)$ bound. Therefore



$$
\boxed{\Delta r_1=0},
 \qquad
 \boxed{\Delta\mathcal C=0},
 \qquad
 \boxed{\text{ordinary-}j=2\text{ ceiling remains }1/105}.
 \tag{1.6}
$$



No prime census, density extrapolation, Route-1 closure, or conclusion
about (e+\pi) is claimed.

## 2. Why the target parity changes

Put



$$
K_0(z)=(1-z)^r(1+z),
 \qquad
 K_1(z)=(1-z)^r(1+z)^4,
 \tag{2.1}
$$



and write $k_{\nu,j}=[z^j]K_\nu(z)$. The two second-sheet polynomials
are



$$
K_0(z)(1+z^2)^Q,
 \qquad
 K_1(z)(1+z^2)^{Q-1}.
 \tag{2.2}
$$



On the ordinary sheet, $Q$ is even and the corresponding upper target
$3Q+r+2$ is odd. Item 250 therefore used odd $K_\nu$-coefficients.
On (1.2), both $Q$ and $r$ are odd, so (1.3) is even. Only even
$K_\nu$-coefficients can contribute to the logarithmic coefficient.

Set



$$
N={T^\perp\over2}={3Q+r+2\over2}
   =q-{r+1\over2},
 \qquad
 D=N-Q={Q+r+2\over2}.
 \tag{2.3}
$$



Writing $Q=2a+1$ and $r=2h+1$ gives



$$
D=a+h+2.
 \tag{2.4}
$$



Thus the largest even index of $K_0$ has $t=h+1<D$, while the
largest even index of $K_1$ has $t=h+2\leq D$. These are exactly the
nonsingular terminating ranges required below.

This refines rather than reverses Item 419's main conclusion. The old
ordinary $f$-vector still does not transport. The parity-corrected
derivation produces a different vector, and Sections 4–5 identify it as
the old (v)-direction.

## 3. Exact terminating-binomial formula

For an integer $A\geq0$ and $n>A$, differentiation of the binomial
coefficient in its upper parameter gives



$$
[x^n](1+x)^A\log(1+x)
 =(-1)^{n-A-1}{A!(n-A-1)!\over n!}.
 \tag{3.1}
$$



Define the two upper tails



$$
U_\nu^\perp
 =[z^{T^\perp}]
 K_\nu(z)(1+z^2)^{Q-\nu}\log(1+z^2),
 \qquad \nu=0,1.
 \tag{3.2}
$$



Factor out



$$
\mathfrak f^\perp
 =(-1)^{D-1}{Q!(D-1)!\over N!}.
 \tag{3.3}
$$



Equation (3.1), term by term in the even coefficients of $K_\nu$,
gives the exact characteristic-zero identities



$$
\boxed{
 U_0^\perp=\mathfrak f^\perp
 \sum_{t=0}^{h+1}k_{0,2t}(-1)^t
 {(-N)_t\over(1-D)_t},}
 \tag{3.4}
$$





$$
\boxed{
 U_1^\perp=\mathfrak f^\perp\left(-{D\over Q}\right)
 \sum_{t=0}^{h+2}k_{1,2t}(-1)^t
 {(-N)_t\over(-D)_t}.}
 \tag{3.5}
$$



For (3.5), the exponent is $Q-1$, so its own factorial parameter is
$D+1$. Its prefactor divided by (3.3) is exactly $-D/Q$. No
half-integer factorial and no analytic continuation occurs.

## 4. Specialization and the parity-flipped vector

Modulo the transverse prime (q), (1.2) gives



$$
\bar Q=-{2r+3\over3},
 \qquad
 \bar N=-{r+1\over2},
 \qquad
 \bar D={r+3\over6},
 \qquad
 \rho^\perp=-{\bar D\over\bar Q}
 ={r+3\over2(2r+3)}.
 \tag{4.1}
$$



Define the fixed-(r) rational vector



$$
\boxed{
 g_0^\perp=
 \sum_{t=0}^{h+1}k_{0,2t}(-1)^t
 {(-\bar N)_t\over(1-\bar D)_t},}
 \tag{4.2}
$$





$$
\boxed{
 g_1^\perp=
 \rho^\perp
 \sum_{t=0}^{h+2}k_{1,2t}(-1)^t
 {(-\bar N)_t\over(-\bar D)_t}.}
 \tag{4.3}
$$



Then (3.4)–(3.5) reduce to



$$
(U_0^\perp,U_1^\perp)
 \equiv\mathfrak f^\perp(g_0^\perp,g_1^\perp)
 \pmod q.
 \tag{4.4}
$$



### 4.1 Unit audit

Here $q>p>2r+3$. Moreover



$$
0<Q<N=q-{r+1\over2}<q,
 \qquad 0<D<N<q.
 \tag{4.5}
$$



Hence all factorials in (3.3) are $q$-units. The range inequalities
after (2.4) keep (3.4) before the zero of $(1-D)_t$ and (3.5) before
the zero of $(-D)_t$.

After specialization, each possible denominator is a product of (2),
(3), and nonzero integers of absolute value less than (q). A zero
could occur only in the excluded class $3\mid r$. Therefore every
denominator in (4.1)–(4.3) is a $q$-unit, and substituting
$Q\equiv\bar Q\pmod q$ in the actual finite sums is legitimate.

## 5. Exact reciprocal closure into (v)

Use the homogeneous odd chain already present in Items 349 and 409:



$$
\eta_{2t}=0,
 \qquad \eta_1=1,
 \qquad
 \eta_{k+2}=-{\bar Q+k\over3\bar Q+k}\eta_k
 \quad(k\text{ odd}).
 \tag{5.1}
$$



Equivalently,



$$
\eta_{2t+1}
 =(-1)^t{(-r/3)_t\over(-(r+1))_t}.
 \tag{5.2}
$$



Its two connection coordinates are



$$
\Delta_0=\sum_{t=0}^{h+1}k_{0,2t}
             (\eta_{2t+1}+\eta_{2t+3}),
 \qquad
 \Delta_1=\sum_{t=0}^{h+2}k_{1,2t+1}\eta_{2t+1}.
 \tag{5.3}
$$



Put



$$
\boxed{
 \kappa_r^\perp=-{\eta_{2h+5}\over\rho^\perp}\neq0.}
 \tag{5.4}
$$



The anti-reciprocal identities



$$
z^{r+1}K_0(1/z)=-K_0(z),
 \qquad
 z^{r+4}K_1(1/z)=-K_1(z)
 \tag{5.5}
$$



give



$$
k_{0,2(h+1-t)}=-k_{0,2t},
 \qquad
 k_{1,2(h+2-t)+1}=-k_{1,2t}.
 \tag{5.6}
$$



Apply



$$
(x)_{n-t}=(x)_n{(-1)^t\over(1-x-n)_t}
 \tag{5.7}
$$



to (5.2), and substitute (4.1). Term by term, one obtains



$$
\begin{aligned}
 &k_{0,2(h+1-t)}
  (\eta_{2(h+1-t)+1}+\eta_{2(h+1-t)+3})\\
 &\qquad=\kappa_r^\perp k_{0,2t}(-1)^t
 {(-\bar N)_t\over(1-\bar D)_t},
 \qquad 0\leq t\leq h+1,
 \tag{5.8}
\end{aligned}
$$



and



$$
\begin{aligned}
 &k_{1,2(h+2-t)+1}\eta_{2(h+2-t)+1}\\
 &\qquad=\kappa_r^\perp\rho^\perp k_{1,2t}(-1)^t
 {(-\bar N)_t\over(-\bar D)_t},
 \qquad 0\leq t\leq h+2.
 \tag{5.9}
\end{aligned}
$$



Summing proves (1.5).

Item 349's exact normalization is



$$
v=\beta_r\Delta,
 \qquad
 \beta_r=-{3(r+1)!\over
 2(2r+3)(-r/3)_{r+1}}.
 \tag{5.10}
$$



All factors in $\beta_r$ and $\kappa_r^\perp$ are $q$-units:
their linear factors are nonzero and have absolute value below $q$,
using $3\nmid r$ and $q>2r+3$. Combining (4.4), (1.5), and (5.10)
gives the exact second-sheet congruence



$$
\boxed{
 (U_0^\perp,U_1^\perp)
 \equiv
 {\mathfrak f^\perp\over\beta_r\kappa_r^\perp}\,v
 \pmod q,}
 \tag{5.11}
$$



where the displayed scalar is a $q$-unit.

Thus the rederived object is not the ordinary $f$-vector, but neither
is it transverse to the old connection module. It is exactly the old
$v$-direction.

## 6. Why this cannot bridge the source target

Let $u_q=\mathfrak f^\perp/(\beta_r\kappa_r^\perp)$. From (5.11),



$$
\det(f,U^\perp)=u_q\det(f,v),
 \qquad
 \det(b,U^\perp)=u_q\det(b,v),
 \qquad
 \det(v,U^\perp)=0.
 \tag{6.1}
$$



Since $u_q$ is a unit, adjoining $U^\perp$ leaves the connection
minor ideal unchanged:



$$
\boxed{I_2(f,b,v,U^\perp)=I_2(f,b,v)\quad\text{over }\mathbf F_q.}
 \tag{6.2}
$$



For an actual transverse factor of the saturated foreign carrier,
$q\mid\mathcal J_{r,s}$ ensures that all old connection denominators
are units and that the old triple-minor gate already vanishes. Equation
(6.2) therefore contributes no additional condition at that factor.

The source target is different data. Item 409's exact rational
coordinates $T_0(r,s),T_1(r,s)$ contain $B_s$, the source Cartier
term, $\tau_{r,s}$, and $4^s$. Its simpler incomplete-period
replacement is certified only in the tied characteristic $p$; it may
not be transported to a foreign $q$ by comparing integer supports.
The vector (5.11) contains none of these source-$s$ quantities.

This insufficiency is also exact at the abstract linear-algebra level.
Fix rank-one columns



$$
f=(1,2),\qquad b=(3,6),\qquad v=(5,10),
 \qquad g^\perp=(35,70).
 \tag{6.3}
$$



All their minors vanish. Nevertheless the affine residual



$$
fZ+9b-11v
 \tag{6.4}
$$



is ((0,0)) at (Z=28) and ((1,2)) at (Z=29). This packet is
**ABSTRACT AND NOT AN ACTUAL ROW**. It proves only that the named column
information cannot distinguish target from rejection. An actual
formula-specific relation involving the missing source target could
escape this model.

Consequently the natural parity-flipped derivation has been fully
settled and is gate-only. This does not rule out a new cross-parameter
reciprocity law, a second period containing (s), or a direct average
gcd theorem.

## 7. Capacity screen

The actual Closer target remains



$$
\boxed{
 B_e^\perp(M)=
 \sum_{\substack{\text{actual fixed-}M\ e\text{-ray rows}\\
 q>p,\ q\not\equiv2r+3\ (6)}}
 \log\operatorname{rad}_q\mathcal J_{r,s}
 =o(M).}
 \tag{7.1}
$$



Equation (6.2) supplies neither an upper bound for (7.1) nor a positive
lower bound for the adaptive tail. The best unconditional estimate is
still Item 419's



$$
B_e^\perp(M)=O\!\left({M^2\over\log M}\right),
 \tag{7.2}
$$



whose quotient by $M$ diverges. It is not a finite linear capacity
coefficient. Even a future proof of (7.1) would still need the aligned
tail and a positive adaptive-tail lower bound before producing a booked
margin.

Therefore the parity-flipped common period fails the admission test for
a new Builder mechanism: it produces no new codimension, no target
bridge, and no positive linear mass. Its value is as a rigorous closure
of the most natural continuation proposed by Item 419.

## 8. Deterministic replay and strict labels

The certificate pins canonical Items 250, 318, 349, 409, and 416, plus
the completed Item-419 work package. It verifies:

1. 7,001 termwise rational identities on all 67 admissible odd
   $r\leq199$;
2. direct finite-logarithm coefficients against (3.4)–(3.5) on five
   declared second-sheet geometry rows;
3. specialization to (4.2)–(4.3);
4. the (q)-unit proportionality (5.11); and
5. the exact abstract target-status countermodel.

Replay from the archive root:

~~~powershell
python scripts/item422_parity_flipped_b_tail_certificate.py `
  --replay results/item422_parity_flipped_b_tail_certificate.json `
  --output results/item422_parity_flipped_b_tail_certificate_replay.json
~~~

### Strict labels

- **PROVED:** (1.4), the exact finite-tail formulas (3.4)–(3.5), the
  all-(r) reciprocal identity (1.5), the old-(v) closure (5.11), the
  ideal equality (6.2), the scoped target-bridge no-go, and zero booking.
- **EXACT GEOMETRY/FORMULA REPLAY ONLY:** the five declared
  $(p,r,s,q)$ rows. No declared $q$ is asserted to divide an actual
  carrier.
- **ABSTRACT LINEAR-ALGEBRA COUNTERMODEL / NOT ACTUAL:** (6.3)–(6.4).
- **OPEN:** any source-target reciprocity involving the odd sheet,
  $B_e^\perp(M)=o(M)$, every positive tail-minus-foreign margin,
  Route 1, and every conclusion about $e+\pi$.

Accordingly Item 422 completes the natural parity-flipped upper-(B)
calculation. It repairs the normalization but proves that the resulting
period is not a new direction and cannot, by itself, transport the
source target or rejection.
