> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Route-1 adversary: bounded-jet indistinguishability and the exact sequential mass ledger

Date: 2026-08-28

## 1. Scope and verdict

This note independently audits frozen items 143, 149, 151, and 160.  It was
developed and checked independently before archival.

The conclusions are deliberately scoped.

1. **PROVED (actual coordinates).**  No uniform $p^2$-lift follows from
   the top prime-power layer, first-Cartier rank zero, or a vanishing
   rank-two determinant.  The exact actual-coordinate rows
   $(m,p)=(3,3),(9,13),(4,7)$ have $v_p(c_m)=1$.
2. **PROVED (limitation theorem).**  In the full rational-differential class
   satisfying the same separable-pole, pole-order, and polynomial-degree
   hypotheses as the top-layer Cartier lemma, first-level Cartier data do
   not determine the next determinant digit.  More strongly, for every
   fixed precision $J$, two pairs can agree globally modulo $p^J$, have
   exactly the same finite-pole principal parts, and have determinant
   valuations $J$ and $J+k$.  Thus no law based only on bounded local
   jets at fixed $p$-adic precision can certify the next digit uniformly.
3. **PROVED (sequential normalization).**  There is an exact primewise
   formula for the exponent in $c_m\Delta_m g_m$.  It validates genuine
   overlap of a prime among all three factors, but also proves
   

$$
c_m\Delta_m g_m\mid |V_m|q_N.
$$


   Every sequential cancellation is therefore chargeable to the original
   coefficient product; none is an independent reuse of Cartier mass.
4. **PROVED (weighted target).**  After the rank-one divisor is booked once,
   the exact remaining sequential weight needed at the optimal beta scale is
   greater than
   

$$
1.0196329836694317938803064012400587396\ldots
   \quad\text{per }6m.
$$


   This weight may mix new internal radicals, higher internal powers,
   $\Delta_m$, and $g_m$, but every term must use the sequentially
   primitive coordinates.
5. **OPEN.**  The explicit limitation family below is not the special
   one-parameter family
   $u^{6m}Q^{-4m-1-s}dx$.  It proves insufficiency of first-level or
   bounded-jet data alone; it does not prove that no deeper identity of the
   actual family exists.  A growing-precision integral formula remains a
   legitimate route.

## 2. Frozen normalization and actual counterexamples

The audited normalization is



$$
X_m=D_m^\sharp A_m,\qquad Y_m=D_m^\sharp B_m,
\qquad U_m=X_m/G_m,\quad V_m=Y_m/G_m,
$$





$$
c_m=\gcd(U_m,V_m).
$$



For $p\in\mathcal H_m\cup\mathcal Z_m$, let
$q_p=p^{e_p}$ and
$\delta_{m,p}=\mathbf1_{p\in\mathcal P_m}$.  Item 160 correctly derives



$$
v_p(U_m)=v_p(q_pA_m)-\delta_{m,p},
\qquad v_p(V_m)\ge e_p+1.                       \tag{2.1}
$$



Consequently, for $1\le r\le e_p+1$,



$$
p^r\mid c_m
\iff v_p(q_pA_m)\ge r+\delta_{m,p}.             \tag{2.2}
$$



The following exact rows show that the first unproved digit need not vanish.



$$
\begin{array}{c|c|c|c|c}
(m,p)&\text{mechanism}&v_p(U_m)&v_p(V_m)&v_p(c_m)\\ \hline
(3,3)&q_p=9=p^2&1&3&1\\
(9,13)&p\in\mathcal P_m\text{ and }G_m\text{ removed}&1&2&1\\
(4,7)&\Delta_{q,s}=0\pmod7&1&2&1
\end{array}                                                   \tag{2.3}
$$



Thus each of the following proposed laws is false for the actual frozen
coordinates:



$$
e_p\ge2\Longrightarrow p^2\mid c_m,
$$





$$
p\in\mathcal P_m\cap\mathcal H_m
\Longrightarrow p^2\mid c_m,
$$





$$
\Delta_{q_p,s_p}=0\pmod p\Longrightarrow p^2\mid c_m.          \tag{2.4}
$$



These are exact counterexamples, not finite-frequency inferences.

## 3. A bounded-jet limitation theorem

Fix an odd prime $p$, an integer $e\ge1$, and $q=p^e$.  For a
rational differential write



$$
\mathcal Z_q(\omega)=(qR(\omega),L(\omega),E(\omega)),          \tag{3.1}
$$



