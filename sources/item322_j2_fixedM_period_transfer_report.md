> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 322 - fixed-$M$ transfer of the actual ordinary-$j=2$ period

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Retain the actual ordinary-$j=2$ rows



$$
p=2r+6s+3,\qquad r=2h+1,\qquad 3\nmid r,\qquad s\geq1,
 \tag{1.1}
$$



and Item 318's actual transverse residual



$$
\mathcal E_{r,s}=\ell_rZ_{r,s}+11C_r,
 \qquad
 Z_{r,s}=B_s\left(\frac{9\kappa_r}{2}A_s-\tau_{r,s}\right).
 \tag{1.2}
$$



Item 319 proves that eliminating $Z$ from the exterior-minor tower leaves
only the old coefficient determinant.  The present item takes the opposite
course: it keeps $Z$ and determines its exact transfer on the master
fixed-$M$ slices



$$
2M=5r+14s+7.                 \tag{1.3}
$$



> **PROVED - a triangular period-retaining system.**  Put
> 

$$
> e_s=\frac{B_sA_s}{2},\qquad
> \mathfrak f_{r,s}=(-1)^{s+h}
>       \frac{(2s)!(s+h)!}{(3s+h+1)!},\qquad u_s=4^s.
> \tag{1.4}
>
$$


> Then $(Z_{r,s},\mathfrak f_{r,s},u_s)$ satisfies an exact rational
> first-order triangular system in $s$.  No fitted recurrence or finite
> interpolation is used.

> **PROVED - exact adjacent-row transfer on every fixed-$M$ slice.**  The
> primitive step preserving (1.3) and the ray $r\bmod6$ is
> 

$$
> (r,s,p)\longmapsto(r-42,s+15,p+6).                 \tag{1.5}
>
$$


> For $r\ge43$, the corresponding fifteen-step transfer is an explicit
> upper-triangular $3$-by-$3$ matrix.  Its determinant is nonzero over
> $\mathbf Q$, and its three diagonal entries are units modulo both
> adjacent candidate primes whenever those candidates are prime.

> **PROVED - division-free transfer of the actual exterior residual.**  The
> same calculation gives an exact relation between
> $\mathcal E_{r,s}$ and $\mathcal E_{r-42,s+15}$ without dividing by
> $\ell_r$ or $\ell_{r-42}$.  Thus every zero chart remains present.

> **PROVED - fixed-$M$ Frobenius/conic normal form.**  On the
> $\ell_r\ne0\pmod p$ chart, $\mathcal E_{r,s}$ is a unit multiple of
> one affine half-binomial collision
> 

$$
>                         H_{s-1}=\Theta_{r,s}.          \tag{1.6}
>
$$


> If $q=(p-1)/2-(s-1)$, then
> 

$$
> q=r+2s+2=2(M-p)+1
> \tag{1.7}
>
$$


> and $H_{s-1}$ is exactly one rationally weighted quadratic-character
> moment on the fixed conic $y^2=x(1-x/2)$.

> **PROVED - scoped bounded-degree no-go.**  Although the character factor
> is quadratic, its rational weight contains $x^q/(1-x)$, with
> 

$$
>                         \frac p3<q\le\frac{p-1}{2}.     \tag{1.8}
>
$$


> Any pointwise rational representation of that weight on
> $\mathbf F_p^*\setminus\{1\}$ has degree at least
> $(p-3)/4$.  Hence the fixed conic does **not** turn the actual period
> into a bounded-degree rational-weight trace.

> **PROVED - adjacent-prime transfer has zero capacity.**  Interpreting one
> transfer step as a relation between two collision rows requires both
> $p$ and $p+6$ prime.  The fixed two-tuple upper-bound sieve gives
> $O(M/\log M)=o(M)$ total logarithmic mass for all such pairs.  This
> transfer submechanism cannot control isolated collision primes.

The transfer is invertible rather than contracting.  Moreover, its reduction
modulo $p$ controls the next rational state modulo $p$, whereas the next
collision is tested modulo $p+6$.  Therefore the recurrence alone supplies
no fixed-$M$ gcd or weighted zero theorem.  The strict ledger effect is



$$
\boxed{\text{new capacity reduction}=0},\qquad
 \boxed{\text{new booking}=0},\qquad
 \boxed{\text{ordinary-}j=2\text{ ceiling}=1/105\text{ per }6M}.
 \tag{1.9}
$$



## 2. Admission and overlap audit

This item begins strictly after the Item-314 determinant gate.  On a
rank-two chart an original collision forces



