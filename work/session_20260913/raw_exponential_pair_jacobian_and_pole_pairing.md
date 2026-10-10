> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The exponential-pair Jacobian: exact determinant and a vanishing pole pairing

Date: 2026-09-13. Original bounded continuation by audit_sources.
Independent review passed: raw_exponential_pair_jacobian_independent_review.md.
The all-degree étaleness question remains unresolved.
This note does not establish that the exponential pair is étale
at every actual four-equation root. It gives a fully normalized
determinant for that remaining question, explains why one natural
pole/concomitant argument is identically uninformative there, and
supplies a single exact counterexample to a weaker proposed lemma.

## 1. The specific remaining Jacobian

Retain $d\ge2$, $D=1+z^2$, $s=3d+2$, $p>3d+3$, and
the operators $L,P=L^{[1]}$ from
raw_extremal_four_accessory_equations.md. Work over
$A=\mathbb Z[1/d!]$, a field of the allowed characteristic, or
a $p$-adic ring where indicated.

The monic polynomial $B^*(z;\beta,\gamma)$ is defined for every
parameter pair by the upper $d$ equations
$[z^k]PB^*=0$, $2\le k\le d+1$. Its coefficients lie in
$A[\beta,\gamma]$. Exactly as in the actual finite algebra,


$$
E_1=d![z]PB^*,\qquad E_0=d![1]PB^*.
$$


Set


$$
\mathcal J_d=
\det\begin{pmatrix}
\partial_\beta E_1&\partial_\gamma E_1\\
\partial_\beta E_0&\partial_\gamma E_0
\end{pmatrix}\in\mathbb Z[\beta,\gamma].
\tag{1}
$$


The desired statement is that $\mathcal J_d$ never vanishes at
an actual common zero of $E_1,E_0,R_0,R_1$ in characteristic
$p>3d+3$. Full rank of the four-by-two Jacobian does not imply
this particular two-row assertion.

## 2. An exact square determinant, with no hidden factorial

For the rest of this section write $B=B^*$ and define


$$
U=[z(\partial+1)-d]B,\qquad V=(\partial+1)B.
$$


Form the square matrix $\mathcal W_d$ whose columns are the
coefficient vectors of


$$
Pz^{d-1},Pz^{d-2},\ldots,P1,\ U,\ V,
$$


and whose rows, in this exact order, are


$$
[z^{d+1}],[z^d],\ldots,[z^2],[z],[1].
$$


All these polynomials have degree at most $d+1$. Then the
identity, valid as a polynomial identity over $A$, is


$$
\boxed{\mathcal J_d=(-1)^d d!\det\mathcal W_d.}
\tag{2}
$$



Indeed the upper-left $d$-by-$d$ block $T$ is triangular
with diagonal $-1,-2,\ldots,-d$: the coefficient of
$z^{m+2}$ in $Pz^m$ is $m-d$. Differentiate the upper
equations defining $B^*$. The two resulting coefficient
vectors of $\partial_\beta B^*,\partial_\gamma B^*$ are
$-T^{-1}$ times the upper entries of $U,V$.
Consequently the lower Schur complement of $\mathcal W_d$
is the Jacobian matrix in (1) divided by $d!$.
Taking determinants gives


$$
\det\mathcal W_d=(-1)^d d!\,\mathcal J_d/(d!)^2,
$$


which is (2). This proof uses no equation $E_1=E_0=0$.

At an exponential-pair root, singularity of (1) is equivalently
the existence of a nonzero $(u,v)$ and a polynomial
$\dot B$ of degree at most $d-1$ with


$$
P\dot B+uU+vV=0.
\tag{3}
$$


The map $P:\mathcal P_{d-1}\to\mathcal P_{d+1}$ is injective,
by its highest coefficient $m-d$. Thus (3) is a precise
intersection of the parameter directions with its image,
not a second homogeneous polynomial solution of $P$.

## 3. The actual two-dimensional cokernel and its recurrence

For any $f\in\mathcal P_{d+1}$, subtract the unique
$Pg$, $g\in\mathcal P_{d-1}$, killing its coefficients
of degrees $2,\ldots,d+1$. Write the remainder
$\ell_1(f)z+\ell_0(f)$. These are the canonical two dual
functionals, with


