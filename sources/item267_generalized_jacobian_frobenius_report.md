> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 267: generalized-Jacobian recognition of the punctured $j=2$ period

Checked: 2026-08-31 (Beijing time)

## 1. Verdict and admission test

Let



$$
E:\quad Y^2=X^3-\frac12,
\qquad
D=E\cap\{X^3=1\},
\qquad
U=E\setminus D.                                             \tag{1.1}
$$



The divisor $D$ is a reduced degree-six divisor over $\mathbf Q$.
Put



$$
\omega_a={X^a\over X^3-1}{dX\over Y}\quad(0\le a\le2),
\qquad
\eta={dX\over Y},
\qquad
\xi={X\,dX\over Y}.                                         \tag{1.2}
$$



The fixed $p\equiv5\pmod6$ logarithmic differential requested in this
item is



$$
\omega_{\log}=\omega_1={X\over X^3-1}{dX\over Y}.             \tag{1.3}
$$



This item gives an exact positive recognition and an equally exact
capacity obstruction.

> **PROVED — fixed open-curve and 1-motive recognition.**  The five
> classes in (1.2) form the hyperelliptic-odd part of
> $H^1_{\mathrm{dR}}(U)$.  Up to the standard duality convention, this
> is the de Rham realization of the fixed Picard 1-motive
> 

$$
> M_U^-=[L^-\xrightarrow{u}E],\qquad
> L^-=\bigoplus_{k=0}^2\mathbf Z\,d_k,\qquad
> u(d_k)=2P_k,                                               \tag{1.4}
>
$$


> where $P_k=(\zeta^k,\beta)$, $\zeta\ne1$, $\zeta^3=1$,
> $\beta^2=1/2$, and
> 

$$
> d_k=[P_k]-[-P_k].
>
$$


> Equivalently, it is the odd isogeny factor of the generalized
> Jacobian of $E$ with modulus $D$.

> **PROVED — the pair $(H_q,h_q)$ is a fixed-motive Cartier
> coordinate pair.**  For $p=6q+5$,
> 

$$
> \boxed{
> H_q=[\eta]\,\mathcal C(\omega_1),\qquad
> h_q=-[\eta]\,\mathcal C(\xi),}                              \tag{1.5}
>
$$


> where $[\eta]$ means the coefficient of $\eta$ in the fixed frame
> (1.2), after the residue term is retained.  Consequently
> 

$$
> \boxed{
> H_{q-\delta}
> =[\eta]\,\mathcal C(\omega_1+K_\delta\xi).}                  \tag{1.6}
>
$$


> The full Item-251 period is obtained by replacing $K_\delta$ by
> $D_r$ and adjoining one trivial constant line.  Thus the cutoff and
> the full affine gate are row-dependent matrix coefficients of one
> fixed mixed object; they are not scalar Frobenius traces.

> **PROVED — exact puncture divisor and non-unit direction.**  The residue
> divisor of $\omega_1$ is
> 

$$
> \boxed{
> \operatorname{res}(\omega_1)
> ={1\over3\beta}
> \left(d_0+\zeta^2d_1+\zeta d_2\right).}                    \tag{1.7}
>
$$


> The only principal odd direction in $L^-$ is
> 

$$
> \mathbf Z(d_0+d_1+d_2),
>
$$


> and
> 

$$
> d\log{Y-\beta\over Y+\beta}=3\beta\,\omega_2.                \tag{1.8}
>
$$


> Hence $\omega_2$, not $\omega_1$, is the algebraic-unit
> logarithm.  No nonzero multiple of the residue character in (1.7) is
> the divisor of a unit on $U_{\overline{\mathbf Q}}$.

> **PROVED — the remaining 1-motive direction is non-torsion.**  Over
> $\mathbf Q(\sqrt2,\zeta)$, the isomorphism
> 

$$
> (X,Y)\longmapsto(x,y)=(2X,2\sqrt2\,Y)
>
$$


> sends $E$ to
> 

$$
> E':\quad y^2=x^3-4
>
$$


> and $P_0$ to $P=(2,2)$.  The point $P$ is non-torsion.
> Therefore the two nonconstant cubic residue characters, including
> (1.7), are genuinely non-torsion elliptic third-kind directions.

> **PROVED, SHARPLY SCOPED SCALAR/CONJUGACY NO-GO.**  Although $H_q$
> is an exact coefficient in the fixed global frame, it is not an
> isomorphism invariant of the mod-$p$ Cartier module.  For
> $p=6q+5$, put
> 

