> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 319 - the third connection minor and the period-elimination barrier

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Retain the actual ordinary-$j=2$ rows



$$
r=6n+e,\qquad e\in\{1,5\},\qquad
 p=2r+6s+3,\qquad c=2^{2s},
 \tag{1.1}
$$



and Item 318's connection-plane coordinates



$$
\ell_r=\det(f,b),\qquad m_r=\det(f,d),\qquad
 C_r=\det(b,d).
 \tag{1.2}
$$



The old determinant and actual-period residual are



$$
D_{r,s}=9c\ell_r-11m_r,\qquad
 E_{r,s}=\ell_rZ_{r,s}+11C_r.
 \tag{1.3}
$$



This item begins with the capacity and overlap audit, then determines the
all-$r$ compulsory content of $C_r$.

> **PROVED - all-$r$ third-minor factorization.**  There is an explicit
> canonical rational sequence $K_r$ such that
> 

$$
> \boxed{C_r=\beta_rK_r},\qquad
> \boxed{\beta_r=
> -\frac{3(r+1)!}{2(2r+3)(-r/3)_{r+1}}.}
> \tag{1.4}
>
$$


> The factor $K_r$ is the determinant of a canonical inhomogeneous
> connection vector and a normalized homogeneous connection vector.  It is
> not defined by dividing $C_r$; Section 4 gives its independent chain
> construction.

> **PROVED - the removed factor has no capacity.**  On every actual row,
> 

$$
> v_p(\beta_r)=0.
> \tag{1.5}
>
$$


> Thus $C_r\equiv0\pmod p$ if and only if
> $K_r\equiv0\pmod p$.  Formula (1.4) removes compulsory
> hypergeometric content but does not localize any actual prime.

> **PROVED - global minor/resultant no-go on both nondegenerate charts.**
> Let $R=k[c,\ell,m,C]$, adjoin $Z$, and put
> 

$$
> D=9c\ell-11m,\quad E_b=\ell Z+11C,\quad
> E_d=mZ+9cC.
> \tag{1.6}
>
$$


> Then
> 

$$
> \boxed{\ell E_d-mE_b=CD.}
> \tag{1.7}
>
$$


> After localizing at $\ell$, or separately at $m$, the
> coefficient-only elimination ideal of $(D,E_b,E_d)$ is exactly
> $(D)$.  Therefore eliminating the actual period from the entire
> exterior-minor tower produces no second coefficient divisor beyond the
> Item-314 determinant.

The transverse condition remains a genuine condition only while the actual
incomplete-beta/logarithmic period $Z_{r,s}$ is retained.  No weighted gcd
bound is proved.  Consequently



$$
\boxed{\text{new capacity reduction}=0},\qquad
 \boxed{\text{new booking}=0},
 \tag{1.8}
$$



and the ordinary-$j=2$ ceiling remains $1/105$ per $6M$.

## 2. Capacity and overlap audit

On a fixed target slice,



$$
2M=5r+14s+7.
 \tag{2.1}
$$



Item 314 supplies the all-row $p$-unit-equivalent integer gate



$$
\widehat D_{r,s}
 =H_r\bigl(18c\,\mathfrak a_r+11\mathfrak b_r\bigr),
 \qquad H_r=6^{r+3}r!,
 \tag{2.2}
$$



while Item 318 supplies the all-row $p$-unit clearing



$$
\widehat E_{r,s}
 =Q_{r,s}^{\,4}\bigl(\ell_rZ_{r,s}+11C_r\bigr)\in\mathbb Z.
 \tag{2.3}
$$



Every actual collision prime divides both integers.  Hence the exact Closer
target would be



$$
\sum_{\substack{(r,s)\text{ on }(2.1)\\
 p\mid\gcd(\widehat D_{r,s},\widehat E_{r,s})}}
 \log p=o(M).
 \tag{2.4}
$$



The second residual lies strictly inside the already retained
$D=0$ branch.  Its raw support cannot be added to the ledger as a
separate source of capacity.  It can only reduce the existing
$1/105$ ceiling.

Before Item 319, three possible shortcuts had to be screened:

1. remove compulsory content from $C_r$;
2. ask whether the old order-three connection operator already controls
   the third minor; and
3. eliminate $Z$ to seek a second coefficient-only resultant.

The first succeeds structurally but removes only a $p$-unit.  The second
fails by exact first-row counterexamples on both rays.  The third is closed
globally by the Laurent-chart theorem in Section 7.

## 3. The inherited arithmetic of $\ell_r$ and $m_r$

Let



$$
\sigma_{e,n}=\frac{g_n\kappa_e}{16^n}.
 \tag{3.1}
$$



Items 314 and 315 prove, for every $n\ge0$,



$$
\boxed{\ell_r=2\sigma_{e,n}\mathfrak a_r},\qquad
 \boxed{m_r=-\sigma_{e,n}\mathfrak b_r}.
 \tag{3.2}
