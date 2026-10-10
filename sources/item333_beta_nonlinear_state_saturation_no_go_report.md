> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 333 — all-modulus saturation of nonlinear beta load invariants

Checked: 2026-09-01 (Beijing time)

## 1. Strict verdict and capacity admission

Retain



$$
q_0=q_1=1,
\qquad
q_n=(4n-2)q_{n-1}+q_{n-2}\quad(n\ge2),
\tag{1.1}
$$



and, for $n\ge5$, put



$$
A=4n-2,
\qquad
a=q_{n-1},\quad b=q_n,\quad c=q_{n-2},
\qquad m=n-2.
\tag{1.2}
$$



Item 316 makes a centered half-bound failure equivalent to one exact
canonical target.  In the sign chamber



$$
\sigma=\operatorname{sgn}(E_m)\in\{\pm1\},
\tag{1.3}
$$



Item 330 identifies its single defect as



$$
\boxed{\Delta_\sigma=\sigma E_{m+1}-a.}
\tag{1.4}
$$



Thus, after Item 330 closed the linear divided-quotient tower, the smallest
genuinely transverse load proposal is to form nonlinear polynomials in the
all-depth suffix loads $N_j$ or first quotients $J_j$, and then demand a
new congruence or a higher valuation.

This proposal passes admission before it is analyzed.  On the exact target,
Item 330 gives



$$
J_0=aG_0,
\qquad
a=7G_0+G_1,
\qquad
0<G_1<G_0,
\tag{1.5}
$$



and hence



$$
\boxed{\frac{a^2}{8}<J_0<\frac{a^2}{7}.}
\tag{1.6}
$$



Consequently $\log J_0=2\log a+O(1)=2n\log n+O(n)$.  Nonlinear load
expressions are not rejected as thin merely by their integer height.  This
is a raw-size admission only; height is not booked as prime mass.

The admitted class nevertheless has an exact global closure.

> **PROVED — INTEGRAL TARGET-COORDINATE THEOREM.**  Fix $n\ge5$ and
> $\sigma\in\{\pm1\}$.  In the polynomial ring
>
> 

$$
> \mathcal A=\mathbb Z[d_1,\ldots,d_m],
> \tag{1.7}
>
$$


>
> form every prefix, suffix-load, and quotient state by the exact Item
> 323/330 recurrences, with $d_i$ in place of the digits.  Then
> $\Delta_\sigma$ is an integral affine coordinate of $\mathcal A$.
> Explicitly, there is an affine unimodular change of variables
>
> 

$$
> \mathcal A=\mathbb Z[d_1,\ldots,d_{m-2},\Delta_\sigma,z].
> \tag{1.8}
>
$$



In particular,



$$
\boxed{
\mathcal A/(\Delta_\sigma)
\cong
\mathbb Z[d_1,\ldots,d_{m-2},z].}
\tag{1.9}
$$



The target ideal is prime, radical, and saturated over $\mathbb Z$; it is
not hiding a second algebraic component.

> **PROVED — ALL-MODULUS NONLINEAR SATURATION.**  For every integer
> $M\ge2$, the kernel of formal target specialization modulo $M$ is
> exactly
>
> 

$$
> \boxed{
> \ker\!\left(
> \mathcal A\longrightarrow
> (\mathbb Z/M\mathbb Z)
> [d_1,\ldots,d_{m-2},z]
> \right)
> =(M,\Delta_\sigma).}
> \tag{1.10}
>
$$



Therefore, after substituting the complete all-depth load state, every
polynomial congruence in $N_j,J_j$, prefix states, and fixed continuants
which follows **formally** from the original target has the exact form



$$
\boxed{F=\Delta_\sigma C+MD}
\tag{1.11}
$$



in the digit ring.  This holds at arbitrary degree, arbitrary depth,
arbitrary composite modulus, and every prime power.

This proves a broad scoped no-go.  Recurrence algebra alone cannot turn a
nonlinear load polynomial, determinant, resultant, or formal higher
valuation into a second target condition.  Such an expression is either a
universal recurrence syzygy, an old-defect multiple, or it is not forced by
Item 316 at all.

The theorem does **not** close genuinely arithmetic statements about the
canonical digit box: sign or size inequalities, nonvanishing of the
cofactor $C$, an exact gcd or valuation distribution, floors and absolute
values, or canonical complement redigitization.  Those would use input
beyond formal polynomial elimination and remain open.