$$
(\ell_0(1),\ell_0(z))=(1,0),\qquad
(\ell_1(1),\ell_1(z))=(0,1).
$$


They exist over every allowed ring because their only pivots
are $-1,\ldots,-d$. In particular


$$
\boxed{\mathcal J_d=(d!)^2
\det\begin{pmatrix}
\ell_1(U)&\ell_1(V)\\
\ell_0(U)&\ell_0(V)
\end{pmatrix}.}
\tag{4}
$$



There is an explicit recurrence requiring no polynomial
reconstruction of $A$ or $C$. For either functional write
$\mu_k=\ell(z^k)$, set negative-index moments to zero, and
for $0\le m<d$ use


$$
\begin{aligned}
0={}&(m-d)\mu_{m+2}+a_m\mu_{m+1}+b_m\mu_m\\
&+c_m\mu_{m-1}+e_m\mu_{m-2},\\
a_m={}&2m(m-2d)+\beta-d(d-1),\\
b_m={}&m(m-1)(m-3d)+(m-d)\beta+m+\gamma
+2d^2(d-1)-3d-2,\\
c_m={}&m(\gamma+2m-6d-6),\\
e_m={}&m(m-1)(m-3d-4).
\end{aligned}
\tag{5}
$$


This is simply $\ell(Pz^m)=0$; each next moment divides by
the unit $d-m$. Formula (4), with (5), is the exact remaining
pairing determinant. It does not become a unit just from the
injectivity of $P$.

## 4. Why the most natural unit-pole adjoint pairing vanishes

Now impose the **actual** four equations and take their
normalized extremal triple $A,B,C$. Put