$$



Here $\mathfrak a_r$ is the $y=-1$ algebraic-branch coefficient and
$\mathfrak b_r$ is the $y=0$ coefficient.  The common scale
$\sigma_{e,n}$ is a $p$-unit on every actual row.  Substitution in
(1.3) gives



$$
D_{r,s}
 =\sigma_{e,n}
   \bigl(18c\,\mathfrak a_r+11\mathfrak b_r\bigr),
 \tag{3.3}
$$



which is exactly the Item-314 gate, not a new contribution.

## 4. Independent construction of $K_r$

Put



$$
\bar q=-\frac{2r+3}{3},
 \tag{4.1}
$$



and retain the two coefficient kernels



$$
P_0(z)=(1-z)^r(1+z),\qquad
 P_1(z)=(1-z)^r(1+z)^4.
 \tag{4.2}
$$



Write $P_{\nu,\ell}=[z^\ell]P_\nu(z)$.

Define the normalized homogeneous chain $\eta_k$ by



$$
\eta_{2t}=0,\qquad \eta_1=1,\qquad
 \eta_{k+2}=-\frac{\bar q+k}{3\bar q+k}\eta_k
 \quad(k\text{ odd}).
 \tag{4.3}
$$



Define the canonical inhomogeneous chain $y_k$ by



$$
(\bar q+k)y_k+(3\bar q+k)y_{k+2}=1.
 \tag{4.4}
$$



The even chain has $y_0=0$.  The odd chain has the Frobenius endpoint
boundary



$$
y_{2r+3}=0
 \tag{4.5}
$$



and is solved backward.  No free terminal period remains in $y$.

Now set



$$
\begin{aligned}
 S_0&=\sum_{\ell=0}^{r+1}
 P_{0,\ell}(y_{\ell+1}+y_{\ell+3}),&
 S_1&=\sum_{\ell=0}^{r+4}P_{1,\ell}y_\ell,\\
 \Delta_0&=\sum_{\ell=0}^{r+1}
 P_{0,\ell}(\eta_{\ell+1}+\eta_{\ell+3}),&
 \Delta_1&=\sum_{\ell=0}^{r+4}P_{1,\ell}\eta_\ell.
\end{aligned}
\tag{4.6}
$$



Finally,



$$
\boxed{K_r=S_0\Delta_1-S_1\Delta_0.}
 \tag{4.7}
$$



This is the promised independent definition.

## 5. Proof of the third-minor factorization

In Item 250's affine chain, let $v_k$ and $w_k$ be the coefficients of
the endpoint $c$ and the constant coordinate.  Their sum satisfies



$$
y_k=v_k+w_k,
 \tag{5.1}
$$



because the two affine recurrences add to (4.4).  On the odd Frobenius
endpoint, $v_{2r+3}+w_{2r+3}=0$, which gives (4.5).  On the even chain,
both constant seeds vanish, giving $y_0=0$.  Therefore



$$
(b_0+d_0,b_1+d_1)=(S_0,S_1).
 \tag{5.2}
$$



The constant coordinate is homogeneous on the odd chain.  If
$\beta_r=w_1$, then



$$
(d_0,d_1)=\beta_r(\Delta_0,\Delta_1).
 \tag{5.3}
$$



Consequently



$$
\begin{aligned}
 C_r
 &=\det(b,d)
  =\det(b+d,d)\\
 &=\beta_r(S_0\Delta_1-S_1\Delta_0)
  =\beta_rK_r.
\end{aligned}
\tag{5.4}
$$



It remains to evaluate $w_1$.  At $k_*=2r+3$,



$$
w_{k_*}=-\frac1{\bar q+k_*}.
 \tag{5.5}
$$



Descending the homogeneous odd recurrence through the $r+1$ odd pivots
gives



$$
\begin{aligned}
 \beta_r
 &=-\frac1{\bar q+2r+3}
   \frac{((3\bar q+1)/2)_{r+1}}
        {((\bar q+1)/2)_{r+1}}\\
 &=-\frac{3(r+1)!}
        {2(2r+3)(-r/3)_{r+1}},
\end{aligned}
\tag{5.6}
$$



because $r+1$ is even.  This proves (1.4) for all $r$ on both rays.

## 6. Unit audit and the quotient $C_r/\ell_r$

The factors of the rising denominator in (5.6) are



$$
-\frac r3+j=\frac{3j-r}{3},\qquad 0\le j\le r.
 \tag{6.1}
$$



They are nonzero because every actual row has $3\nmid r$.  Moreover,



$$
|3j-r|\le2r<p,\qquad r+1<2r+3<p.
 \tag{6.2}
$$



The constants $2,3$, the factor $2r+3$, and every factorial factor are
also below $p$.  Hence $v_p(\beta_r)=0$, proving (1.5).  The recurrence
pivots defining $S$ and $\Delta$ are the already audited Item-250
$p$-units, so $K_r$ has a $p$-unit denominator on every actual row.