The centered half-bound is not proved.  Booking and beta capacity reduction
remain zero.

## 2. Universal prefix and load algebra

Set



$$
w_1=7,
\qquad
w_j=4j+2\quad(2\le j\le m),
\qquad
w_{m+1}=A.
\tag{2.1}
$$



Let $d_1,\ldots,d_m$ be algebraically independent variables.  Extend the
word by $d_{m+1}=0$, and define



$$
E_0=0,
\qquad
E_1=d_1,
\tag{2.2}
$$





$$
E_{j+1}=w_{j+1}E_j+E_{j-1}+(-1)^j d_{j+1}
\qquad(1\le j\le m).
\tag{2.3}
$$



Every $E_j$ is a linear polynomial in the digits.  Fix $\sigma$, and
put



$$
k_j=\sigma E_j,
\qquad
\kappa=\sigma E_m,
\qquad
\epsilon=(-1)^n\sigma.
\tag{2.4}
$$



Define the fixed suffix continuants and polynomial loads by



$$
H_m=1,\quad H_{m+1}=0,
\qquad
N_m=N_{m+1}=0,
\tag{2.5}
$$





$$
H_{j-1}=w_{j+1}H_j+H_{j+1},
\tag{2.6}
$$





$$
N_{j-1}=w_{j+1}N_j+N_{j+1}+d_{j+1}
\qquad(1\le j\le m),
\tag{2.7}
$$



and



$$
J_j=\kappa H_j+\epsilon N_j.
\tag{2.8}
$$



Thus every all-depth state under consideration belongs to $\mathcal A$.
Fixed continuants, $a,b,A$, and the sign chamber are coefficients, not
new variables.  Any polynomial construction from finitely many or all of
the states has a well-defined pullback to $\mathcal A$.

For an actual Item-316 target, the variables specialize to its unique
canonical digits, $\sigma$ is their actual sign, and



$$
E_{m+1}=\sigma a.
\tag{2.9}
$$



Hence $\Delta_\sigma=0$.  Conversely, after retaining Item 316's window,
small-error, and sign hypotheses, $\Delta_\sigma=0$ is exactly the old
target.  No arbitrary formal point of $\mathcal A$ is promoted to an
actual beta counterexample.

## 3. The two top coefficients are unimodular

The last inhomogeneous step in (2.3) gives



$$
[d_m]E_m=(-1)^{m-1},
\qquad
[d_{m-1}]E_m=(-1)^m w_m.
\tag{3.1}
$$



Because $d_{m+1}=0$,



$$
E_{m+1}=AE_m+E_{m-1}.
\tag{3.2}
$$



Therefore



$$
[d_{m-1}]E_{m+1}=(-1)^m(Aw_m+1),
\tag{3.3}
$$





$$
[d_m]E_{m+1}=(-1)^{m-1}A.
\tag{3.4}
$$



Put



$$
s=\sigma(-1)^m,
\qquad
u=s(Aw_m+1),
\qquad
v=-sA.
\tag{3.5}
$$



These are precisely the coefficients of $d_{m-1},d_m$ in
$\Delta_\sigma$.  They satisfy the explicit Bezout identity



$$
\boxed{su+sw_m v=1.}
\tag{3.6}
$$



This identity is uniform in $n$, in both sign chambers, and survives
reduction modulo every prime.  In particular, the gradient of the target
defect cannot vanish in any characteristic.

Write



$$
\Delta_\sigma
=L(d_1,\ldots,d_{m-2})+u d_{m-1}+v d_m-a,
\tag{3.7}
$$



where $L$ is the contribution of the lower variables.  Let



$$
\alpha=s,
\qquad
\beta=sw_m,
\tag{3.8}
$$



so that $\alpha u+\beta v=1$, and define



$$
t=\Delta_\sigma,
\qquad
z=-\beta d_{m-1}+\alpha d_m.
\tag{3.9}
$$



The linear matrix on the two top variables is



$$
\begin{pmatrix}
u&v\\
-\beta&\alpha
\end{pmatrix},
\qquad
\det=\alpha u+\beta v=1.
\tag{3.10}
$$



The inverse is integral and explicit:



$$
d_{m-1}
=\alpha\bigl(t-L+a\bigr)-vz,
\tag{3.11}
$$





