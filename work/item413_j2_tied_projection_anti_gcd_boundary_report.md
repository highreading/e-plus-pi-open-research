> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 413 — tied-prime projection and the foreign-tail boundary for the ordinary-$j=2$ anti-gcd carrier

Checked: 2026-09-01 (Beijing time)

## 1. Capacity first and verdict

Retain one actual ordinary-(j=2) ray



$$
p=2r+6s+3,qquad r=6M-7p,qquad
 s={5p-4M-1\over2},qquad
 r\equiv e\pmod6,quad e\in\{1,5\}.
\tag{1.1}
$$



Its raw Chebyshev mass is



$$
R_e(M)={1\over35}M+o(M),
\tag{1.2}
$$



and its normalized capacity is (1/210).  The two rays retain the
ordinary-(j=2) ceiling (1/105).

Items 404, 407, and 409 give the actual carriers



$$
\Pi_r=\gcd\bigl(
 |\operatorname{num}\mathfrak a_r|,
 |\operatorname{num}\mathfrak b_r|,
 |\operatorname{num}K_r|
 \bigr),
\tag{1.3}
$$





$$
\Gamma_{r,s}=\gcd\bigl(
 \Pi_r,|\operatorname{num}T_0|,|\operatorname{num}T_1|
 \bigr),
\tag{1.4}
$$



and, after tied-prime-safe saturation,



$$
\mathcal J_{r,s}
 =\bigl(\Pi^{\rm sat}_{r,s}\bigr)_{
    (\Gamma^{\rm sat}_{r,s})}.
\tag{1.5}
$$



Here (A_{(B)}) means the largest divisor of (A) coprime to (B).
Item 409 shows on the actual row ((p,r,s)=(709,347,2)) that



$$
\Pi^{\rm sat}=\mathcal J=79,qquad
 \Gamma^{\rm sat}=1,qquad 709\nmid79.
\tag{1.6}
$$



Thus a nontrivial or even large integer (mathcal J) is not itself a
tied-prime rejection.  This item replaces that unsafe statistic by the
exact selected projection.

> **PROVED — exact binary tied Smith quotient.**  On every actual row,
> 

$$
> \boxed{
> j^{\rm tie}_{r,s}
> ={\gcd(p,\Pi_r)\over\gcd(p,\Gamma_{r,s})}
> ={\gcd(p,\Pi^{\rm sat}_{r,s})
>   \over\gcd(p,\Gamma^{\rm sat}_{r,s})}
> =\gcd(p,\mathcal J_{r,s})\in\{1,p\}.}
> \tag{1.7}
>
$$


> It equals (p) exactly on a degenerate row rejected by the surviving
> target and equals (1) otherwise.

> **PROVED — mandatory large-prime projection.**  Since (s\ge1),
> 

$$
> p=2r+6s+3>2r+3.
> \tag{1.8}
>
$$


> If
> 

$$
> L_{r,s}=\operatorname{rad}_{q>2r+3}\mathcal J_{r,s},
> \qquad F_{r,s}=(L_{r,s})_{(p)},
> \tag{1.9}
>
$$


> then
> 

$$
> \boxed{L_{r,s}=j^{\rm tie}_{r,s}F_{r,s},qquad
>        \gcd(j^{\rm tie}_{r,s},F_{r,s})=1.}
> \tag{1.10}
>
$$


> Thus every factor at or below (2r+3), and every remaining factor
> unequal to the selected (p), is rigorously foreign to the capacity
> ledger.

> **PROVED — exact aggregate anti-gcd identity.**  On one fixed ray put
> 

$$
> A_e(M)=\sum\log L_{r,s},qquad
> B_e(M)=\sum\log F_{r,s}.
> \tag{1.11}
>
$$


> The sums are over the actual tied-prime rows.  Then
> 

$$
> \boxed{J_e(M)=A_e(M)-B_e(M)=D_e(M)-G_e(M),}
> \tag{1.12}
>
$$


> where (J_e) is the actual degenerate target-rejection mass and
> (D_e,G_e) are Item 407's degenerate-gate and degenerate-collision
> masses.

> **PROVED — sharp capacity boundary.**  If actual theorems give
> 

$$
> A_e(M)\ge aM+o(M),\quad B_e(M)\le bM+o(M),\quad
> G_e(M)\le gM+o(M),\quad N_e(M)\le nM+o(M),
> \tag{1.13}
>
$$


> then
> 

$$
> \boxed{
> \Delta\mathcal C_e\ge {1\over6}
> \max\left\{0,a-b,{1\over35}-g-n\right\}.}
> \tag{1.14}
>
$$


> Conversely, an upper bound (A_e(M)\le uM+o(M)) limits the reward
> obtainable from the direct matched-(mathcal J) mechanism to at most
> 

$$
> \boxed{{1\over6}\min\{u,1/35\}.}
> \tag{1.15}
>
$$


> Formula (1.15) is not an upper bound for independent nondegenerate or
> off-chart exclusions.

No positive (a-b), useful (g+n<1/35), or finite (u) improving the
raw bound is proved.  Hence



