> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 231 — the second (j=1) resonance as one Frobenius coefficient

Date: 2026-08-31

## 1. Scope and verdict

Retain the actual (j=1) parameterization



$$
p=2r+6s+3,\qquad r=2h,\qquad h,s\geq1,              \tag{1.1}
$$



and Item 223's two transfer scalars $\Delta_+,\Delta_-$.  Put



$$
\epsilon=(-1)^{(p-1)/2},\qquad a=2s+4.              \tag{1.2}
$$



This item gives a closed coefficient formula for Item 228's second
Frobenius invariant.  Define



$$
D(x)={1\over(1-x)^{r+1}(1+x^2)^{2s}},               \tag{1.3}
$$





$$
R(x)=2r+4s-1+(r+1)x-(r+8s)x^2,
 \qquad g_n=[x^n]R(x)D(x).                           \tag{1.4}
$$



The main exact result is



$$
\boxed{\Delta_+=g_a,\qquad
 \Psi=-2\epsilon\bigl(g_a+2g_{a+p}\bigr)\pmod p.}  \tag{1.5}
$$



Consequently every original common-log collision must satisfy



$$
\boxed{g_a=2\Delta_-\ne0,\qquad
        g_{a+p}=-\Delta_-\pmod p.}                  \tag{1.6}
$$



Equivalently, with the first Frobenius defect



$$
H=g_{a+p}-g_a,              \tag{1.7}
$$



the second condition is



$$
\boxed{H=-3\Delta_-\pmod p.}          \tag{1.8}
$$



Statements (1.5)--(1.8) are **PROVED for every actual row**.  They remove
the propagated auxiliary scalars $\rho_0,\rho_1$ from Item 228 and retain
the actual seed through the explicit coefficients $g_a,g_{a+p}$.

The Frobenius defect has an exact same-row reciprocal sum, proved below.
Its Gosper reduction leaves a second incomplete-binomial partial sum whose
binomial parameter is fixed at the original $s$.  Item 232's recurrence
for the diagonal sequence $S_n$ does not control this coordinate.

**EXACT FINITE ONLY.**  The 22 Item 223 survivors through $p\leq2000$
all fail the second coefficient equation in (1.6).  No simultaneous
$\Theta=E=0$ row, hence no triple $\Theta=\Psi=E=0$ row, occurs through
that bound.  The phase-Gosper comparison described in Section 7 is exact
only for $h\leq20$.

**OPEN.**  There is no all-prime exclusion, weighted exceptional-prime
bound, or all-$h$ phase resultant.  The new unconditional Route-1 rate
and divisibility exponent are zero.

## 2. The coefficient solution behind the first transfer

Item 223's normalized recurrence solution $v_t$, with



$$
(v_0,v_1,v_2)=(1,1,-1),                \tag{2.1}
$$



has generating function $F(x)=\sum_{t\geq0}v_tx^t$ satisfying



$$
x(1-x)(1+x^2)F'(x)+Q(x)F(x)=R(x),             \tag{2.2}
$$



where $R$ is (1.4) and



$$
Q=2r+4s-1-(r+4s-1)x+(2r+1)x^2-(r+1)x^3.        \tag{2.3}
$$



The integrating factor from Item 223 is



$$
\mu(x)={x^{2r+4s-1}\over(1-x)^r(1+x^2)^{2s-1}}.             \tag{2.4}
$$



Since



$$
{\mu R\over x(1-x)(1+x^2)}
 =x^{2r+4s-2}R(x)D(x),                             \tag{2.5}
$$



coefficientwise integration gives the exact formal identity



$$
\boxed{F(x)=(1-x)^r(1+x^2)^{2s-1}
     \sum_{n\geq0}{g_n\over 2r+4s-1+n}x^n.}       \tag{2.6}
$$



The first two denominators in (2.6) divisible by $p$ occur at



$$
2r+4s-1+a=p,\qquad
 2r+4s-1+(a+p)=2p.                                \tag{2.7}
$$



Thus the first terminal numerator is $g_a$.  Expanding (1.4) with
$D_n=[x^n]D$ gives



$$
g_a=(2r+4s-1)D_{2s+4}+(r+1)D_{2s+3}
                         -(r+8s)D_{2s+2},          \tag{2.8}
$$



