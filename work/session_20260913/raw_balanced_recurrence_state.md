> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact ladder and endpoint determinants for the balanced raw remainder

Date: 2026-09-13. A bounded attempt to obtain a recurrence for the
**actual selected remainder**, following the dual factorial-mass theorem.
No recurrence for that remainder with known asymptotic modes is claimed.

Subsequent continuation: `raw_hp_rational_degree_transfer.md` supplies
a bounded rational transfer through a different mixed-Wronskian gauge,
and a fixed21-unknown construction of the next actual triple. Thus the
growing state discussed here is an obstruction to this particular raw
ladder mechanism, not to all bounded degree-transfer constructions.

## 1. Archive check and the exact target

The canonical files `sources/raw_arctan_endpoint_remainder.md`,
`sources/raw_arctan_endpoint_arithmetic.md`, and
`sources/raw_arctan_bordered_rank_proof.md` supply the defining high
Taylor system, full endpoint cofactor formulas, and exact whole-integral
representations. They do not contain a closed recurrence in the balanced
degree n. The factorial and Bessel recurrence notes found in the archive
concern other families and cannot be substituted for this one.

Use the notation Q_k,F_k,h_k,v_k,G_k from the positive-kernel note, and
let V_n be the space of real polynomials of degree at most n satisfying



$$
\mu_k(P):=\int_0^1P(x)F_k(x)\,dx=0,
 \qquad n+1\le k\le2n-1.
\tag{1}
$$



The accepted rank theorem implies dim V_n=2 for n>=1. The two endpoint
functionals select the actual P_n in V_n; its remainder is
R_n(1)=integral P_n G_(2n-1). The present note supplies an exact
second-order ladder, its boundary forcing, and a two-by-two determinant
for this actual value. It also identifies the unclosed data in the
natural degree-shift construction.

## 2. A second-order differential ladder

Define the differential operator



$$
\mathcal J=xD^2+D+x,\qquad D=d/dx.
$$



Then



$$
\boxed{\mathcal J F_k=(k+1)F_{k+1}
          +k\beta_kF_{k-1},\qquad
 \beta_k=\frac{k^2}{4k^2-1}\quad(k\ge1),}
\tag{2}
$$



and JF_0=F_1. This is an operator ladder, not a three-term recurrence
under multiplication by x. The latter scalar Favard proposal has
already been disproved in `raw_borel_legendre_literature.md`.

For a direct proof, the monic raw Legendre identity is



$$
(1+t^2)Q_k'=ktQ_k+\gamma_kQ_{k-1},\qquad
 \gamma_k=\frac{k^2}{2k-1}=(2k+1)\beta_k.
$$



Its Borel transform uses