$$
\boxed{j_{\rm proved}=0},\qquad
 \boxed{\Delta\mathcal C=0},\qquad
 \boxed{\text{ordinary-}j=2\text{ ceiling remains }1/105}.
\tag{1.16}
$$



There is no prime census and no finite extrapolation.

## 2. Proof of the binary quotient

Write



$$
\pi_p(A)=\gcd(p,A).
\tag{2.1}
$$



Because (p) is prime, (pi_p(A)\in\{1,p\}).  Item 404 proves
(Gamma_{r,s}\mid\Pi_r); hence



$$
\pi_p(\Gamma_{r,s})\mid\pi_p(\Pi_r).
\tag{2.2}
$$



The quotient in (1.7) is therefore an integer in ({1,p}).  It is
(p) precisely when (p\mid\Pi_r) and (p\nmid\Gamma_{r,s}).
By Item 404, these are precisely the degenerate-gate rows which fail the
surviving target.

Let (S_{r,s}) be the safe saturation product.  Item 338 gives
(p\nmid S_{r,s}), so removing all prime powers supported on (S_{r,s})
does not change either (p)-support:



$$
\pi_p(\Pi_r)=\pi_p(\Pi^{\rm sat}_{r,s}),qquad
 \pi_p(\Gamma_{r,s})=\pi_p(\Gamma^{\rm sat}_{r,s}).
\tag{2.3}
$$



Finally, (mathcal J=(\Pi^{\rm sat})_{(\Gamma^{\rm sat})}) contains
the full (p)-part of (Pi^{\rm sat}) when
(p\nmid\Gamma^{\rm sat}), and none of it when
(p\mid\Gamma^{\rm sat}).  Therefore



$$
\pi_p(\mathcal J)
 ={\pi_p(\Pi^{\rm sat})\over\pi_p(\Gamma^{\rm sat})},
\tag{2.4}
$$



which proves (1.7).  Notice that valuation excess is deliberately not
credited: if (p) divides both (Pi) and (Gamma), the row is a
collision even when their (p)-adic valuations differ.

## 3. The (2r+3) threshold and the actual factor (79)

The actual phase relation gives



$$
p-(2r+3)=6s\ge6.
\tag{3.1}
$$



Consequently the selected characteristic can occur only in the radical
tail supported on primes (q>2r+3).  Define (L,F) as in (1.9).
Since (p>2r+3),



$$
\gcd(p,L)=\gcd(p,\mathcal J)=j^{\rm tie}.
\tag{3.2}
$$



The integer (L) is squarefree.  Removing its selected (p)-factor gives
(F=L_{(p)}), so (1.10) follows immediately.

For Item 409's exact actual-formula witness,



$$
2r+3=697,qquad \mathcal J=79.
\tag{3.3}
$$



Hence



$$
\operatorname{rad}_{q>697}(79)=1,qquad
 j^{\rm tie}=\gcd(709,79)=1.
\tag{3.4}
$$



This does not say that every foreign factor is below (2r+3), nor does
it prove tied-prime good reduction.  It proves exactly that the known
factor (79) is inadmissible as density evidence and motivates applying
the threshold before any size or support statistic is considered.

## 4. Exact aggregate factorization

Sum the logarithm of (1.10) over the actual tied rows on one fixed ray.
Because every factor is positive,



$$
\sum\log j^{\rm tie}_{r,s}
 =\sum\log L_{r,s}-\sum\log F_{r,s}
 =A_e(M)-B_e(M).
\tag{4.1}
$$



By (1.7), the left side is precisely



$$
J_e(M)=
 \sum_{\substack{p\text{ on the ray}\\p\mid\mathcal J_{r,s}}}\log p.
\tag{4.2}
$$



Item 407 independently gives (J_e=D_e-G_e), proving (1.12).  The
identity has two useful interpretations:

1. **Builder form:** lower-bound the large-prime tail (A_e) and
   upper-bound the unmatched foreign tail (B_e).
2. **Closer form:** prove (A_e=o(M)).  Then (J_e=o(M)), so this direct
   rejection mechanism has zero positive-linear capacity.

The second conclusion books no saving by itself.  It says that the
degenerate rejection set is thin, not that the full collision set is thin;
the nondegenerate chart can still occupy the ray.

## 5. Capacity theorem and direct-channel upper boundary

Under (1.13), (1.12) gives



$$
J_e(M)\ge(a-b)M+o(M).
\tag{5.1}
$$



Since (J_e\ge0), the certified lower coefficient is
((a-b)_+).  Item 409's exact chart coupling also gives the independent
exclusion



$$
R_e-(G_e+N_e)
 \ge\left({1\over35}-g-n\right)M+o(M).
\tag{5.2}
$$



Taking the stronger of (5.1) and (5.2), then dividing by (6M), proves
(1.14).

For the opposite direction, (J_e=A_e-B_e\le A_e) and
(J_e\le R_e).  Thus (A_e\le uM+o(M)) implies



$$
J_e(M)\le\min\{u,1/35\}M+o(M),
\tag{5.3}
$$



which proves (1.15).  This is an admission threshold: if a proposed
formula can control only a tail of maximum mass (u), it cannot deliver
more than (u/6) through the direct anti-gcd channel.