$$
D_{r,s}=0,\qquad \mathcal E_{r,s}=0. \tag{2.1}
$$



The second condition is internal to the already retained $1/105$ ceiling;
it cannot be added as separate capacity.  Item 319 also proves that removing
the actual period from (2.1) yields no second coefficient-only divisor.
Accordingly, the only admissible uses of the present theorem are:

1. a weighted upper bound for primes satisfying both conditions;
2. an exact arithmetic propagation theorem for the period state; or
3. a scoped closure of a proposed period-removal mechanism.

The first two remain open.  Sections 7-9 prove the third for bounded-degree
pointwise rational compression and explain why the exact transfer itself
does not propagate modular zeros.

## 3. The one-step incomplete-beta system

Item 251 gives



$$
A_{s+1}+A_s
 =4^s\frac{28s+11}{2s+1}\binom{3s-1}{s-1}.       \tag{3.1}
$$



Using



$$
B_s=\frac{(2s-1)!(s-1)!}{(3s-1)!},
$$



direct factorial cancellation in (3.1) yields



$$
\boxed{e_{s+1}=-\rho_se_s+\eta_s4^s},             \tag{3.2}
$$



where



$$
\rho_s=\frac{2s(2s+1)}{3(3s+1)(3s+2)},\qquad
 \eta_s=\frac{28s+11}{6(3s+1)(3s+2)}.             \tag{3.3}
$$



This is a first-order **inhomogeneous** recurrence.  The endpoint $4^s$
is essential; dropping it would replace the actual incomplete beta value by
a homogeneous product mode.

The second summand in $Z$ is hypergeometric:



$$
\boxed{
 \frac{\mathfrak f_{r,s+1}}{\mathfrak f_{r,s}}
 =q_{r,s}:=-\frac{(2s+1)(2s+2)(s+h+1)}
 {(3s+h+2)(3s+h+3)(3s+h+4)}.}                     \tag{3.4}
$$



Since $Z_{r,s}=9\kappa_re_s-\mathfrak f_{r,s}$, equations
(3.2)-(3.4) give



$$
\boxed{
 Z_{r,s+1}
 =-\rho_sZ_{r,s}-(\rho_s+q_{r,s})\mathfrak f_{r,s}
   +9\kappa_r\eta_s4^s.}                           \tag{3.5}
$$



Together with



$$
\mathfrak f_{r,s+1}=q_{r,s}\mathfrak f_{r,s},
 \qquad4^{s+1}=4\cdot4^s,                          \tag{3.6}
$$



this is the promised exact triangular system.  It retains the actual
incomplete-beta coordinate and its Frobenius endpoint.

## 4. The exact fifteen-step fixed-$M$ transfer

Solving (1.1) and (1.3) also gives



$$
p=\frac{6M-r}{7},\qquad
 s=\frac{5p-4M-1}{2}.                              \tag{4.1}
$$



Thus adjacent candidates on one fixed ray differ as in (1.5).  Define



$$
a_s^{(15)}=\prod_{j=0}^{14}(-\rho_{s+j}),          \tag{4.2}
$$



and



$$
b_s^{(15)}=
 \sum_{j=0}^{14}\eta_{s+j}4^j
          \prod_{k=j+1}^{14}(-\rho_{s+k}).          \tag{4.3}
$$



Iterating (3.2) gives the exact identity



$$
e_{s+15}=a_s^{(15)}e_s+b_s^{(15)}4^s.              \tag{4.4}
$$



Put



$$
K_r=\frac{\kappa_{r-42}}{\kappa_r},\qquad
 \Lambda_{r,s}=K_ra_s^{(15)},                       \tag{4.5}
$$



and, with $h=(r-1)/2$,



$$
F_{r,s}=\frac{(2s+1)_{30}}
 {(s+h-5)_6(3s+h+2)_{24}}.                          \tag{4.6}
$$



The sign in (4.6) is positive because
$(s+15)+(h-21)-(s+h)=-6$.  Direct factorial cancellation proves



$$
\mathfrak f_{r-42,s+15}=F_{r,s}\mathfrak f_{r,s}. \tag{4.7}
$$



Substituting (4.4) and (4.7) into the definition of $Z$ gives



$$
\boxed{
\begin{pmatrix}
 Z_{r-42,s+15}\\
 \mathfrak f_{r-42,s+15}\\
 4^{s+15}
\end{pmatrix}
=
\begin{pmatrix}
 \Lambda_{r,s}&\Lambda_{r,s}-F_{r,s}
    &9\kappa_{r-42}b_s^{(15)}\\
 0&F_{r,s}&0\\
 0&0&4^{15}
\end{pmatrix}
\begin{pmatrix}
 Z_{r,s}\\
 \mathfrak f_{r,s}\\
 4^s
\end{pmatrix}.}                                    \tag{4.8}
$$



