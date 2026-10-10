> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 416 — adaptive selected-prime saturation and the forward foreign-tail boundary for ordinary $j=2$

Checked: 2026-09-01 (Beijing time)

Status: **CANONICAL, ROOT-AUDITED, ZERO BOOKING**

## 1. Capacity first and verdict

Retain one actual ordinary-$j=2$ ray



$$
p=2r+6s+3,\qquad
 r=6M-7p,\qquad
 s={5p-4M-1\over2},\qquad
 r\equiv e\pmod6,\quad e\in\{1,5\}.
\tag{1.1}
$$



Its raw Chebyshev mass is



$$
R_e(M)={1\over35}M+o(M),
\tag{1.2}
$$



so one ray has normalized capacity $1/210$, and the two rays retain the
ordinary-$j=2$ ceiling $1/105$.

Items 407, 409, and 413 give the actual rejection carrier



$$
\mathcal J_{r,s}
 =\bigl(\Pi^{\rm sat}_{r,s}\bigr)_{
       (\Gamma^{\rm sat}_{r,s})},
 \qquad
 j^{\rm tie}_{r,s}
 =\gcd(p,\mathcal J_{r,s})\in\{1,p\}.
\tag{1.3}
$$



Item 413 retained the radical tail above $2r+3$, then paid for every
factor unequal to $p$ as foreign.  The cutoff can in fact be moved
safely to $p$, or to any larger row-dependent level.

For an integer $Y_{r,s}\ge p$, put



$$
C_{p,Y}
 =\prod_{\substack{\ell\le Y\\
                    \ell\ {\rm prime},\ \ell\ne p}}\ell,
 \qquad
 \mathcal J^{[Y]}_{r,s}
 =(\mathcal J_{r,s})_{(C_{p,Y})},
\tag{1.4}
$$





$$
L^{[Y]}_{r,s}
 =\operatorname {rad}\mathcal J^{[Y]}_{r,s},
 \qquad
 F^{[Y]}_{r,s}
 =(L^{[Y]}_{r,s})_{(p)}.
\tag{1.5}
$$



Here $A_{(B)}$ is the largest divisor of $A$ coprime to $B$.

> **PROVED — adaptive selected-prime cutoff.** On every actual row,
>
> 

$$
> \boxed{
> \operatorname {supp}L^{[Y]}_{r,s}
> \subseteq\{p\}\cup\{q:q>Y\},
> \qquad
> L^{[Y]}_{r,s}
> =j^{\rm tie}_{r,s}F^{[Y]}_{r,s}.}
> \tag{1.6}
>
$$


>
> If $Y_2\ge Y_1\ge p$, the radical removed in passing from $Y_1$
> to $Y_2$ is purely foreign and divides both the old tail and the old
> foreign tail by exactly the same factor.

Consequently, with



$$
A^{[Y]}_e(M)=\sum\log L^{[Y]}_{r,s},
 \qquad
 B^{[Y]}_e(M)=\sum\log F^{[Y]}_{r,s},
\tag{1.7}
$$



one has



$$
\boxed{
 A^{[Y]}_e(M)-B^{[Y]}_e(M)
 =J_e(M)=D_e(M)-G_e(M)}
\tag{1.8}
$$



for every allowed cutoff.  Taking $Y=p$ removes every foreign prime



$$
2r+3<q<p
\tag{1.9}
$$



from both sides of Item 413's decomposition at zero matched-margin cost.

> **PROVED — forward transport of aligned foreign support.** Let
> $q>p$ be a prime factor of $F^{[p]}_{r,s}$. If
>
> 

$$
> q\equiv2r+3\pmod6,
> \tag{1.10}
>
$$


>
> then
>
> 

$$
> t={q-2r-3\over6}\ge1,\qquad
> M_q={r+7q\over6},\qquad
> M_q-M={7(q-p)\over6}>0.
> \tag{1.11}
>
$$


>
> The same $q$ is the tied characteristic of the unique future actual
> row $(q,r,t,M_q)$, and $q\mid\Pi_r$ makes it a degenerate gate row.

This transport does not determine the future target status.  The source
condition $q\nmid\Gamma_{r,s}$ gives no proved statement about
$\Gamma_{r,t}$, and Item 409's incomplete-period replacement is a
tied-$p$ congruence rather than an equality of foreign-prime carriers.
Foreign $q$ in the other residue class has no same-$r$ ordinary row.