which is exactly Item 223's closed formula for $\Delta_+$.

## 3. Eliminating $\rho_0,\rho_1$

Let



$$
f=-4\epsilon              \tag{3.1}
$$



be the first terminal source.  Item 228 propagates three components:
the fixed forcing, the initial scalar $\lambda$, and the first-pole free
mode.  At the second terminal the free component vanishes by the exact
support inequality in Item 228, leaving $(\rho_0,\rho_1,0)$.

Delete the first pole term in (2.6), and compare the resulting regularized
coefficient solution with Item 228's fixed-forcing and initial-line
columns.  If



$$
W(x)=(1-x)^r(1+x^2)^{2s-1}=\sum_kw_kx^k,
 \qquad k=t-a,                                      \tag{3.2}
$$



direct substitution of the deleted term $g_ax^aW/p$ gives the retained
left-side forcing



$$
-g_a(w_k-w_{k+1}+w_{k+2}-w_{k+3}).                \tag{3.3}
$$



Item 228's fixed column has the same expression with $g_a$ replaced by
$f$.  Thus their initial triples, deleted-pole forcing, and recurrence
agree after cross multiplication by $g_a$ and $f$.  Any discrepancy at the
first pole is a multiple of the free mode
$(1-x)^r(1+x^2)^{2s-1}$, which is identically absent from the second
terminal covector.  At the next pole, (2.6) therefore gives



$$
\boxed{g_a\rho_0+f\rho_1=f g_{a+p}\pmod p.}           \tag{3.4}
$$



This comparison uses no division by $g_a$, so it remains valid on rows
where $g_a=0$.  It can also be checked directly by substituting the
deleted coefficient $g_a/p$ into the exact regularized recurrence: the
four-term forcing is the same finite difference of the free-mode
coefficients as in Item 228.

Item 228 defines



$$
\Psi=g_a(\rho_0-2\epsilon)-4\epsilon\rho_1.       \tag{3.5}
$$



Substitution of (3.1) and (3.4) into (3.5) proves



$$
\Psi=f g_{a+p}-2\epsilon g_a
      =-2\epsilon(g_a+2g_{a+p}),                  \tag{3.6}
$$



which is (1.5).  If $\Theta=0$, Item 223 gives
$g_a=2\Delta_-\ne0$.  Equation (3.6) is then equivalent to
$g_{a+p}=-\Delta_-$, proving (1.6)--(1.8).

## 4. Cartier/Frobenius form of the defect

In $\mathbb F_p[[x]]$, put



$$
\Pi(x)=(1-x)^{p-r-1}(1+x^2)^{p-2s}.             \tag{4.1}
$$



Frobenius gives



$$
D(x)={\Pi(x)\over(1-x^p)(1+x^{2p})}.             \tag{4.2}
$$



Because $a<p$ and $a+p<2p$, only the terms $1+x^p$ of the
denominator inverse contribute.  Hence



$$
g_{a+p}=g_a+[x^{a+p}]R(x)\Pi(x),                 \tag{4.3}
$$



and therefore



$$
\boxed{H=[x^{a+p}]R(x)\Pi(x).}         \tag{4.4}
$$



This is the exact first Cartier/Frobenius defect of the lower terminal
coefficient.  It is not a guessed interpolation in $h$ or $s$.

The polynomial $\Pi$ is palindromic: $p-r-1$ is even because
$p$ is odd and $r$ is even.  Its degree is
$3p-r-4s-1$.  Reversing $R$, and using (1.1), transforms (4.4) into



$$
H=[x^{p+r}]\bigl(-(r+8s)+(r+1)x+(2r+4s-1)x^2\bigr)\Pi(x).    \tag{4.5}
$$



## 5. Exact same-row reciprocal sum

Set



$$
t_j=(-1)^j\binom{2s+j-1}{j},\qquad
 J={p+r-1\over2}=3h+3s+1,                         \tag{5.1}
$$



and abbreviate



$$
A=2r+4s-1,\qquad B=r+1,\qquad C=-(r+8s).         \tag{5.2}
$$



Expanding (4.5), complementing the $(1-x)$-binomial, and using



$$
\binom{p-2s}{j}\equiv(-1)^j\binom{2s+j-1}{j}\pmod p          \tag{5.3}
$$



gives the exact formula