This is an all-parameter identity over $\mathbf Q$.  It is not a
recurrence guessed from a table.

## 5. Division-free transfer of the exterior residual

Write



$$
\ell=\ell_r,\quad C=C_r,\quad
 \ell'=\ell_{r-42},\quad C'=C_{r-42},\quad
 \mathcal E=\ell Z+11C,\quad
 \mathcal E'=\ell'Z'+11C'.                         \tag{5.1}
$$



Multiplying (4.8) by $\ell\ell'$ and using (5.1) gives



$$
\boxed{
\begin{aligned}
 \ell\mathcal E'={}&
 \ell'\Lambda_{r,s}\mathcal E
 +\ell\ell'(\Lambda_{r,s}-F_{r,s})\mathfrak f_{r,s}\\
 &+9\ell\ell'\kappa_{r-42}b_s^{(15)}4^s
 +11\ell C'-11\ell'\Lambda_{r,s}C.
\end{aligned}}                                      \tag{5.2}
$$



No division by either connection minor occurs.  Formula (5.2) is therefore
valid on the $\ell=0$ and $\ell'=0$ residue charts as an exact rational
identity before reduction.  Dividing it by a connection minor modulo $p$
would be unsafe and is not part of the theorem.

## 6. Unit and invertibility audit

Assume $r\ge43$.  The source prime satisfies



$$
p=2r+6s+3\ge6s+89.          \tag{6.1}
$$



Every numerator and denominator factor in the product (4.2) is positive
and smaller than $p$.  In particular, the largest denominator factor is
$3s+44<p$, while the largest numerator factor is $2s+29<p$.
Hence $a_s^{(15)}$ is a $p$-unit.

For completeness, Item 250's exact formula is



$$
\kappa_r=\frac{2(4h+5)}{9(4h+3)}(-1)^h
 \frac{((5-2h)/6)_h}{(h+3/2)_h}.                   \tag{6.2}
$$



After clearing the powers of $2,3$, the numerator factors of the first
Pochhammer string are $5-2h+6j$, $0\le j<h$.  They are odd and hence
nonzero; their absolute values are at most $4h-1=2r-3$.  The other
Pochhammer string has positive raw factors at most $4h+1=2r-1$, and the
two explicit linear factors are $4h+5=2r+3$ and $4h+3=2r+1$.
All are strictly below $p$.  Replacing $h$ by $h-21$ only decreases
these bounds, so both $\kappa_r$ and $\kappa_{r-42}$, and hence $K_r$,
are units modulo $p$ and $p+6$.

For (4.6), the largest numerator factor is $2s+30$, and the largest
denominator factor is $3s+h+25$.  Since



$$
p-(3s+h+25)=3s+3h-20>0,                            \tag{6.3}
$$



all of them are units.  The same inequalities remain true modulo the next
candidate $p+6$.  Therefore



$$
\det T_{r,s}=\Lambda_{r,s}F_{r,s}4^{15}             \tag{6.4}
$$



is a unit modulo either adjacent prime whenever that integer is prime.

The off-diagonal coefficient $b_s^{(15)}$ can vanish; invertibility does
not require it.  Factors $28(s+j)+11$ can also meet a candidate prime in
the numerator of $\eta_{s+j}$; they are never inverted.

This audit gives a first scoped no-go.  The fixed-$M$ transfer has no
singular layer that projects away the period.  It preserves all three state
coordinates.  A transfer-only argument therefore still needs one actual
initial-period condition.

There is a second, arithmetic obstruction.  Reducing (4.8) modulo $p$
relates both rational states **modulo $p$**.  The adjacent collision is
instead tested modulo $p+6$.  No implication



$$
\mathcal E_{r,s}=0\pmod p
 \quad\Longrightarrow\quad
 \mathcal E_{r-42,s+15}=0\pmod{p+6}                 \tag{6.5}
$$



follows from (4.8) or (5.2).  This is a moving-modulus barrier, not a claim
that every possible arithmetic use of the recurrence is impossible.

### 6.1 Capacity of adjacent-prime propagation

There is a separate capacity reason not to promote this transfer into a
main Closer mechanism.  A collision-to-collision use of one adjacent step
requires both $p$ and $p+6$ to be prime.  The classical Brun/Selberg
upper-bound sieve for the fixed two-tuple $\{0,6\}$ gives, uniformly for
an interval of length $O(M)$,