The inherited height yields only



$$
\boxed{B^{[p]}_e(M)=O(M^2),}
 \qquad
 \boxed{\sum\omega(F^{[p]}_{r,s})
        =O(M^2/\log M).}
\tag{1.12}
$$



Both bounds are superlinear.  No $B^{[p]}_e=o(M)$, positive tail lower
bound, or matched positive margin is proved.  Therefore



$$
\boxed{\Delta r_1=0},\qquad
 \boxed{\Delta\mathcal C=0},\qquad
 \boxed{\text{ordinary-}j=2\text{ ceiling remains }1/105}.
\tag{1.13}
$$



There is no prime census and no finite extrapolation.

## 2. Proof of the adaptive cutoff theorem

For a positive integer $J$, write



$$
\mathcal P(J)=\{q:q\text{ prime},\ q\mid J\}.
\tag{2.1}
$$



Because $C_{p,Y}$ contains every prime at most $Y$ except $p$,



$$
\mathcal P(\mathcal J^{[Y]})
 =\mathcal P(\mathcal J)\cap
   \bigl(\{p\}\cup\{q:q>Y\}\bigr).
\tag{2.2}
$$



Moreover $p\nmid C_{p,Y}$, so



$$
\gcd(p,\mathcal J^{[Y]})
 =\gcd(p,\mathcal J)
 =j^{\rm tie}.
\tag{2.3}
$$



Taking radicals proves (1.6).  For $Y_2\ge Y_1\ge p$, define



$$
C(Y_1,Y_2)
 =\prod_{\substack{q\mid\mathcal J\\
                    Y_1<q\le Y_2\\q\ne p}}q.
\tag{2.4}
$$



Then exactly



$$
L^{[Y_1]}=C(Y_1,Y_2)L^{[Y_2]},
 \qquad
 F^{[Y_1]}=C(Y_1,Y_2)F^{[Y_2]}.
\tag{2.5}
$$



Subtracting logarithms proves cutoff invariance row by row and hence
(1.8) after summation.

Increasing $Y$ may make a foreign upper bound easier, but it makes the
tail lower bound harder by exactly the same removed mass.  Cutoff
selection alone therefore cannot manufacture a positive exponent.

## 3. The selected-prime cutoff

Denote Item 413's $2r+3$ tail and foreign tail by $L^{[0]},F^{[0]}$.
At the selected-prime cutoff define



$$
C^{\rm mid}_{r,s}
 =\operatorname {rad}_{\,2r+3<q<p}\mathcal J_{r,s}.
\tag{3.1}
$$



Every factor of $C^{\rm mid}$ is foreign, and (2.5) gives



$$
\boxed{
 L^{[0]}=C^{\rm mid}L^{[p]},
 \qquad
 F^{[0]}=C^{\rm mid}F^{[p]}.}
\tag{3.2}
$$



Thus the smallest useful foreign-tail target is



$$
\boxed{
 B^{[p]}_e(M)
 =\sum\log\operatorname {rad}_{q>p}\mathcal J_{r,s}.}
\tag{3.3}
$$



This is strictly weaker than controlling every foreign factor above
$2r+3$, but it is not a numerical saving because the corresponding
lower-bound object must also be $A^{[p]}$.

Item 409's pinned actual row



$$
(p,r,s,J)=(709,347,2,79)
\tag{3.4}
$$



has $j^{\rm tie}=1$ and $L^{[p]}=1$.  It remains a single exact
formula witness, not a census.  The certificate's other cutoff packets
are explicitly non-actual and serve only to replay (2.5).

## 4. Aligned and transverse foreign support

Split



$$
F^{[p]}_{r,s}
 =F^\parallel_{r,s}F^\perp_{r,s},
\tag{4.1}
$$



where



$$
q\mid F^\parallel
 \Longleftrightarrow
 q\equiv2r+3\pmod6,
\tag{4.2}
$$



and $F^\perp$ contains the other nonzero residue class.  The two
supports are disjoint.

If $q\mid F^\parallel$, then
$q\mid\mathcal J_{r,s}\mid\Pi_r$.  Equations (1.10)-(1.11) give a
future ordinary row with the same $r$.  Applying Item 349's tied-safe
equivalence in characteristic $q$ gives



$$
q\mid\Pi_r
 \Longleftrightarrow
 (q,r,t)\text{ is a future degenerate-gate row}.
\tag{4.3}
$$