$$
d_m
=\beta\bigl(t-L+a\bigr)+uz.
\tag{3.12}
$$



Equations (3.9)-(3.12) prove (1.8) without invoking a field, dividing by a
moving integer, or excluding any prime.

## 4. Exact integral and modular target ideals

Under the automorphism in Section 3, the target ideal becomes the
coordinate ideal $(t)$.  Hence



$$
\mathcal A/(\Delta_\sigma)
\cong
\mathbb Z[d_1,\ldots,d_{m-2},z].
\tag{4.1}
$$



The right side is an integral domain and is torsion-free over
$\mathbb Z$.  It follows that $(\Delta_\sigma)$ is prime and radical,
and that



$$
rF\in(\Delta_\sigma),\quad 0\ne r\in\mathbb Z
\quad\Longrightarrow\quad
F\in(\Delta_\sigma).
\tag{4.2}
$$



Thus no integer content can conceal a second target component.

For every $M\ge2$, the same unimodular transformation gives



$$
\mathcal A/(M,\Delta_\sigma)
\cong
(\mathbb Z/M\mathbb Z)
[d_1,\ldots,d_{m-2},z].
\tag{4.3}
$$



The quotient map has kernel exactly $(M,\Delta_\sigma)$, proving
(1.10).  No primality of $M$ is used.  In particular, (4.3) applies to



$$
M=b,
\qquad
M=Q\mid b,
\qquad
M=p^r,
\qquad
M=2^r,
\tag{4.4}
$$



whenever such a modulus is declared in a candidate mechanism.

The statement is about formal polynomial identities in the quotient ring,
not about coincidental equality of polynomial functions on a small finite
set.  This distinction prevents a finite residue table from being promoted
to a theorem.

## 5. Pullback theorem for all-depth nonlinear load states

Let $\mathcal S$ be a polynomial ring whose symbols represent any chosen
collection of



$$
N_j,\ J_j,\ E_j,\ k_j,\ R_j,\ L_j,
\tag{5.1}
$$



together with fixed suffix continuants and fixed beta coefficients.  The
recurrences define a substitution homomorphism



$$
\pi:\mathcal S\longrightarrow\mathcal A.
\tag{5.2}
$$



Take any polynomial $F\in\mathcal S$, of arbitrary degree and involving
arbitrary depths.  There are exactly three cases.

1. If $\pi(F)=0$, then $F$ is a universal recurrence syzygy.  It holds
   for every digit word and carries no target information.
2. If $\pi(F)\ne0$ but its vanishing is a formal consequence of the exact
   target, then

   

$$
\boxed{\pi(F)=\Delta_\sigma C}
   \tag{5.3}
$$



   for a unique polynomial $C\in\mathcal A$.
3. Otherwise $F$ is not forced by Item 316 and needs a genuinely new
   arithmetic theorem before it can be used.

Modulo $M$, the corresponding dichotomy is



$$
\boxed{\pi(F)=\Delta_\sigma C+MD.}
\tag{5.4}
$$



The same conclusion holds for a portfolio $F_1,\ldots,F_r$: after
pullback, every formally forced row lies in the one ideal
$(M,\Delta_\sigma)$.  Increasing the degree, adjoining more depths, or
forming determinants and resultants does not increase the formal target
codimension.

For a numerical off-target word, (5.3) gives



$$
v_p\!\left(\pi(F)\right)
=v_p(\Delta_\sigma)+v_p(C)
\tag{5.5}
$$



when neither side is zero.  The first term is the old defect.  Controlling
the second term requires new arithmetic about $C$; it is not supplied by
the target or the load recurrences.  Equation (5.5) is why the present
theorem closes formal valuation lifts but deliberately does not claim to
close exact valuation distribution.

## 6. Scoped no-go and what would count as transverse progress

The preceding sections prove



$$
\boxed{
\begin{array}{c}
\text{Item-316 target}
+\text{ all-depth linear load recurrences}
+\text{ polynomial algebra}\\[2mm]
\Longrightarrow
\text{only the saturated ideal }(M,\Delta_\sigma).
\end{array}}
\tag{6.1}
$$



Thus none of the following, by itself, creates a fresh target condition:

* a nonlinear polynomial in one or many $N_j$ or $J_j$;
* a determinant or resultant formed from several depths;
* reduction of such an expression modulo $b$, a divisor of $b$, or a
  prime power;