using the item-143 endpoint basis



$$
\int_0^1\omega=R(\omega)+{L(\omega)\over4}\log2
                         +{E(\omega)\over8}\pi.
$$



Consider the three explicit $\mathbb Z_{(p)}$-differentials



$$
\rho_q=x^{q-1}dx,\qquad
\lambda={dx\over4(1+x)},\qquad
\epsilon={dx\over2(1+x^2)}.                                  \tag{3.2}
$$



Direct integration gives



$$
\mathcal Z_q(\rho_q)=(1,0,0),\qquad
\mathcal Z_q(\lambda)=(0,1,0),\qquad
\mathcal Z_q(\epsilon)=(0,0,1).                               \tag{3.3}
$$



The poles are among $-1,\pm i$, whose common pole polynomial has
discriminant $-16$, a $p$-unit.  Their pole orders are one, and the only
polynomial term has degree $q-1\le pq-2$.  Hence these forms satisfy the
structural hypotheses of the top prime-power endpoint lemma.

### Theorem 3.1 (first-level data allow arbitrary lift valuation)

For integers $r,s\ge1$, put



$$
\omega_0=\rho_q+\lambda+\epsilon,
$$





$$
\omega_1^{(r,s)}=(1+p^r)\rho_q+\lambda+(1+p^s)\epsilon.        \tag{3.4}
$$



Then the two reduced forms are equal modulo $p$, so all their first-level
Cartier images, local jets, and endpoint vectors modulo $p$ agree.  Yet



$$
qA=L_1(qR_0)-L_0(qR_1)=-p^r,
$$





$$
8B=L_1E_0-L_0E_1=-p^s.                                       \tag{3.5}
$$



In particular the first-level datum is compatible with every prescribed
positive value of $v_p(qA)$.  If $s$ is chosen larger than $r$, the
rational-coordinate minor is the limiting one after the usual clearing.

**Proof.**  Equations (3.3) give



$$
\mathcal Z_q(\omega_0)=(1,1,1),\qquad
\mathcal Z_q(\omega_1^{(r,s)})=(1+p^r,1,1+p^s).
$$



The reductions coincide.  Taking the two displayed minors gives (3.5)
exactly. $\square$

### Theorem 3.2 (the post-$G_m$ rank-zero digit is also arbitrary)

Put



$$
\omega_0^{(0)}=p(\rho_q+\lambda+\epsilon),
$$





$$
\omega_1^{(0;r,s)}=p(\rho_q+\lambda+\epsilon)
                    +p^r\rho_q+p^s\epsilon.                    \tag{3.6}
$$



Both reduced endpoint vectors vanish.  Nevertheless



$$
v_p(qA)=r+1,\qquad v_p(8B)=s+1.                                \tag{3.7}
$$



After one squarefree rank-zero factor is removed, the surviving rational
valuation is exactly $r$.  If $s\ge r$, the other cleared coordinate is
deeper, so the post-$G_m$ content valuation is also exactly $r$.  Thus
first-level rank zero is compatible both with one sharp post-$G_m$ digit
($r=1$) and with arbitrarily many digits.

The proof is the same determinant calculation as in Theorem 3.1.

### Theorem 3.3 (fixed-precision bounded jets cannot certify the next digit)

Fix $J,k\ge1$, and fix $S>J+k$.  Compare the two ordered pairs



$$
(\omega_0,\omega_1^{(J,S)})
\quad\text{and}\quad
(\omega_0,\omega_1^{(J+k,S)}).                                \tag{3.8}
$$



They agree globally modulo $p^J$.  Their finite-pole principal parts agree
even integrally, because their difference is



$$
(p^J-p^{J+k})x^{q-1}dx,                                       \tag{3.9}
$$



a polynomial differential.  Therefore any fixed collection of local jets,
at every finite pole and at infinity, reduced modulo $p^J$, is identical
for the two pairs.  But



$$
v_p(qA)=J\quad\text{for the first pair},
\qquad
v_p(qA)=J+k\quad\text{for the second}.                         \tag{3.10}
$$



Hence data at fixed precision $p^J$ cannot decide whether the determinant
has an additional digit beyond $J$.

This theorem applies a fortiori to candidates based on only finitely many
first-level Cartier coefficients or a bounded number of mod-$p$ Laurent
jets.  It does **not** rule out a formula whose precision or number of
coefficients grows with $m,p$, or a special recurrence tying the actual
two forms together over $\mathbb Z_p$.