For one fixed source $M$, the map



$$
(r,q)\longmapsto(M_q,q,r,t)
\tag{4.4}
$$



is injective.  Hence aligned foreign mass is exactly forward
degenerate-gate pollution.  This is not a fixed-$M$ upper bound: the
future slices $M_q$ are unbounded within the inherited pointwise
height, and the future gate statement contains no target information.

For $F^\perp$, the quotient



$$
{q-2r-3\over6}
\tag{4.5}
$$



is not an integer, so there is no same-$r$ ordinary row.  A cross-$r$
relation or unmatched resultant would be new arithmetic.

Thus



$$
B^{[p]}_e=B^\parallel_e+B^\perp_e,
\tag{4.6}
$$



and a sufficient Closer theorem is



$$
B^\parallel_e(M)=o(M),
 \qquad
 B^\perp_e(M)=o(M).
\tag{4.7}
$$



Neither estimate is proved.

## 5. Gate transport is not target transport

At the source row, $q\mid F^{[p]}$ means



$$
q\mid\Pi_r,\qquad q\nmid\Gamma_{r,s}.
\tag{5.1}
$$



At the future row, however,



$$
\Gamma_{r,t}
 =\gcd\bigl(\Pi_r,
             |\operatorname {num}T_0(r,t)|,
             |\operatorname {num}T_1(r,t)|\bigr).
\tag{5.2}
$$



The residuals use different second parameters and different tied
characteristics.  Item 409's replacement



$$
T_\nu(r,s)\equiv
 (-1)^s\bigl(
 f_\nu Z_{r,s}+9\,4^sb_\nu-11v_\nu
 \bigr)\pmod p
\tag{5.3}
$$



preserves tied-$p$ support only.  It cannot be reduced modulo a foreign
$q$ as an integer identity to identify $\Gamma_{r,t}$.

Therefore an $r$-only common-divisor resultant for
$(\mathfrak a_r,\mathfrak b_r,K_r)$ can at most reproduce the future
gate in (4.3).  Without a new two-parameter identity involving the
actual target residual, it cannot convert source foreign support into a
future rejection.  This is a scoped boundary for same-$r$ gate-only
transport, not an impossibility theorem for every unmatched resultant
or reciprocity law.

## 6. Unconditional size and support-count screen

Item 349 gives



$$
\log^+\mathcal J_{r,s}
 \le\log^+\Pi_r
 =O(r\log r).
\tag{6.1}
$$



On the actual fixed-$M$ interval,



$$
1\le r\le {2M-21\over5},
 \qquad
 {4M+3\over5}\le p\le{6M-1\over7}.
\tag{6.2}
$$



The number of prime rows on one ray is $O(M/\log M)$, by the standard
Chebyshev/Brun--Titchmarsh upper bound for this fixed-proportion
interval.  Since $F^{[p]}\mid\operatorname {rad}\mathcal J$, summing
(6.1) over those rows gives



$$
B^{[p]}_e(M)
 \le\sum\log^+\mathcal J_{r,s}
 =O(M^2).
\tag{6.3}
$$



Every prime in $F^{[p]}$ is greater than $p\gg M$, so



$$
F^{[p]}_{r,s}
 >p^{\omega(F^{[p]}_{r,s})}
 \quad(F^{[p]}>1).
\tag{6.4}
$$



The same height argument gives



$$
\sum\omega(F^{[p]}_{r,s})
 =O(M^2/\log M).
\tag{6.5}
$$



These bounds count radical support once per row; valuation depth is not
credited.  The improvement from the all-integer-row
$O(M^2\log M)$ height sum to (6.3) still misses $o(M)$ by an entire
power of $M$.

### 6.1 Sharpness in the height-and-support information class

The order in (6.3) cannot be improved from only the row count, the
pointwise height, and $q>p$.  In a fixed positive-length subinterval
where $r\asymp M$, decorate
$N_M\asymp M/\log M$ abstract ray labels.  For each label choose, by
Bertrand's postulate, a prime



$$
\exp(cM\log M)<q_i<2\exp(cM\log M),
\tag{6.6}
$$



and formally set its squarefree foreign carrier equal to $q_i$.  Then



$$
\log q_i=\Theta(M\log M),
 \qquad
 \sum_{i=1}^{N_M}\log q_i=\Theta(M^2),
\tag{6.7}
$$