* repeating the construction at higher polynomial degree; or
* claiming a higher formal valuation solely from the target recurrence.

A successful continuation must add a theorem not present in (6.1), for
example:



$$
C\not\equiv0\pmod p
\tag{6.2}
$$



on the actual canonical family, a sign/size contradiction, a controlled gcd
distribution, or a non-polynomial redigitization statement.  Such a theorem
could be genuinely transverse.  It is not ruled out here.

This is stronger than checking individual quadratic or cubic candidates:
the degree and the number of depths are unrestricted.  It is also narrower
than a no-go for all arithmetic of the loads.  The word "formal" is
essential in every conclusion.

## 7. Actual-family and capacity audit

The actual-family bridge is exact:



$$
\text{centered half-bound failure}
\Longrightarrow
\text{Item-316 canonical word}
\Longrightarrow
\Delta_\sigma=0.
\tag{7.1}
$$



Within Item 316's declared window, the final implication reverses.  Thus the
old defect in (1.4) is neither an ambient surrogate nor a modified seed.

The formal coordinate construction allows noncanonical integer points when
proving the polynomial-ring theorem.  Those points certify algebraic
saturation only.  They are not asserted to satisfy digit bounds, the Markov
condition, the half-language, or the beta target.  Any theorem using those
inequalities lies outside the scoped no-go.

The raw candidate class passed the size screen by (1.6).  Nevertheless,
(1.10) proves that its recurrence-only modular portfolio has no target
codimension beyond $\Delta_\sigma$.  Therefore its incremental capacity is
zero.  Fixed suffix content, repeated depths, degrees, and prime powers may
not be rebooked.

For a proper de-overlapped target $Q\mid b$, (1.10) only says that a formal
load congruence belongs to $(Q,\Delta_\sigma)$.  It does not give a lower
bound for the centered residue modulo $Q$, a zero-density theorem, or a
weighted return cover.  Item 282's product baseline remains separate.

## 8. Strict labels

### PROVED

* The raw-height admission (1.5)-(1.6), without converting height into mass.
* The exact top-coefficient formulas (3.3)-(3.4).
* The uniform Bezout identity (3.6) in both sign chambers.
* The explicit affine unimodular target coordinate (3.9)-(3.12).
* The prime, radical, and integer-saturated target ideal (4.1)-(4.2).
* The all-composite-modulus kernel theorem (4.3).
* The all-depth nonlinear-state pullback dichotomy (5.3)-(5.4).
* The actual-family implication and capacity separation in Section 7.

### PROVED SCOPED NO-GO

* Recurrence-only polynomial nonlinear invariants of $N_j,J_j$, at any
  degree and any collection of depths, add no formal target codimension.
* Formal modular and prime-power valuation lifts of those polynomials reduce
  to the old saturated ideal $(M,\Delta_\sigma)$.
* This no-go does not include canonical inequalities or arithmetic of the
  cofactor after the old defect is removed.

### EXACT FINITE ONLY

* The deterministic replay's declared coefficient, affine-coordinate,
  state-substitution, and modular-control rows.
* Formal target lattice points used in the replay are noncanonical algebraic
  controls and are never promoted to actual beta candidates.

### OPEN

* The exclusion $\Delta_\sigma\ne0$ for every Item-316 candidate and the
  centered half-bound.
* Nonvanishing, sign, size, gcd, or exact valuation theorems for a cofactor
  $C$ on the actual canonical family.
* Non-polynomial operations, including floors, absolute values, minimum
  valuations, and canonical complement redigitization.
* A proper-target residue lower bound, weighted zero-density theorem, or beta
  capacity reduction.
* Route 1 and every conclusion about $e+\pi$.

### BOOKING



$$
\boxed{
\text{new beta capacity reduction}=0,
\qquad
\text{new Route-1 rate}=0.}
\tag{8.1}
$$



No canonical, master, status, checkpoint, or research-log file is edited by
this work package.

## 9. Deterministic replay

From the archive root:

~~~text
python work/item333_beta_nonlinear_state_saturation_no_go_certificate.py ^
  --output work/item333_beta_nonlinear_state_saturation_no_go_certificate.replay.json
~~~

The checker uses only the Python standard library and exact integer
arithmetic.  It performs no half-bound scan, no exceptional-prime scan, and
promotes no bounded row.
