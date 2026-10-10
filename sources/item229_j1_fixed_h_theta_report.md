> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 229 — fixed-$h$ reduction of the corrected $j=1$ transfer determinant

## 1. Outcome

Item 223, after correction of the upper Frobenius multiplier, gives the
necessary condition



$$
\Theta:=\Delta_+-2\Delta_-=0\pmod p.                         \tag{1.1}
$$



This item compares (1.1) with the fixed-$h$ phase eliminant
$E_h(s)$ of Items 218 and 222.  It proves an exact all-$h$
Gosper reduction of $\Theta$.  In this direct polynomial-antidifference
ansatz the reduction exposes one surviving incomplete-binomial coordinate,
so the displayed formulas alone do not reduce the comparison to an
ordinary resultant of rational functions of $s$.  A different identity
could still control or cancel that coordinate.

There is a striking exact finite pattern.  At the row phase



$$
s_*=-{4h+3\over6},                    \tag{1.2}
$$



the coefficient of the incomplete sum is proportional to $E_h^*$
for every $1\leq h\leq80$, $3\nmid h$, with a simple
hypergeometric ratio.  No symbolic telescoping certificate for all $h$
was obtained, so this factorization is labeled **EXACT_FINITE_ONLY** and is
not used as a theorem.

The independent finite scan through $p\leq2000$ finds 22 zeros of
$\Theta$, 58 zeros of $E$, and no joint zero.  This is also
finite evidence only.  Item 229 books no positive rate or exponent.

## 2. The corrected closed determinant

Write $r=2h$, so that an actual row satisfies



$$
p=4h+6s+3.                            \tag{2.1}
$$



Use the Item 223 coefficients



$$
D_n(h,s)=[x^n](1-x)^{-2h-1}(1+x^2)^{-2s}.                    \tag{2.2}
$$



Then



$$
\begin{aligned}
\Delta_+={}&(4h+4s-1)D_{2s+4}+(2h+1)D_{2s+3}
                    -(2h+8s)D_{2s+2},\\
\Delta_-={}&-(2h+3)D_{2h+3}+(6h+5)D_{2h+2}
                    -(4h+4s+2)D_{2h+1},                       \tag{2.3}
\end{aligned}
$$



where the first equality is used modulo $p$, while the second is
an integer equality.  Item 223 proves that every common-log collision
forces (1.1) and $\Delta_+\Delta_-\ne0$.

## 3. Exact fixed-$h$ Gosper reduction

Set



$$
t_j=(-1)^j\binom{2s+j-1}{j},\qquad
 S_s=\sum_{j=0}^{s}t_j.                                      \tag{3.1}
$$



After aligning the three upper sums in (2.3), their common summand for
$0\leq j\leq s$ is $t_jP_h(s,j)$, where



$$
\begin{aligned}
P_h(s,j)={}&(4h+4s-1)\binom{2h+2s+4-2j}{2h}\\
 &+(2h+1)\binom{2h+2s+3-2j}{2h}\\
 &-(2h+8s)\binom{2h+2s+2-2j}{2h}.             \tag{3.2}
\end{aligned}
$$



For a polynomial $R(j)$, define



$$
\mathscr L_sR(j)=-(2s+j)R(j+1)-jR(j).                        \tag{3.3}
$$



The leading term of $\mathscr L_s(j^d)$ is
$-2j^{d+1}$.  Hence triangular elimination proves that there
are unique



$$
c_h(s)\in\mathbb Q[s],\qquad
 R_h(s,j)\in\mathbb Q[s,j],\qquad \deg_jR_h\leq2h-1,          \tag{3.4}
$$



such that



$$
\boxed{P_h(s,j)=c_h(s)+\mathscr L_sR_h(s,j).}    \tag{3.5}
$$



Since



$$
{t_{j+1}\over t_j}=-{2s+j\over j+1},                        \tag{3.6}
$$



the second term in (3.5) telescopes exactly:



$$
\sum_{j=0}^{s}t_jP_h(s,j)
   =c_h(s)S_s+t_{s+1}(s+1)R_h(s,s+1).                         \tag{3.7}
$$



The two omitted upper-tail terms give



$$
\boxed{\Theta_h(s)=c_h(s)S_s+t_{s+1}G_h(s)-2\Delta_-(h,s),} \tag{3.8}
$$



with



$$
\begin{aligned}
G_h(s)={}&(s+1)R_h(s,s+1)+T_h(s)
       -{3s+1\over s+2}(4h+4s-1),\\
T_h(s)={}&(4h+4s-1)\binom{2h+2}{2}+(2h+1)^2-(2h+8s).          \tag{3.9}
\end{aligned}
$$



Equations (3.5)--(3.9) are identities over $\mathbb Q$ for every
$h,s\geq1$.  They retain the actual seed and do not replace the
moving upper limit by an interpolating polynomial.

## 4. The residual coefficient is genuinely present

The same triangular calculation, now comparing the top homogeneous terms
in $s$, gives



$$
\boxed{\deg_s c_h=2h+1,\qquad
 [s^{2h+1}]c_h(s)=-{2^{4h+2}\over(2h)!}.}                     \tag{4.1}
$$



In particular $c_h$ is never the zero polynomial.  A useful
coefficient form of the same scalar is



$$
\begin{aligned}
c_h(s)=[y^{2h}]&(1+y)^{2h+6s+2}
 \left({2\over(1+y)^2+1}\right)^{2s}\\