$$
\#\{p\ll M:p,\ p+6\text{ prime}\}
 =O\!\left(\frac{M}{(\log M)^2}\right).             \tag{6.6}
$$



Consequently its total logarithmic mass is



$$
\sum_{\substack{p\ll M\\p,\ p+6\ {\rm prime}}}\log p
 =O\!\left(\frac{M}{\log M}\right)=o(M).            \tag{6.7}
$$



Thus simultaneous adjacent-prime rows already form a zero-rate
submechanism.  Even a perfect propagation theorem on every such pair could
not reduce the mass of isolated collision primes.  The single-row conic
condition in Sections 7-9 is logically separate and remains the live
positive-capacity target.

## 7. Affine Frobenius normal form on the nondegenerate chart

Put



$$
m=s-1,\qquad d=r+2,\qquad
 h_j=\frac{(1/2)_j}{j!2^j},\qquad H_m=\sum_{j=0}^mh_j, \tag{7.1}
$$



and



$$
P_d(m)=\sum_{k=1}^d2^{-k}\frac{(m+1/2)_k}{(1/2)_k}. \tag{7.2}
$$



Item 252 proves, with $\epsilon=(2/p)$,



$$
A_s=(-1)^m\{\epsilon[H_m-h_mP_d(m)]-1\}\pmod p.  \tag{7.3}
$$



On the chart $\ell_r\ne0\pmod p$, define



$$
\boxed{
 \Theta_{r,s}=h_mP_{r+2}(m)+\epsilon\left[
 1+(-1)^m\frac{2}{9\kappa_r}
 \left(\tau_{r,s}-\frac{11C_r}{\ell_rB_s}\right)
 \right].}                                          \tag{7.4}
$$



Every division in (7.4) is by a certified unit on this chart.  Substitution
of (7.3) into (1.2) gives the exact finite-field identity



$$
\boxed{
 \mathcal E_{r,s}
 =\ell_rB_s\frac{9\kappa_r}{2}(-1)^m\epsilon
       (H_m-\Theta_{r,s})\pmod p.}                  \tag{7.5}
$$



The displayed multiplier is a unit.  Hence, after imposing $D=0$, Item
318's rank-two chart equivalence becomes



$$
\boxed{\text{original collision}\quad\Longleftrightarrow\quad
 H_m=\Theta_{r,s}\pmod p}                          \tag{7.6}
$$



on $\ell_r\ne0$.  This is genuinely period-retaining: it identifies the
single incomplete period that still has to hit the connection-plane target.

When $\ell_r=0\pmod p$, formula (7.4) is not used.  One keeps the
division-free residual (1.2), the $m_r\ne0$ chart of Item 318 when
available, or an individual coordinate on the rank-at-most-one chart.
The bounded replay finds such an $\ell$-zero row; it is retained rather
than silently discarded.

## 8. The fixed-$M$ conic moment

Let



$$
n=\frac{p-1}{2}=r+3s+1,\qquad q=n-m=r+2s+2.        \tag{8.1}
$$



Equations (1.3) and (1.1) give (1.7).  On $\mathbf F_p^*$,



$$
x^{-m}=x^{n-m}x^n=x^q\chi(x),                    \tag{8.2}
$$



where $\chi$ is the quadratic character.  Substitution in Item 254's
exact Mellin/Jacobi decomposition yields



$$
\boxed{
 H_m=\epsilon(q+1)-
 \sum_{x\in\mathbf F_p\setminus\{0,1\}}
 \frac{x^q\chi(x(1-x/2))}{1-x}\pmod p.}           \tag{8.3}
$$



The explicit Jacobi term is $\epsilon(q+1)$; it is not omitted.  The
character factor belongs to the fixed rational conic



$$
y^2=x(1-x/2).               \tag{8.4}
$$



Nevertheless, the rational moment is not fixed.  Directly from (8.1),



$$
3q-p=r+3>0,\qquad p-1-2q=2s-2\ge0,                \tag{8.5}
$$



which proves (1.8).  Thus the polynomial weight has degree linear in the
prime on every actual row, including the fixed-$M$ family.

Combining (7.6) and (8.3), the actual collision on the nondegenerate chart
is exactly the conic-moment collision



$$
\sum_{x\ne0,1}\frac{x^q\chi(x(1-x/2))}{1-x}
 =\epsilon(q+1)-\Theta_{r,s}\pmod p.               \tag{8.6}
$$



This is the smallest period-retaining finite-field target supplied by this
item.

## 9. Linear degree is unavoidable for pointwise rational compression