while every $q_i>p_i\gg M$ and the pointwise height condition holds.
The same prime may be reused, so no prime-in-short-interval or
residue-class theorem is required.

This is an **ABSTRACT HEIGHT/SUPPORT MODEL, NOT AN ACTUAL VALUE OF
$\Pi_r,\Gamma_{r,s}$, OR $\mathcal J_{r,s}$**.  It proves only that
the named information cannot yield $B^{[p]}=o(M)$.  A formula-specific
relation among the actual connection minors can evade the model.

## 7. Exact capacity boundary

Suppose one actual cutoff gives



$$
A^{[Y]}_e(M)\ge aM+o(M),
 \qquad
 B^{[Y]}_e(M)\le bM+o(M),
\tag{7.1}
$$



and retain Item 407's bounds



$$
G_e(M)\le gM+o(M),
 \qquad
 N_e(M)\le nM+o(M).
\tag{7.2}
$$



Then



$$
\boxed{
 \Delta\mathcal C_e\ge{1\over6}
 \max\left\{0,a-b,{1\over35}-g-n\right\}.}
\tag{7.3}
$$



Changing the cutoff changes the plausibility of the two hypotheses in
(7.1), but not their exact difference.  In particular:

1. $B^{[p]}=o(M)$ alone books nothing without a positive lower bound
   for $A^{[p]}$.
2. $A^{[p]}=o(M)$ closes this direct Builder mechanism because
   $0\le J_e\le A^{[p]}$, but it does not reduce the full
   ordinary-$j=2$ ceiling without complementary chart control.
3. $A^{[p]}\ge aM+o(M)$ and $B^{[p]}=o(M)$, with $a>0$, would
   book $a/6$ on this ray.
4. The unconditional $O(M^2)$ estimate is not a finite linear upper
   coefficient and must not enter the ledger.

The smallest foreign-tail Closer target is therefore



$$
\boxed{
 \sum_{\text{actual fixed-}M\ e\text{-ray rows}}
 \log\operatorname {rad}_{q>p}\mathcal J_{r,s}=o(M),}
\tag{7.4}
$$



or the two separate estimates in (4.7).

## 8. Scoped obstruction, replay, and strict labels

The obstruction is limited to:

1. adaptive primorial saturation that excludes $p$;
2. Item 349's pointwise height;
3. the $r$-only gate carrier $\Pi_r$; and
4. same-$r$ forward transport of aligned foreign primes.

Within these inputs, raising the cutoff removes equal tail and foreign
mass; height remains superlinear; aligned transport reaches only a
future gate; and transverse support has no same-$r$ target.  This does
not exclude a formula-specific large-prime theorem, a cross-$r$
resultant, target-residual reciprocity, or an average weighted theorem.

The deterministic certificate pins audited canonical Items 349, 409, and
413.  It verifies cutoff
factorization, monotonicity, selected-$p$ saturation, aligned and
transverse geometry, the Item 409 witness, capacity arithmetic, and
byte-identical replay.  Auxiliary support packets are labelled
**NOT ACTUAL**.

Replay from the archive root:

~~~powershell
python scripts/item416_j2_adaptive_foreign_tail_transport_certificate.py --replay results/item416_j2_adaptive_foreign_tail_transport_certificate.json --output results/item416_j2_adaptive_foreign_tail_transport_certificate_replay.json
~~~

### Strict labels

- **PROVED:** (1.6), cutoff invariance (1.8), free removal of the middle
  foreign range, aligned forward gate transport, the size screens
  (1.12), the conditional capacity theorem (7.3), and zero booking.
- **EXACT PINNED ACTUAL WITNESS / NOT A CENSUS:** the Item 409 row
  $(709,347,2)$.
- **EXACT ALGEBRAIC SUPPORT PACKETS / NOT ACTUAL:** the cutoff and
  transport examples used only for replay.
- **ABSTRACT HEIGHT/SUPPORT MODEL / NOT ACTUAL:** Section 6.1, used only
  to prove sharpness for the stated information class.
- **CONDITIONAL:** every positive capacity implication whose
  $(a,b,g,n)$ antecedents are displayed.
- **OPEN:** (7.4), its aligned and transverse components, any positive
  adaptive-tail minus foreign-tail margin, target-status transport,
  Route 1, and every conclusion about $e+\pi$.

Accordingly Item 416 removes avoidable foreign noise and identifies the
remaining forward/transverse arithmetic, but proves no positive
linear-exponent gain.