## 6. Sharp support-statistic no-go

Consider the information class which retains, row by row,

1. the actual labels (p,r,s) and the threshold (2r+3);
2. positive integers (Pi,Gamma) with (Gamma\mid\Pi);
3. tied-prime-safe saturation;
4. the integer (mathcal J=(\Pi^{\rm sat})_{(\Gamma^{\rm sat})}); and
5. lower bounds for the size, radical, or large-prime tail of
   (mathcal J),

but no theorem matching a tail prime to the selected (p).

Within this class, no positive tied rejection mass follows.  For example,
on a formal row choose a prime (q>2r+3) with (q\ne p), and take



$$
S=1,qquad \Pi=q,qquad \Gamma=1,qquad \mathcal J=q.
\tag{6.1}
$$



Then (L=q) can be arbitrarily large while



$$
j^{\rm tie}=\gcd(p,q)=1,qquad F=q.
\tag{6.2}
$$



Alternatively, (Pi=pq,Gamma=p) gives the same foreign tail on a tied
collision row.  Choosing (Pi=p,Gamma=1) gives a matched rejection.
Mixtures attain every difference allowed by (A-B).  Therefore an
(A)-lower bound together with a (B)-upper bound yields exactly
((a-b)_+), and no stronger universal coefficient.

These are **exact algebraic packets, not actual values of the connection
sequences**.  They prove sharpness only for the stated information class.
They do not refute a formula-specific relation forcing actual large-prime
tail factors to equal the tied characteristic.

The actual Item 409 witness provides a separate formula anchor: it proves
that foreign contamination is not merely an abstract logical possibility,
although its factor (79) lies below the new threshold and therefore says
nothing about the actual foreign tail above (2r+3).

## 7. The remaining actual arithmetic target

Substituting Item 409's formulae into (1.7) gives



$$
j^{\rm tie}_{r,s}=p
\tag{7.1}
$$



exactly when



$$
p\mid\operatorname{num}\mathfrak a_r,qquad
 p\mid\operatorname{num}\mathfrak b_r,qquad
 p\mid\operatorname{num}K_r,qquad
 (T_0,T_1)\not\equiv(0,0)\pmod p.
\tag{7.2}
$$



All denominators are tied-(p) units.  On the branch (f\ne0), the last
condition is one scalar residual containing the actual incomplete period
(A_s).  On (f=0), it is the vector inequality



$$
9\,4^s b-11v\ne(0,0)\pmod p.
\tag{7.3}
$$



The smallest direct theorem remains



$$
\boxed{
 \sum_{\text{actual fixed-}M\text{ ray rows}}
 \log j^{\rm tie}_{r,s}
 \ge\delta M+o(M)}
\tag{7.4}
$$



for some (delta>0).  The exactly equivalent decomposed target is



$$
A_e(M)\ge aM+o(M),qquad B_e(M)\le bM+o(M),qquad a-b>0.
\tag{7.5}
$$



Unlike a lower bound for (|\mathcal J|), (7.5) explicitly pays the
foreign-support loss.  Unlike a prime census, it is already an asymptotic
Chebyshev statement on the selected fixed-(M) diagonal.

The opposite formula-specific theorem



$$
A_e(M)=o(M)
\tag{7.6}
$$



would close this direct Builder branch by (4.1), but would not lower the
ordinary-(j=2) ceiling without separate information on (G_e+N_e).

## 8. Deterministic certificate and strict labels

The certificate pins the audited canonical Items 404 and 407 and the
complete work Item 409 package.  It verifies the binary quotient before
and after safe saturation, the (2r+3) threshold, the matched/foreign
tail factorization, Item 409's exact actual witness, the sharp capacity
arithmetic, and byte-identical replay.  Its declared support packets are
labelled **NOT ACTUAL / NO CENSUS**.

Replay from the archive root:

~~~powershell
python work/item413_j2_tied_projection_anti_gcd_boundary_certificate.py --replay work/item413_j2_tied_projection_anti_gcd_boundary_certificate.json --output work/item413_j2_tied_projection_anti_gcd_boundary_certificate_replay.json
~~~

### Strict labels

- **PROVED:** (1.7), the threshold (1.8), the factorization (1.10), the
  aggregate identity (1.12), the conditional capacity theorem (1.14),
  the direct-channel upper boundary (1.15), and zero booking.
- **EXACT PINNED ACTUAL WITNESS, NOT A CENSUS:** the row
  ((709,347,2)), for which (79) is foreign and below threshold.
- **EXACT ALGEBRAIC COUNTERMODELS, NOT ACTUAL:** the packets used to
  prove sharpness of the support-statistic information boundary.
- **CONDITIONAL:** every positive capacity conclusion whose
  (a,b,g,n) antecedents are displayed.
- **OPEN:** every positive actual matched-(mathcal J) theorem, every
  useful actual tail/foreign-tail pair, tied-prime good reduction, Route 1,
  and every conclusion about (e+\pi).

Accordingly Item 413 supplies a safe exact statistic and a sharp screening
boundary, but no positive linear exponent gain.