$$
\boxed{\begin{aligned}
H={}&C\sum_{j=r+1}^{J}t_j\binom{2j-r-1}{r}
   +B\sum_{j=r}^{J}t_j\binom{2j-r}{r}\\
 &+A\sum_{j=r}^{J-1}t_j\binom{2j-r+1}{r}\pmod p.
\end{aligned}}                                                \tag{5.4}
$$



All upper and lower limits in (5.4) come from the ordinary support of the
two factors in $\Pi$; there are no discarded endpoint terms.

Define the degree-$r$ polynomial



$$
P^\uparrow_{h,s}(j)=C\binom{2j-r-1}{r}
                     +B\binom{2j-r}{r}
                     +A\binom{2j-r+1}{r}.          \tag{5.5}
$$



Then (5.4) is equivalently



$$
H=\sum_{j=r}^{J}t_jP^\uparrow_{h,s}(j)
       -A t_J\binom{2J-r+1}{r}.                   \tag{5.6}
$$



## 6. What Gosper reduction leaves

Use the same operator as Item 229,



$$
\mathcal L_sU(j)=-(2s+j)U(j+1)-jU(j).             \tag{6.1}
$$



There is a unique decomposition



$$
P^\uparrow_{h,s}(j)=c^\uparrow_h(s)
                   +\mathcal L_sR^\uparrow_h(s,j),
 \qquad\deg_jR^\uparrow_h\leq2h-1.               \tag{6.2}
$$



Since



$$
t_j\mathcal L_sU(j)=(j+1)t_{j+1}U(j+1)-jt_jU(j),              \tag{6.3}
$$



equations (5.6) and (6.2) give



$$
\boxed{\begin{aligned}
H={}&c^\uparrow_h(s)\,\mathcal T_{h,s}
 +(J+1)t_{J+1}R^\uparrow_h(s,J+1)
 -rt_rR^\uparrow_h(s,r)\\
 &-A t_J\binom{2J-r+1}{r},                         \tag{6.4}
\end{aligned}}
$$



where the surviving same-row coordinate is



$$
\boxed{\mathcal T_{h,s}=\sum_{j=r}^{J}t_j
 =\sum_{j=r}^{3h+3s+1}(-1)^j\binom{2s+j-1}{j}.}    \tag{6.5}
$$



This is the precise limitation of the second-resonance reduction.

Item 232 proves a recurrence for



$$
S_n=\sum_{j=0}^{n}(-1)^j\binom{2n+j-1}{j}.        \tag{6.6}
$$



That recurrence changes both the endpoint and the binomial parameter from
$n$ to $n+1$.  In (6.5), the endpoint changes from $s$ to $J$ but
the binomial parameter remains the original row value $s$.  Thus
$\mathcal T_{h,s}$ is a difference of fixed-$s$ partial sums, not
$S_J-S_{r-1}$ in Item 232's diagonal sequence.  Inserting the adjacent
identity would therefore mix different summands and different rows.  The
checker records the first exact mismatch:



$$
(p,h,s,J)=(13,1,1,7),\qquad
 \sum_{j=0}^{J}(-1)^j\binom{2s+j-1}{j}=-4,
 \quad S_J=-57044.                                  \tag{6.7}
$$



Accordingly Item 232 supplies no legitimate same-row scalar elimination of
(6.4).

## 7. Phase comparison: finite evidence only

At the row phase



$$
s_*=-{4h+3\over6},           \tag{7.1}
$$



the checker solves both exact polynomial Gosper systems over $\mathbb Q$.
For every $1\leq h\leq20$, it finds



$$
c^\uparrow_h(s_*)=c_h(s_*),            \tag{7.2}
$$



where $c_h$ is Item 229's lower residual.  This is an
**EXACT FINITE PATTERN**, not an all-$h$ theorem.

If one formally sets the common residual to zero, (6.4) has only the two
endpoint terms.  The endpoint ratio is exactly reducible on an actual row:



$$
{t_J\over t_{s+1}}
 \equiv(-1)^{h+1}{(3s+1)_{h+1}\over(s+2)_{h+1}}\pmod p.       \tag{7.3}
$$



To prove (7.3), write the factorial ratio for $t_J/t_{s+1}$, complement
the two factorials nearest $p$ with Wilson's theorem, and cancel.  Every
factor in the denominator of (7.3) is strictly between 0 and $p$.