$$
\mathcal B(Q')=(xF')',\qquad
 \mathcal B(tQ)=\int_0^xF(s)ds,\qquad
 \mathcal B(t^2Q')=xF-\int_0^xF(s)ds.
$$



Consequently JF_k=(k+1)integral F_k+gamma_kF_(k-1). Substituting
integral F_k=F_(k+1)-beta_kF_(k-1) proves(2).

## 3. Exact transfer of the moment data

The operator J is formally self-adjoint. Its Green formula on [0,1]
has only the upper-endpoint contribution:



$$
\int_0^1P\,\mathcal JF-\int_0^1(\mathcal JP)F
   =P(1)F'(1)-P'(1)F(1).
$$



Applying (2) therefore proves the exact update for k>=1



$$
\boxed{\mu_k(\mathcal JP)
 =(k+1)\mu_{k+1}(P)+k\beta_k\mu_{k-1}(P)
       -P(1)F_k'(1)+P'(1)F_k(1).}
\tag{3}
$$



For P in V_n, even the interior range n+2<=k<=2n-2 gives



$$
\mu_k(\mathcal JP)=-P(1)F_k'(1)+P'(1)F_k(1),
$$



rather than zero. Thus J does not map V_n into the next annihilator.
Moreover V_(n+1) requires the high window n+2,...,2n+1. Compared with
the interior where both shifted old moments vanish, three upper rows
must still be imposed: 2n-1,2n,2n+1. The old degree window and its
endpoint forcing must both be handled; shifting only the polynomial
degree does not give a balanced recurrence.

The jet update is equally explicit. Write u_r=P^(r)(1), with u_(-1)=0.
Then



$$
\boxed{(\mathcal JP)^{(r)}(1)
 =u_{r+2}+(r+1)u_{r+1}+u_r+r u_{r-1}.}
\tag{4}
$$



Hence a jet state through order m requires two further derivatives
under one update. This is a genuine failure of closure for the proposed
fixed-jet mechanism: the polynomial (x-1)^(m+2) has zero jets through
order m, but (JP)^(m)(1)=(m+2)! is nonzero. No map on just those jets
can update J on all polynomial degrees.

This observation does not rule out a special identity for the selected
P_n, or a different finite-dimensional system. Such an identity has
not been derived from (1). For example, adjoining endpoint distributions
does not by itself close the system: the adjoint of J raises their
derivative order by two, with nonzero leading coefficient at x=1.

## 4. A two-by-two determinant for the actual remainder

Define, for P of degree at most n,



$$
b(P)=\int_{-\infty}^1e^{x-1}P(x)dx
     =\sum_{r=0}^n(-1)^rP^{(r)}(1),
$$




$$
t(P)=\int_0^1P(x)T_n(x)dx,\qquad m(P)=t(P)+4b(P),
$$




$$
r(P)=\int_0^1P(x)G_{2n-1}(x)dx.
$$



The first identity follows by repeated integration by parts. In the
original B-coordinate change it is exactly B(1), not a new arbitrary
normalization. The endpoint equations are b(P_n)=1 and m(P_n)=0.

For any rational basis U,V of the actual two-dimensional V_n, put



$$
D_n=\det\begin{pmatrix}b(U)&b(V)\\m(U)&m(V)\end{pmatrix}.
$$



The accepted all-degree endpoint rank theorem gives D_n!=0. Cramer's
rule now gives the exact whole-value identity



$$
\boxed{R_n(1)=
 \frac{\det\begin{pmatrix}r(U)&r(V)\\m(U)&m(V)\end{pmatrix}}
      {\det\begin{pmatrix}b(U)&b(V)\\m(U)&m(V)\end{pmatrix}}.}
\tag{5}
$$



Both determinants change by the same nonzero factor when U,V are
replaced by another basis. Thus(5) has the actual normalization and
combines the signed mass and cancellation into one value. The
denominator is nonzero, but no quantitative estimate for this ratio
follows from nonvanishing alone.

The inverse-Gram note `raw_arctan_inverse_norm_attempt.md` supplies
an equivalent projected-space description and correctly preserves its
small angle. Formula(5) is not a claim that the entries have already
been computed by a fixed-size recurrence: obtaining U,V still involves
the growing high moment system.

## 5. A rational spectral representation of the remaining state

For completeness, the four-jet Green representation in the literature
and inverse-Gram notes gives a direct rational description of that
growing system. Let lambda_j=j(j+1) and



$$
v_j=(F_j(1),F_j'(1),F_j''(1),F_j'''(1))^T,\qquad
 \Omega=\begin{pmatrix}
 0&1&2&1\\-1&0&-1&0\\-2&1&0&0\\-1&0&0&0
 \end{pmatrix}.
$$



The fourth-order eigenoperator
L=(x^2D^2)''+(x^2D)' satisfies LF_j=lambda_jF_j. Its boundary form gives



$$
(\lambda_k-\lambda_j)\int_0^1F_jF_k
       =v_j^T\Omega v_k\quad(j\ne k),\qquad\det\Omega=1.
\tag{6}
$$



Write P=sum_(j=0)^n a_jF_j and define the four-component rational function



$$
Z_P(\lambda)=\sum_{j=0}^n\frac{a_jv_j}{\lambda-\lambda_j}.
$$



Since every high k is greater than n, no diagonal limit is needed, and



$$
\boxed{P\in V_n\quad\Longleftrightarrow\quad
 Z_P(\lambda_k)^T\Omega v_k=0
       \quad(k=n+1,\ldots,2n-1).}
\tag{7}
$$



The residue at lambda_j is constrained to the one-dimensional line
spanned by v_j. Thus Z_P has n+1 free scalar residues, not four free
constants. Its common denominator is product_(j=0)^n(lambda-lambda_j),
and its numerator degree grows with n.

The positive tail identity in the dual-mass note gives the actual
remainder functional in these coordinates:



$$
\boxed{r(P)=\sum_{k\ge2n}\frac{v_k^{\rm mom}}{h_k}
                  Z_P(\lambda_k)^T\Omega v_k,}
\tag{8}
$$



where v_k^mom=L_raw(Q_k/(1-t)) is the scalar second-kind moment
(distinguished from the four-vector v_k). The series is absolutely
convergent, by the already proved uniform Borel-tail convergence and
the bounded polynomial P on [0,1]. This is an actual value formula,
not an estimate of its positive kernel alone.

Under n->n+1 the pole set acquires lambda_(n+1), the observation at that
node is removed, and two new observations lambda_(2n),lambda_(2n+1)
are added. Knowing that the boundary vectors v_k obey holonomic
relations does not specify how all these residues transform. A
closed matrix transformation preserving these constrained residues
would be a useful additional lemma; it is not supplied by(6).

## 6. What was and was not achieved

The new operator ladder(2), moment update(3), and jet update(4) are exact.
They show precisely why the simplest bounded-jet balanced recurrence
attempt does not close. Equations(5),(7),(8) express the selected whole
remainder through its two-dimensional annihilator and four boundary
coordinates, without estimating M_n and its cancellation separately.

No fixed-order linear recurrence in n with specified rational
coefficients, and no asymptotic modes for R_n(1), were obtained. It would
be invalid to infer such a recurrence merely from the holonomic entries
of an increasing determinant. The remaining concrete possibilities are
a closed degree-shift transformation for(7), or an asymptotic estimate
for the actual determinant ratio(5). The independent bounded-degree
third-order z-ODE in `raw_hp_homogeneous_ode.md` is a
different route and may replace the growing jet hierarchy if its
accessory parameters can be controlled. Its existence alone does not
supply those parameter asymptotics.