$$
> \widetilde\omega_0=\omega_0+{H_q\over\epsilon}\eta,
> \qquad
> \widetilde\xi=-h_q^{-1}\xi.
>
$$


> Then
> 

$$
> \boxed{
> \begin{aligned}
> \mathcal C\widetilde\omega_0&=\epsilon\omega_1,&
> \mathcal C\omega_1&=\epsilon\widetilde\omega_0,\\
> \mathcal C\omega_2&=\epsilon\omega_2,&
> \mathcal C\eta&=0,&
> \mathcal C\widetilde\xi&=\eta.
> \end{aligned}}                                             \tag{1.9}
>
$$


> Thus the abstract Cartier module has a normal form independent of
> $H_q$ and $h_q$.  Scalar traces, determinants, eigenvalues, and
> conjugacy invariants cannot recover the actual cutoff coordinate.
> This does **not** erase the fixed-frame period or the endpoint
> functional.

The underlying 1-motive is therefore elliptic-logarithmic rather than
unit-logarithmic.  But the congruence



$$
H_{q-\delta}=0
$$



is not proved equivalent to any basis-free elliptic-Wieferich condition.
Calling it “Wieferich-type” may describe the hoped-for extra arithmetic
vanishing, but no actual if-and-only-if with divisibility of $P$ modulo
$p^2$, or with a $p$-adic elliptic logarithm, is obtained here.

The admission test fails.  The vector $\omega_1+K_\delta\xi$, and then
the full-gate vector with $D_r$, moves with $r$; the endpoint
functional does not descend to de Rham cohomology; and ordinary Frobenius
invariants discard the relevant coefficient.  Therefore



$$
\boxed{\text{new unconditional Route-1 rate}=0,\qquad
\text{new ordinary-\(j=2\) capacity reduction}=0.}            \tag{1.10}
$$



Every bounded replay below is **EXACT FINITE ONLY** and is used only to
check identities.

## 2. Generalized Jacobian and odd Picard 1-motive

The divisor is the finite étale scheme



$$
D=\operatorname{Spec}
\mathbf Q[X,Y]/(X^3-1,Y^2-1/2).                               \tag{2.1}
$$



For the reduced modulus $D$, the generalized Jacobian fits into



$$
1\longrightarrow
T_D\longrightarrow J_D\longrightarrow E\longrightarrow0,
\qquad
T_D={\operatorname{Res}_{D/\mathbf Q}\mathbf G_m\over\mathbf G_m}.
                                                                    \tag{2.2}
$$



The hyperelliptic involution



$$
\iota(X,Y)=(X,-Y)
$$



acts on this sequence.  Since $2$ is invertible over $\mathbf Q$, its
plus and minus parts are defined in the isogeny category.  If



$$
D_0=D/\iota=\operatorname{Spec}\mathbf Q[X]/(X^3-1),
$$



then, up to this harmless $2$-isogeny, the odd torus is the norm-one
torus



$$
T^-=\ker\!\left(
\operatorname{Res}_{D/\mathbf Q}\mathbf G_m
\xrightarrow{N_{D/D_0}}
\operatorname{Res}_{D_0/\mathbf Q}\mathbf G_m\right),          \tag{2.3}
$$



of dimension three.  The odd generalized-Jacobian factor is an extension
of $E$ by $T^-$, and its first de Rham realization has dimension



$$
2\dim E+\dim T^-=2+3=5.                                      \tag{2.4}
$$



This is exactly the dimension of the frame (1.2).

The dual Picard description is more explicit.  Over the splitting field
$K=\mathbf Q(\sqrt2,\zeta)$, choose



$$
\beta={1\over\sqrt2},\qquad
P_k=(\zeta^k,\beta),\qquad -P_k=(\zeta^k,-\beta).              \tag{2.5}
$$



The odd degree-zero boundary lattice is



$$
L^-=\bigoplus_{k=0}^2\mathbf Z\,d_k,
\qquad d_k=[P_k]-[-P_k].                                     \tag{2.6}
$$



On a genus-one curve, the Abel-Jacobi image of a degree-zero divisor is
the group-law sum of its points.  Therefore



$$
u(d_k)=P_k-(-P_k)=2P_k,                                      \tag{2.7}
$$



which proves (1.4).  The construction is Galois-equivariant and hence
descends from the displayed split form to the fixed 1-motive over
$\mathbf Q$.

The residue exact sequence