## 4. Exact primewise ledger for $c_m\Delta_mg_m$

Let



$$
u_p=v_p(U_m),\qquad v_p^*=v_p(V_m),\qquad
\kappa_p=\min(u_p,v_p^*)=v_p(c_m).                             \tag{4.1}
$$



After primitive reduction,



$$
\beta_p=v_p(b_m)=v_p^*-\kappa_p.                              \tag{4.2}
$$



For the primitive beta pair put



$$
t_p=v_p(q_N).
$$



Then the matching gcd has exponent



$$
d_p=v_p(\Delta_m)=\min(\beta_p,t_p).                           \tag{4.3}
$$



Let $P^*=b_0p_N-\varepsilon q_0a_m$.  The final exponent is exactly



$$
\gamma_p=v_p(g_m)=
\begin{cases}
\min\{\beta_p,v_p(P^*)\},&\beta_p=t_p>0,\\
0,&\text{otherwise}.
\end{cases}                                                    \tag{4.4}
$$



Therefore



$$
\boxed{
v_p(c_m\Delta_mg_m)=\kappa_p+d_p+\gamma_p.}                    \tag{4.5}
$$



The equality condition in (4.4) is not optional.  If
$0<t_p<\beta_p$, then the normalized first term in $P^*$ is divisible
by $p$ and the second is a unit.  If
$0<\beta_p<t_p$, the roles reverse.  In either unequal case $P^*$ is a
unit, so $\gamma_p=0$.

The cases can be displayed as follows:



$$
\begin{array}{c|c|c|c}
\text{condition}&d_p&\gamma_p&v_p(c\Delta g)\\ \hline
\beta_p=0\text{ or }t_p=0&0&0&\kappa_p\\
0<t_p<\beta_p&t_p&0&\kappa_p+t_p\\
0<\beta_p<t_p&\beta_p&0&\kappa_p+\beta_p\\
\beta_p=t_p=r>0&r&\min(r,v_p(P^*))&\kappa_p+r+\gamma_p
\end{array}                                                    \tag{4.6}
$$



Two useful exact safeguards follow.

First,



$$
d_p+\gamma_p\le2\min(\beta_p,t_p).                            \tag{4.7}
$$



Second,



$$
\kappa_p+d_p+\gamma_p\le v_p^*+t_p.                           \tag{4.8}
$$



Globally, the latter is the divisor theorem



$$
\boxed{c_m\Delta_mg_m\mid |V_m|q_N.}                          \tag{4.9}
$$



There is also a one-line proof: $|V_m|=c_m\Delta_mb_0$,
$q_N=\Delta_mq_0$, and $g_m\mid\Delta_m$, so



$$
|V_m|q_N=c_m\Delta_m^2b_0q_0
$$



is divisible by $c_m\Delta_mg_m$.

Equation (4.9) explains the legitimate triple overlap at $(m,N,p)=(6,4,7)$:



$$
(v_7(c_6),v_7(\Delta_6),v_7(g_6))=(1,1,1).
$$



Those three copies cancel three distinct stages, and their product divides
$|V_6|q_4$.  But replacing the primitive coefficient $b_6$ by raw
$|V_6|$ gives the wrong value



$$
\gcd(|V_6|,q_4)=1001\ne91=\Delta_6.                            \tag{4.10}
$$



Thus overlap is legitimate; reuse of an unnormalized coordinate is not.

## 5. Exact weighted mass sufficient after every normalization

Let $\mathcal H_m$ be the item-149 rank-one set and put



$$
R_{1,m}=\sum_{p\in\mathcal H_m}\log p.
$$



The proved limit is



$$
{R_{1,m}\over6m}\longrightarrow
r_1={-4\log2+6\log3-3\over6}
=0.136514168294812818450423822617\ldots .                      \tag{5.1}
$$



Define the exact **sequential excess weight**



$$
\mathcal W_{m,N}
=\sum_p\left(
v_p(c_m)-\mathbf1_{p\in\mathcal H_m}
+d_p+\gamma_p
\right)\log p.                                                \tag{5.2}
$$



Every summand is nonnegative because item 149 proves
$v_p(c_m)\ge1$ on $\mathcal H_m$.  Equations (4.5) and (5.2) give the
exact identity