$$
J=C(B'+B)-C'B,\qquad
K=D(AC'-A'C)-C^2.
$$


The newly derived pole identity is


$$
4\operatorname{Res}(D,C)\operatorname{Res}(D,J)=\kappa^2,
\qquad \kappa=b_d\Xi_d\text{ a unit}.
\tag{6}
$$


Although both pole resultants are units, they do not directly
provide a nonzero cokernel row.

The rational factorization of $L$ in
literature_accessory_heine_stieltjes_and_pole_identity.md
shows that its formal adjoint has the rational solution


$$
L^\dagger\left(\frac{DJ}{z^{s+1}}\right)=0.
\tag{7}
$$


For example the left factor of $L/(zD)$ is
$\partial-s/z+2D'/D+J'/J$; the adjoint of that factor
annihilates $D^2J/z^s$. Dividing this solution by $zD$
gives (7).

It is tempting to take the coefficient pairing


$$
\Lambda(f)=[z^s]\,E_T(z)D(z)J(z)f(z),
\tag{8}
$$


where $E_T$ is the finite exponential jet through degree
$M-1=3d+3$, $M=s+2$. All its coefficients exist because
$M-1<p$. But the actual Taylor condition gives the stronger
identity


$$
\boxed{E_T D J\equiv K\pmod {z^{s+1}}.}
\tag{9}
$$



To verify it without characteristic-$p$ infinite series, write
$U_T=B E_T$ and
$R_T=A+U_T+C F_T=O(z^M)$, using the finite arctangent jet
$F_T$ through degree $M-1$. Through degree $M-2=s$,
one may use $E_T'=E_T$ and $F_T'=1/D$: their errors
start at degree $M-1$. Hence


$$
\begin{aligned}
E_T D J
&\equiv D(CU_T'-C'U_T)\\
&\equiv D(AC'-A'C)-C^2
\pmod {z^{M-1}}.
\end{aligned}
$$


In the second line the term involving $R_T'$ starts at
degree $M-1$, and the term involving $R_T$ even later.
This proof includes the boundary prime $p=M$.

Finally $\deg K\le2d$. For degrees $d,d$, the leading
Wronskian terms cancel; otherwise the sum of degrees is
at most $2d-1$. Thus
$\deg(AC'-A'C)\le2d-2$, which proves the bound after
multiplication by $D$.
For every $f\in\mathcal P_{d+1}$, (9) now yields


$$
\boxed{\Lambda(f)=0,}
\tag{10}
$$


because $s-(d+1)=2d+1>\deg K$.
Therefore this natural rational adjoint/pole pairing is the
zero functional on the entire space where (4) is tested.
Its endpoint units cannot be used to declare it a nonzero
row of the cokernel. A different dual construction would
have to establish its relation to the actual $\ell_0,\ell_1$.

## 5. One exact counterexample to the weaker pole-unit lemma

This is one fixed symbolic degree, followed by a single prime
selected from its exact discriminant. It is not a scan of
actual extremal degrees or primes.

For $d=2$, write $b=\beta,g=\gamma$. The exact equations are


$$
\begin{aligned}
E_1={}&b^3-22b^2+3bg+132b-18g-224,\\
E_0={}&-2b^3+b^2g+36b^2-18bg-180b+g^2+54g+288.
\end{aligned}
\tag{11}
$$


Their beta eliminant is


$$
f(b)=b^6-38b^5+589b^4-4714b^3
+20344b^2-44304b+37120,
$$


and the other monic relation, after inverting $12$, is


$$
12g=b^5-32b^4+397b^3-2336b^2+6416b-6336.
$$


The exact discriminant of $f$ is


$$
2^{19}3^6\cdot751\cdot318737.
$$


Modulo $751$, $\gcd(f,f')=b-30$, giving the exponential
root $(b,g)=(30,15)$. Its Jacobian matrix is


$$
\begin{pmatrix}55&72\\214&444\end{pmatrix},
\qquad \det=12\cdot751=0\pmod{751}.
$$


The normalized polynomial and actual signed-cofactor polynomial are


$$
B=z^2+20z-151,\qquad C^*=-328z^2-14z+68
\quad\text{in }\mathbb F_{751}[z].
$$


For $J^*=C^*(B'+B)-(C^*)'B$,


$$
\operatorname{Res}(D,C^*)=53,\qquad
\operatorname{Res}(D,J^*)=124.
\tag{12}
$$


Both are units, but the exponential Jacobian is singular.
The residue remainder is


$$
2(C^*)'-[(b+14)z+g-4]C^*
\equiv257+193z\pmod D,
$$


so this is **not** an actual four-equation root.
Moreover $4\cdot53\cdot124=3\pmod{751}$, a nonsquare;
it does not satisfy the stronger actual identity (6) with
a unit $\kappa$. No counterexample to the desired actual
étaleness statement has been obtained.

The precise refuted assertion is that an exponential-pair
root and the two pole-resultant units alone force étaleness.
The full two-pole compatibility is essential and remains
available as a potential additional input.

The exact certificate is
exponential_pair_single_symbolic_counterexample.py, with saved
output exponential_pair_single_symbolic_counterexample.json.
It also verifies the square-determinant normalization (2) in
this symbolic degree and the tangent witness
$(u,v)=(72,-55)$, $\dot B=72z+358$ modulo $751$.

## 6. What étaleness would improve, if the missing lemma is proved

Let $\mathscr A_d$ be the already reviewed finite free
exponential algebra over $\mathbb Z_p$. Assume $f>0$
and suppose $\mathcal J_d$ is a unit at the unique actual
residue point. That component of $\mathscr A_d$ is then
étale with residue field $\mathbb F_p$, hence is exactly
$\mathbb Z_p$. Equivalently the two exponential equations
have their unique Hensel lift there. On every other local
component at least one residue equation is nonzero modulo
the maximal ideal, since the full four-equation root is unique.

It follows that the norm polynomial


$$
\mathcal N_d(t)=\det(M_{R_0}+tM_{R_1})
$$


has content valuation exactly $f$ at this prime. The actual
component contributes the factor $\rho_0+t\rho_1$ with
$\min(v_p\rho_0,v_p\rho_1)=f$. The product from all other
components has unit Gauss content: after reduction, each
geometric factor is a nonzero linear polynomial, even when
that component has multiplicity. Therefore


$$
v_p(\operatorname{content}\mathcal N_d)=f.
\tag{13}
$$


This improves the earlier interval $f\le c\le D_df$
conditionally on precisely the missing two-row unit.
It still does not bound the height of the carrier or the
number of lifts.

The immediate remaining target is an identity forcing the
determinant (2) or (4) to be a unit under both equations (2)
of the pole-identity note, not merely under their resultant
unit consequences. The cancellation (10) and counterexample
(12) rule out two shortcuts to that conclusion.