&\times\bigl((4h+4s-1)(1+y)^2
 +(2h+1)(1+y)-(2h+8s)\bigr).                  \tag{4.2}
\end{aligned}
$$



To obtain (4.2), extend the telescoping functional to polynomial moments
and use



$$
\sum_{j\geq0}(-1)^j\binom{2s+j-1}{j}x^j=(1+x)^{-2s}.         \tag{4.3}
$$



Only finitely many derivatives of (4.3) are used, so (4.2) is a polynomial
identity in $s$, not an analytic convergence assumption.

This proves a sharply scoped obstruction for the displayed polynomial
Gosper-antidifference ansatz: its direct fixed-$h$ expression for
$\Theta_h(s)$ retains the specific incomplete sum $S_s$ with a nonzero
polynomial coefficient.  Thus these formulas, without an additional
identity for $S_s$, do not furnish a plain $\mathbb Q[s]$ resultant
with Item 222's rational eliminant.  This is not a non-rationality or
algebraic-independence theorem.  A different Gosper representation,
Ore/holonomic relation, finite-polylogarithmic identity, or arithmetic
elimination could conceivably cancel or control $S_s$.

## 5. Phase comparison with the Item 222 eliminant

At (1.2), (4.2) becomes the finite algebraic coefficient



$$
\begin{aligned}
c_h^*=[y^{2h}]&(1+y)^{-2h-1}
 (1+y+y^2/2)^{(4h+3)/3}\\
&\times\left({4h-9\over3}(1+y)^2
 +(2h+1)(1+y)+{10h+12\over3}\right).           \tag{5.1}
\end{aligned}
$$



Exact rational evaluation for every $1\leq h\leq80$,
$3\nmid h$, gives



$$
c_h^*=\mathcal R_hE_h^*.              \tag{5.2}
$$



The observed factors satisfy



$$
\mathcal R_1=-{49\over18},\qquad
 \mathcal R_2={4235\over1944},                                \tag{5.3}
$$



and



$$
{\mathcal R_{h+3}\over\mathcal R_h}=
{h(4h+1)(4h+5)(4h+7)(4h+9)(4h+11)(4h+15)^2
 \over
864(h+1)(h+2)(2h+1)^2(2h+3)(2h+5)^2(4h+3)}.                  \tag{5.4}
$$



Every factor in the finite product generated by (5.3)--(5.4) is nonzero
and has absolute value below an actual row prime, apart from powers of 2
and 3, which are also units.  Thus an all-$h$ proof of (5.2)
would imply



$$
c_h^*\equiv0\iff E_h^*\equiv0\pmod p. \tag{5.5}
$$



But (5.2) has no all-$h$ symbolic/WZ certificate in this package.
Equations (5.2)--(5.4) are labeled **EXACT_FINITE_ONLY** and (5.5) remains
**OPEN**.  The clean ratio is a high-priority lead, not a theorem smuggled
in from pattern matching.

## 6. What would remain even after the phase factorization

If (5.5) is proved, the simultaneous conditions $E=0$ and
$\Theta=0$ reduce (3.8) to



$$
t_{s+1}G_h(s_*)=2\Delta_-(h,s_*)\pmod p,    \tag{6.1}
$$



where



$$
t_{s+1}=(-1)^{s+1}\binom{3s}{s+1}.          \tag{6.2}
$$



All rational denominators displayed in (6.1) are row units.  The remaining
quantity (6.2) is a central/incomplete-beta boundary coordinate for which
this package supplies no rational phase formula or independence theorem.
No all-prime theorem excluding (6.1), and no collective height bound strong
enough for the Route-1 gap, is proved here.  Thus even the conjectural
factorization (5.2) identifies rather than removes the final arithmetic
obstruction.

## 7. Finite replay and rate ledger

The deterministic scan covers all 22,934 actual rows with
$p\leq2000$.  It finds



$$
\begin{array}{c|r}
\Theta=0&22\\
E=0&58\\
\Theta=E=0&0.
\end{array}                                                    \tag{7.1}
$$



These counts are **EXACT_FINITE_ONLY**.  In particular, the empty
intersection in (7.1) is not used to infer sparsity, density zero, or an
all-prime theorem.

The exact decomposition (3.8) supplies no bound for the prime log-mass of
rows on which its incomplete-binomial coordinate takes the required value.
Therefore



$$
\boxed{\text{new unconditional linear log rate}=0,\qquad
        \text{new divisibility exponent}=0.}                  \tag{7.2}
$$



## 8. Reproducibility and labels

The companion standard-library checker verifies (3.5)--(3.9) exactly on a
formal rational grid, replays the degree and leading-coefficient theorem,
checks (5.1)--(5.4) exactly through the declared $h$-bound, and
reruns the complete finite row scan.  Canonical and replay JSON are intended
to be byte-identical.

Classification:

* **PROVED:** the all-$h$ identities (3.5)--(4.3) and the scoped no-go for
  the displayed polynomial Gosper-antidifference/direct-resultant ansatz.
* **EXACT_FINITE_ONLY:** (5.2)--(5.4) for $h\leq80$ and (7.1) for
  $p\leq2000$.
* **OPEN:** an all-$h$ telescoping certificate for (5.2); exclusion
  or useful collective control of (6.1); any positive Route-1 rate or
  radical saving.