$$
0\longrightarrow H^1_{\mathrm{dR}}(E)
\longrightarrow H^1_{\mathrm{dR}}(U)
\xrightarrow{\operatorname{res}}
H^0(D,\mathcal O_D)_0
\longrightarrow0,
\qquad
H^0(D,\mathcal O_D)_0
=\ker\!\left(\operatorname{Tr}_{D/\mathbf Q}\right).          \tag{2.8}
$$



restricts on the odd part to dimensions $2$, $5$, and $3$.
The residue vectors of $\omega_0,\omega_1,\omega_2$ are the three
cubic characters, while $\eta,\xi$ span the compact kernel.  This is
the de Rham realization of (1.4), up to duality.

## 3. Puncture divisor, units, and the non-torsion point

At $P_{\alpha,\beta'}=(\alpha,\beta')\in D$,



$$
\operatorname{Res}_{P_{\alpha,\beta'}}\omega_a
={\alpha^{a-2}\over3\beta'}.                                \tag{3.1}
$$



For $a=1$, choose $\alpha=\zeta^k$ and $\beta'=\pm\beta$.
Equation (3.1) becomes exactly (1.7).

There is one visible principal odd divisor.  The horizontal lines
$Y=\pm\beta$ meet $E$ at the three corresponding punctures, so



$$
\operatorname{div}{Y-\beta\over Y+\beta}
=d_0+d_1+d_2.                                               \tag{3.2}
$$



Differentiating gives



$$
\begin{aligned}
d\log{Y-\beta\over Y+\beta}
&={2\beta\,dY\over Y^2-\beta^2}\\
&={3\beta X^2\over Y(X^3-1)}\,dX
=3\beta\,\omega_2,
\end{aligned}                                                \tag{3.3}
$$



which proves (1.8).

To prove that there are no other odd unit directions, transport the
points to



$$
E':y^2=x^3-4.
$$



Let



$$
\rho(x,y)=(\zeta x,y),\qquad P=(2,2).
$$



Then $P_k$ maps to $\rho^kP$, and $\rho$ satisfies



$$
1+\rho+\rho^2=0
$$



in the CM endomorphism ring.  The first multiples of $P$ are



$$
2P=(5,-11),\qquad
3P=\left({106\over9},{1090\over27}\right).                    \tag{3.4}
$$



If $P$ were torsion, then $3P$ would be a finite rational torsion
point.  The Nagell-Lutz theorem for $y^2=x^3-4$ would force its
coordinates to be integral, contradicting (3.4).  Hence $P$ is
non-torsion.

Now suppose that $\sum n_kd_k$ is principal.  Equations (2.7) and the
transport give



$$
[2(n_0+n_1\rho+n_2\rho^2)]P=O.                               \tag{3.5}
$$



A nonzero CM endomorphism has finite kernel, so it cannot kill the
non-torsion point $P$.  Thus



$$
n_0+n_1\rho+n_2\rho^2=0.
$$



Since the only integral relation among $1,\rho,\rho^2$ is
$1+\rho+\rho^2=0$,



$$
\boxed{\ker(u|_{L^-})=\mathbf Z(d_0+d_1+d_2).}                \tag{3.6}
$$



The residue vector



$$
(1,\zeta^2,\zeta)
$$



in (1.7) is not proportional to $(1,1,1)$.  Therefore it does not lie
in the unit direction, even after extending scalars.  Equivalently, with



$$
\nu_k=\beta\,{dX\over(X-\zeta^k)Y},
$$



one has



$$
\omega_1=\sum_{k=0}^2{1\over3\zeta^k\beta}\,\nu_k,             \tag{3.7}
$$



and each $\nu_k$ is a third-kind differential attached to the
non-torsion divisor $d_k$.  This proves the elliptic-logarithmic
recognition in its exact algebraic sense.

## 4. Exact Cartier matrix coefficients

Let $p\ge5$ be a good prime, put



$$
n={p-1\over2},\qquad
\epsilon=\left({2\over p}\right),\qquad
h_j={(1/2)_j\over j!\,2^j},\qquad
H_j=\sum_{i=0}^jh_i.                                      \tag{4.1}
$$



The absolute Frobenius pullback on ordinary differentials is zero in
characteristic $p$.  The nonzero mod-$p$ operator used here is the
Cartier operator on the de Rham realization; no characteristic-zero
Frobenius lift is silently chosen.

For $p=6q+5$, Item 263 proves



$$
\begin{aligned}
\mathcal C\omega_0&=\epsilon\omega_1,&
\mathcal C\omega_1&=\epsilon\omega_0+H_q\eta,\\
\mathcal C\omega_2&=\epsilon\omega_2,&
\mathcal C\eta&=0,&
\mathcal C\xi&=-h_q\eta.
\end{aligned}                                                \tag{4.2}
$$



Since $h_q$ is a $p$-unit on every actual row, equations (1.5) and
(1.9) follow immediately.

For $p=6q+1$, the companion phase is



$$
\begin{aligned}
\mathcal C\omega_0&=\epsilon\omega_0+(H_q-h_q)\eta,&
\mathcal C\omega_1&=\epsilon\omega_1,\\
\mathcal C\omega_2&=\epsilon\omega_2,&
\mathcal C\eta&=h_q\eta,&
\mathcal C\xi&=0.
\end{aligned}                                                \tag{4.3}
$$



Thus the pair is again recovered:



$$
h_q=[\eta]\,\mathcal C(\eta),\qquad
H_q=h_q+[\eta]\,\mathcal C(\omega_0).                         \tag{4.4}
$$



Both phases therefore come from the same fixed mixed realization.

## 5. Cutoff and full affine gate as moving matrix coefficients

The two phases share



$$
m=q-\delta,\qquad H_m=H_q-K_\delta h_q.                       \tag{5.1}
$$



For $p=6q+5$, define



$$
v_\delta^{(5)}=\omega_1+K_\delta\xi.
$$



Equation (4.2) gives



$$
\mathcal Cv_\delta^{(5)}
=\epsilon\omega_0+(H_q-K_\delta h_q)\eta,                     \tag{5.2}
$$



which proves (1.6).

For $p=6q+1$, define



$$
v_\delta^{(1)}=\omega_0+(1-K_\delta)\eta.
$$



Equation (4.3) gives



$$
\mathcal Cv_\delta^{(1)}
=\epsilon\omega_0+(H_q-K_\delta h_q)\eta.                     \tag{5.3}
$$



Thus the cutoff is a single coefficient in both phases, but the input
vector moves with $\delta$.

For the full Item-251 period, put



$$
D_r=K_\delta+c_\delta\Pi_r.
$$



Replace $K_\delta$ by $D_r$ in (5.2)--(5.3) and call the resulting
vector $v_r$.  Then



$$
\boxed{
A_s=(-1)^m\left\{
\epsilon[\eta]\,\mathcal C(v_r)-1\right\}.}                    \tag{5.4}
$$



The remaining coordinates are



$$
Z=B_s\left({9\kappa_r\over2}A_s-\tau_{r,s}\right),
\qquad
G_\nu=f_\nu Z+U_\nu.                                         \tag{5.5}
$$



Adjoining a one-dimensional trivial object makes the constant in (5.4)
and every affine expression in (5.5) into linear matrix coefficients.
This is an exact actual-family representation.  It does not remove the
separate $f_0=f_1=0$ branch, and it does not turn the moving family
$v_r$ into one fixed scalar trace.

## 6. Conjugacy invariants and the endpoint obstruction

The frame change in (1.9) is legal because $\epsilon^2=1$ and
$h_q\ne0$.  It proves that, on the $p\equiv5$ phase, every abstract
odd Cartier module is isomorphic to the same normal form for fixed
$\epsilon$.  The entries $H_q$ and $h_q$ are periods of the chosen
global frame, not conjugacy invariants.

There is a parallel statement on the $p\equiv1$ phase.  Put



$$
\lambda=H_q-h_q.
$$



If $h_q\ne\epsilon$, then



$$
\widetilde\omega_0
=\omega_0-{\lambda\over h_q-\epsilon}\eta
$$



satisfies



$$
\mathcal C\widetilde\omega_0=\epsilon\widetilde\omega_0.       \tag{6.1}
$$



Only on the resonant locus $h_q=\epsilon$ can the zero/nonzero status
of $\lambda$ survive as a Jordan-extension invariant of this
two-dimensional block.  Even there, the full gate uses
$H_q-D_rh_q$, not merely $\lambda$, so no gate exclusion follows.

The conjugacy reduction must not be confused with evaluation of the
actual finite sum.  For $p=6q+5$, the endpoint functional of Item 260
satisfies



$$
\Lambda_p(\mathcal L(X^{-1}))=-\epsilon\ne0.                  \tag{6.2}
$$



For $p=6q+1$, the two exact endpoint defects $d_0,d_1$ of Item 261
satisfy



$$
30d_0+12d_1=\epsilon\ne0.                                   \tag{6.3}
$$



Hence the finite punctured functional does not descend to the abstract
de Rham class in either phase.  A $p$-dependent splitting can remove a
matrix entry from a conjugacy normal form while changing the canonical
representative on which the endpoint functional is evaluated.  The
actual period therefore remains; only the proposed scalar shortcut is
ruled out.

## 7. Why no algebraic-unit or Wieferich capacity theorem follows

Equation (3.3) identifies the complete algebraic-unit direction:



$$
\mathbf G_m\text{-logarithm}\quad\longleftrightarrow\quad\omega_2.
$$



Equation (3.6) proves that $\omega_1$ has no such reduction.  Its
1-motive extension is controlled by a non-torsion CM orbit of
$P=(2,2)$, so complex and $p$-adic realizations naturally involve
elliptic logarithms or third-kind elliptic periods.

That recognition is not yet an elliptic-Wieferich theorem.  A basis-free
elliptic-Wieferich condition would normally be formulated using an
integral $p$-adic realization, a formal-group logarithm, or divisibility
of a multiple of $P$ modulo $p^2$.  The present gate is instead the
mod-$p$, fixed-frame coefficient



$$
[\eta]\,\mathcal C(v_r),
$$



which can move under a change of de Rham splitting as shown in Section 6.
No exact equivalence with a standard elliptic-Wieferich condition is
proved.  Ordinary Weil bounds control eigenvalues or scalar traces and
are silent about this removable off-diagonal coordinate.

Finally, $r$ ranges through a positive-mass cell.  The coefficients
$K_\delta$, $D_r$, and then the affine vectors in (5.5) all move with
the row.  Fixed dimension of $M_U^-$ does not bound the number or
log-prime weight of zeros of these moving linear functionals.  A fixed
$r$ ray still has only $O(\log M)=o(M)$ weight at global index $M$,
but that is the previously known fixed-ray geometry and cannot be summed
over linearly many $r$'s.

Therefore the exact generalized-Jacobian representation supplies no
all-prime exclusion, no weighted zero-density theorem, and no positive
linear capacity saving.  The booking remains zero.

## 8. Reproducible checks and strict labels

The standard-library checker accompanying this report performs no search
for exceptional zero primes.  It verifies:

1. the rational group law
   $2P=(5,-11)$ and
   $3P=(106/9,1090/27)$;
2. the cubic-character residue vectors, the partial fractions in (3.7),
   and the algebraic-unit identity (3.3);
3. the integral kernel calculation for the boundary lattice on a bounded
   coefficient box;
4. the coefficient-level Cartier formulas and the normal-form changes
   through a bounded prime range;
5. the moving cutoff matrix-coefficient identities for every bounded
   admissible phase row.

### PROVED

- The generalized-Jacobian and Picard 1-motive recognition
  (2.1)--(2.8).
- The residue divisor (1.7), exact unit direction (1.8), and kernel
  theorem (3.6).
- Non-torsion of $P=(2,2)$ and the non-torsion elliptic third-kind
  nature of $\omega_1$.
- The fixed-motive coordinate formulas (1.5)--(1.6) and the full-gate
  representation (5.4)--(5.5).
- The $p\equiv5$ conjugacy normal form (1.9), the
  $p\equiv1$ nonresonant splitting (6.1), and the endpoint non-descent
  distinction.
- Failure of the positive-linear-capacity admission test.

### EXACT FINITE ONLY

- Every bounded row count and identity count in the certificate.  No
  bounded nonoccurrence is promoted to an all-prime statement.

### OPEN

- An integral/crystalline formula identifying the canonical-frame gate
  with a basis-free $p$-adic elliptic logarithm.
- Any actual if-and-only-if between the gate and an elliptic-Wieferich
  congruence modulo $p^2$.
- Uniform or weighted control when $r$ moves through the positive-mass
  cell.
- Route 1 and every conclusion about $e+\pi$.

### BOOKING

No new Route-1 rate and no new ordinary-$j=2$ capacity reduction are
booked.

## 9. Portable package

~~~text
sources/item267_generalized_jacobian_frobenius_report.md
scripts/item267_generalized_jacobian_frobenius_certificate.py
results/item267_generalized_jacobian_frobenius_certificate.json
results/item267_generalized_jacobian_frobenius_certificate_replay.json
results/item267_generalized_jacobian_frobenius_ledger.json
manifests/item267_generalized_jacobian_frobenius_manifest.json
results/item267_generalized_jacobian_frobenius_hashes.sha256
~~~

The principal frozen dependencies are Items 251, 260, 261, 262, and 263.