Let $L_h,d_h,U_h,F_h$ denote, respectively, the lower endpoint
coefficient, $\Delta_-$, the upper coefficient of $t_J$, and the fixed
lower endpoint in (6.4), all evaluated at $s_*$.  Eliminating
$t_{s+1},t_J$ from



$$
t_{s+1}L_h=2d_h,\qquad t_JU_h=F_h-3d_h             \tag{7.4}
$$



produces the natural rational phase scalar



$$
K_h=2d_hU_h(-1)^{h+1}{(3s_*+1)_{h+1}\over(s_*+2)_{h+1}}
          -L_h(F_h-3d_h).                           \tag{7.5}
$$



For every admissible $h\leq20$, the checker computes the reduced
numerators of $E_h^*$ and $K_h$.  After their gcd is removed, every
remaining prime divisor of the $E_h^*$ numerator is at most $4h+3$.
This is again **EXACT FINITE ONLY**.  It suggests that this most direct
phase endpoint eliminant may be redundant after Item 222's condition, but
no divisibility pattern is promoted to a symbolic factorization or a
prime-uniform no-go.

The all-$h$ statements still missing are:

1. a proof of (7.2);
2. a proof relating $c_h(s_*)$ to $E_h^*$ for every admissible $h$;
3. a unit-localized all-$h$ gcd or resultant theorem for $E_h^*$ and
   (7.5);
4. control of the incomplete coordinate (6.5) when the residual does not
   vanish.

## 8. Finite replay, kept separate

The proof replay covers every 479 actual row with $p\leq251$.  It checks
(1.5), (4.3)--(4.5), and the full reciprocal sum (5.4).  The row stream has
SHA-256
`81891b3f86a830cfbbcc286c65c4a48d8a9e95a9b8b1fae2376fdda3a2953ae3`.
This is a replay of identities proved above, not their logical basis.

Separately, the actual-row census through $p\leq2000$ has



$$
\begin{array}{c|r}
\text{actual rows}&22934\\
\Theta=0\text{ with nonzero transfers}&22\\
\text{failures of }g_{a+p}=-\Delta_-\text{ on those 22}&22\\
\Theta=\Psi=0&0\\
\Theta=E=0&0\\
\Theta=\Psi=E=0&0.
\end{array}                                                   \tag{8.1}
$$



The 22-row stream has SHA-256
`51cb124d5f719e9e68321c6ffd8c04210f35a9d2eae88f5df79ace713c9c61cd`.
Every count in (8.1) is **EXACT FINITE ONLY** and yields no density
inference.

## 9. Route-1 ledger

The full $j=1$ cell would have conditional removable mass $1/6$ per
$m$.  Item 231 replaces Item 228's long propagation by an explicit
Cartier coefficient and exposes the exact surviving same-row boundary
coordinate.  It does not classify the simultaneous zeros of (1.6), nor
bound their prime-log mass.  Therefore



$$
\boxed{\text{new unconditional linear log rate}=0,\qquad
        \text{new divisibility exponent}=0.}                  \tag{9.1}
$$



## 10. Reproducibility and labels

From the archive root, run

```text
python scripts/item231_j1_second_phase_coefficient_certificate.py --output results/item231_j1_second_phase_coefficient_certificate.json
python scripts/item231_j1_second_phase_coefficient_certificate.py --output results/item231_j1_second_phase_coefficient_certificate.replay.json
```

The checker uses only Python 3.11+ standard-library exact integer,
`Fraction`, polynomial, and finite-field arithmetic.  Its portable manifest
pins Items 222, 223, 228, and the corrected Item 229 checker.

**PROVED:** (1.5)--(1.8), the coefficient solution (2.6), the cross relation
(3.4), the Cartier defect (4.4), the reciprocal sum (5.4), and the precise
Item 232 scope distinction.

**EXACT FINITE ONLY:** the identity replay through $p\leq251$, the
survivor/triple census through $p\leq2000$, and the phase-Gosper/gcd
patterns through $h\leq20$.

**OPEN:** all-$h$ phase identities and gcd/resultants; all-prime or
weighted control of simultaneous $\Theta=\Psi=0$; any positive Route-1
rate or radical saving.