$$
\boxed{
\log(c_m\Delta_mg_m)=R_{1,m}+\mathcal W_{m,N}.}                \tag{5.3}
$$



This is the correct ledger after all sequential normalizations.  It includes
without duplication:

- additional powers on rank-one primes;
- every internal prime outside $\mathcal H_m$, including new radicals;
- the primitive matching gcd $\Delta_m$;
- the final primitive content $g_m$, only under (4.4).

Suppose



$$
{N\log N\over6m}\longrightarrow\theta.
$$



The frozen positive-matching height ledger requires



$$
{\log(c_m\Delta_mg_m)\over6m}
>\max\{h-\theta,h-d+\theta\}+o(1).                             \tag{5.4}
$$



Combining (5.1)--(5.4), a sufficient exact weighted statement is



$$
\liminf_{m\to\infty}{\mathcal W_{m,N_m}\over6m}
>\max\{h-\theta,h-d+\theta\}-r_1.                             \tag{5.5}
$$



The right side is minimized at $\theta=d/2$.  The certified optimal
threshold is therefore



$$
\boxed{
\liminf{\mathcal W_{m,N_m}\over6m}
>h-{d\over2}-r_1
=1.0196329836694317938803064012400587396\ldots .}              \tag{5.6}
$$



The replay encloses the last constant in an interval of width $10^{-52}$:



$$
\begin{split}
1.019632983669431793880306401240058739632901069045296317679092339358102
&<h-d/2-r_1\\
&<1.019632983669431793880306401240058739632901069045296417679092339358102.
\end{split}                                                    \tag{5.7}
$$



If one refuses to use any matching gain or new radical, the older pure
higher-power target



$$
\mathcal M_m^{\rm pow}
=\sum_p\max\{v_p(c_m)-1,0\}\log p
$$



with $\liminf\mathcal M_m^{\rm pow}/(6m)>$ the right side of (5.6) is
sufficient.  It is not necessary: (5.2) is the weaker and exact mixed target.

A theorem asserting only one additional digit on every rank-one prime would
add merely another $r_1$, leaving



$$
1.01963298366943179\ldots-r_1
=0.88311881537461897\ldots
$$



still unfilled.  The target is weighted mass, not the existence of an
isolated or even universal second digit.

## 6. Dwork/Hasse--Witt boundary

The bounded-jet theorem explains why a first-level singular comparison
matrix cannot by itself control its order of singularity.  On the rank-one
locus the two selected images already span one line; on the rank-zero locus
they vanish; and on the rank-two zero locus the selected $2\times2$ minor
is singular.  Any step requiring its inverse is unavailable precisely there.

This does **not** identify that selected matrix with an ambient Hasse--Witt
matrix.  The pole divisor stays separable for odd $p$, and no frozen
package constructs a smooth proper family with an integral Frobenius-stable
lattice whose Hasse--Witt matrix is the endpoint comparison matrix.  Thus:

- **PROVED:** first-level singularity alone has no lift implication;
- **OPEN:** a separately constructed higher Frobenius/crystalline object may
  contain growing-precision information special to the actual family;
- **INVALID:** treating $e_p$ characteristic-$p$ Cartier iterations as
  $e_p$ digits, or invoking a matrix inverse on its singular locus.

## 7. Replay and status ledger

Run

```text
python scripts/modp2_bounded_jet_sequential_mass_check.py
```

The checker pins the item-143, item-149, item-151, and item-160 sources and
three exact certificates.  It then:

1. replays the three actual sharp $p^2$ counterexamples;
2. checks 12 explicit arbitrary-valuation differential models;
3. checks six fixed-precision indistinguishable pairs;
4. exhausts 2,401 small primewise sequential-exponent states and verifies
   (4.7)--(4.8);
5. replays $(m,N)=(6,4)$, including (4.9)--(4.10);
6. recomputes $r_1$ and the certified interval (5.7).

Final classification:

- **PROVED:** Theorems 3.1--3.3, the exact sequential ledger (4.5), divisor
  safeguard (4.9), and weighted sufficiency target (5.6).
- **EXPERIMENTAL:** the frozen finite frequencies of lifted and sharp rows;
  they are not used in any theorem here.
- **OPEN:** a growing-precision formula for the actual lifted digit
  $\eta_{m,p}$, and any positive asymptotic lower bound for the exact
  sequential weight (5.2).

Nothing in this note proves the irrationality or transcendence of
$e+\pi$.