The following elementary lemma quantifies the remaining weight.

Let $A,B\in\mathbf F_p[x]$ be arbitrary coprime polynomials,
$B\ne0$, and suppose



$$
\frac{A(x)}{B(x)}=x^q      \tag{9.1}
$$



at every $x\in\mathbf F_p^*$ where $B(x)\ne0$.  The coefficient field
is the full field $\mathbf F_p$; no bounded coefficient set or lift is
assumed.  The rational function is reduced, and its degree means
$D=\max(\deg A,\deg B)$.  The polynomial



$$
A(x)-x^qB(x)               \tag{9.2}
$$



has at least $p-1-D$ roots and degree at most $q+D$.  If
$D<q$ and $2D<p-1-q$, it must vanish identically.  But then
$\deg A=q+\deg B\ge q>D$, a contradiction.  Therefore



$$
\boxed{D\ge\min\left(q,\left\lceil\frac{p-1-q}{2}\right\rceil\right)
 \ge\frac{p-1}{4}.}                                \tag{9.3}
$$



The same root count applied directly to
$A/B=x^q/(1-x)$ on $\mathbf F_p^*\setminus\{1\}$ gives



$$
\boxed{D\ge\min\left(q,\left\lceil\frac{p-2-q}{2}\right\rceil\right)
 \ge\frac{p-3}{4}.}                                \tag{9.4}
$$



Indeed, use $A(1-x)-Bx^q$, which has at least $p-2-D$ roots.  If
it vanishes identically, coprimality of $x^q$ and $1-x$ forces
$\deg A\ge q$.

Equations (9.3)-(9.4) prove a rigorously scoped no-go:



$$
\boxed{\text{the moving conic moment cannot be rewritten pointwise
 by rational weights of uniformly bounded degree}.}              \tag{9.5}
$$



This does **not** rule out a summation identity special to the particular
polynomial $C_p$, cancellation after adjoining another period, a
higher-rank $F$-crystal, or a weighted zero-density theorem.  It also does
not turn the absence of a bounded-degree rewrite into evidence that the
zero set has positive density.

## 10. Capacity and strategic conclusion

The exact transfer and conic form sharpen the branch, but both outcomes are
structurally neutral for the ledger:

* the transfer is invertible and compares different collision moduli;
* rows where both adjacent moduli are prime already have $o(M)$
  logarithmic mass by the fixed two-tuple upper-bound sieve;
* the conic has fixed genus, but its rational weight has degree
  $\Omega(p)$;
* individual numerator height or P-recursiveness still sums to a bound much
  larger than the retained $O(M)$ raw ceiling; and
* no theorem bounds the weighted prime support of (8.6).

Accordingly, no part of the $1/105$ ceiling is removed.  A successful
continuation must use arithmetic that couples the actual period to the
changing prime, for example a summation-specific Frobenius module or a
sequence-specific average gcd theorem.  More transfer iteration alone is
not strategic progress.

## 11. Deterministic replay

The standard-library checker verifies the exact one-step identities on 150
declared rational rows and the fifteen-step fixed-$M$ identities on 80
declared rows.  It also verifies (7.5) and (8.3) on 330 nondegenerate actual
rows through $p\le199$.  One $\ell$-zero row is recorded separately.

The row-stream digests are stored in the certificate JSON.  These row
counts, samples, and digests are **EXACT FINITE ONLY**.  The all-parameter
proofs are the factorial cancellations, iteration, finite-field identities,
and root counts in Sections 3-9.

## 12. Strict labels

**PROVED**

* the exact one-step triangular period system (3.2)-(3.6);
* the exact fifteen-step fixed-$M$ transfer (4.8);
* the division-free exterior-residual transfer (5.2);
* the all-row unit and invertibility audit for $r\ge43$;
* the zero-rate capacity theorem for adjacent-prime transfer pairs;
* the affine half-binomial chart identity (7.5);
* the fixed-$M$ conic moment (8.3);
* both linear rational-degree barriers (9.3)-(9.4); and
* zero capacity booking.

**EXACT FINITE ONLY / DIAGNOSTIC**

* all bounded replay counts, samples, zero-chart rows, and digests in the
  certificate.

**OPEN**

* a fixed-$M$ weighted zero-density theorem for (8.6);
* a summation-specific bounded-rank Frobenius compression;
* arithmetic propagation across the changing prime moduli;
* control of every degenerate connection chart by a non-exterior coordinate;
* any reduction of the ordinary-$j=2$ ceiling; and
* any new Route-1 booking or conclusion about $e+\pi$.