Combining (3.2) and (5.4) gives the exact characteristic-zero quotient



$$
\boxed{
 \frac{C_r}{\ell_r}
 =\frac{\beta_r}{2\sigma_{e,n}}\,
  \frac{K_r}{\mathfrak a_r}.}
 \tag{6.3}
$$



Item 315 proves $\mathfrak a_r<0$, so (6.3) is defined over
$\mathbb Q$ on both rays.  It is **not** used modulo $p$ when
$p\mid\ell_r$ or $p\mid\mathfrak a_r$.

The safe modular form is division-free:



$$
E_{r,s}
 =2\sigma_{e,n}\mathfrak a_rZ_{r,s}+11\beta_rK_r.
 \tag{6.4}
$$



Both displayed scalar factors are actual-row $p$-units.  Removing them
normalizes the condition but excludes no prime and gives no capacity
reduction.

## 7. The Laurent-chart elimination theorem

Besides Item 318's syzygy, direct expansion gives



$$
\begin{aligned}
 \ell E_d-mE_b
 &=\ell(mZ+9cC)-m(\ell Z+11C)\\
 &=C(9c\ell-11m)=CD.
\end{aligned}
\tag{7.1}
$$



This identity holds over every commutative coefficient ring.

On the $\ell$-chart, $E_b=0$ gives



$$
Z=-\frac{11C}{\ell}.
 \tag{7.2}
$$



After this substitution,



$$
E_d=\frac{CD}{\ell}.
 \tag{7.3}
$$



Thus



$$
(D,E_b,E_d)\cap R[\ell^{-1}]=(D).
 \tag{7.4}
$$



More precisely, the left ideal is first taken in
$R[\ell^{-1},Z]$, then eliminated to $R[\ell^{-1}]$.

On the $m$-chart, $E_d=0$ gives



$$
Z=-\frac{9cC}{m},\qquad
 E_b=-\frac{CD}{m},
 \tag{7.5}
$$



and hence



$$
(D,E_b,E_d)\cap R[m^{-1}]=(D).
 \tag{7.6}
$$



These are exact quotient-ring isomorphisms, not dimension heuristics or
finite tests.  They prove the scoped no-go:



$$
\boxed{\text{minor arithmetic alone cannot create a second
 coefficient-only resultant after }Z\text{ is eliminated}.}
 \tag{7.7}
$$



The actual-period equation is not redundant.  Rather, it cannot be replaced
by an invariant involving only $(c,\ell,m,C)$.  Any successful Closer
theorem must retain arithmetic information about $Z_{r,s}$.

## 8. Why individual height or recurrence does not close the branch

There are $O(M)$ tied rows satisfying (2.1).  An individual numerator
bound such as



$$
\log|\widehat E_{r,s}|=O(M\log M)
 \tag{8.1}
$$



would only give, after summing over all rows, an
$O(M^2\log M)$ support bound.  Even an $O(M)$ bound per row would sum
to $O(M^2)$.  Neither implies the required $o(M)$ estimate (2.4).

The certificate also gives exact, nonzero first recurrence residuals on
both rays for all five most natural direct-reuse ansatzes:

- the Item-291 operator on $C_n$;
- the same operator on $16^nC_n$;
- the Item-237 operator on $C_n/\sigma_n$;
- its $16^{-n}$-scaled version; and
- the Item-237 operator on $K_n$.

One exact nonzero first residual is sufficient to disprove each global
operator identity.  This is a theorem about those five stated ansatzes, not
a scan.  A different higher-order recurrence or algebraic realization of
$K_r$ remains open.  Such a realization would still need a
sequence-specific weighted gcd theorem to affect (2.4).

## 9. Deterministic replay

The certificate reconstructs $\ell_r,m_r,C_r,\beta_r,K_r$ exactly for
the 18 admissible odd indices $r\le53$, verifies (3.2) and (5.4), and
records a deterministic row-stream digest.  This bounded replay checks the
implementation only; the all-$r$ proof is the chain derivation in
Sections 4-5.

No prime census is used in this item.

## 10. Strict labels

**PROVED**

- the inherited all-$r$ normalizations (3.2);
- the canonical factorization $C_r=\beta_rK_r$;
- the actual-row $p$-unit theorem for $\beta_r$;
- the quotient formula (6.3), with its modular division warning;
- both exact Laurent-chart elimination ideals;
- exact counterexamples to five specific old-operator reuse ansatzes; and
- zero capacity booking.

**EXACT FINITE REPLAY**

- the 18 declared rational identity rows through $r=53$.

**OPEN**

- a different recurrence or algebraic realization for $K_r$;
- an $o(M)$ weighted gcd theorem for (2.4);
- arithmetic control of the actual incomplete-beta period in (6.4); and
- any reduction of the retained $1/105$ ceiling.

