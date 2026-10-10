> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A homogeneous third-order equation for the actual raw Hermite–Padé family

Date: 2026-09-13. Original bounded-degree reduction, with exact accessory
constraints. No asymptotic coefficient limit, primitive shrinking, or
irrationality conclusion is claimed.

## 1. Scope, archive comparison, and normalization

For n>=1 let



$$
R=A+Be^z+CF,\quad F=\arctan z,\quad D=1+z^2,
 \quad\deg A,\deg B,\deg C\le n,
 \quad\operatorname{ord}_0R\ge3n+1.
\tag{1}
$$



The endpoint condition is C(1)=4B(1). Its exact nonzero normalized raw
solution is supplied by the existing rank and endpoint determinant proofs.
Write U=Be^z and V=C. The derivation below works before endpoint
normalization and also for F'=kappa/D with a nonzero constant kappa and
a fixed quadratic D having simple roots and D(0)!=0.

`endpoint_hp_continuation.md` already proved the nonzero cubic Wronskian
factor and a second-order inhomogeneous equation. Its proof applies to
(1) with kappa=1. The archive also contains an order-three equation for
the fixed span {1,e^z,arctan z} in
`sources/e_g_mixed_slope_division_no_go.md`. That equation does not
annihilate arbitrary polynomial-prefactored high-order remainders. The
new content here is a homogeneous equation for {R,Be^z,C}, whose
polynomial coefficient degrees remain bounded independently of n, and
its accessory constraints. The searched Wronskian and raw-HP notes did
not already contain this equation.

For an ordered row set I contained in {0,1,2,3}, let
$W_I=\det(y_j^{(r)})_{r\in I,j=1,2,3}$, with columns (R,U,C).
The previously proved cubic is



$$
N=D^2e^{-z}W_{012}=z^{3n-1}Q,\quad Q\ne0,\quad q:=\deg Q\le3.
\tag{2}
$$



B and C are nonzero because the two-function multiplicity bound is
2n+1. Logarithmic monodromy and the nonrationality of exp imply the
constant linear independence of R,U,C. Thus these are three independent
solutions, not merely three names for a smaller solution space.

## 2. All four cofactors and the exact homogeneous equation

Expand the 4-by-4 Wronskian with first column y and remaining columns
R,U,C. Its determinant vanishes precisely on their constant span and
gives



$$
W_{012}y'''-W_{013}y''+W_{023}y'-W_{123}y=0.
\tag{3}
$$



Set



$$
\begin{aligned}
 A_3&=zDQ,\\
 A_2&=-\bigl[((z+3n-1)D-2zD')Q+zDQ'\bigr],\\
 A_1&=D^3e^{-z}W_{023}/z^{3n-2},\\
 A_0&=-D^3e^{-z}W_{123}/z^{3n-2}.
 \end{aligned}
\tag{4}
$$



Then the actual homogeneous equation is



$$
\boxed{A_3y'''+A_2y''+A_1y'+A_0y=0.}
\tag{5}
$$



All A_j are polynomials over the coefficient field of A,B,C. To see
this without manipulating a logarithm in a determinant, subtract U and
F times C from the R column. Its derivative row r becomes



$$
E_r=A^{(r)}+
 \sum_{j=1}^r\binom rjC^{(r-j)}F^{(j)}.
\tag{6}
$$



The other columns, after factoring e^z, are
$(\partial_z+1)^rB$ and $C^{(r)}$. For r<=3, F^(r) has denominator
dividing D^3. Thus D^3 clears all four determinants. Since every
cofactor includes one R derivative of order at most3, its origin order
is at least ord(R)-3>=3n-2. Division in (4) is therefore polynomial.

Finally W013=W012', since differentiating the first two rows of W012
produces a repeated row. Differentiating (2) gives exactly the displayed
A2. In monic form its coefficient has the especially simple identity



$$
\boxed{\frac{A_2}{A_3}
 =-1-\frac{3n-1}{z}+2\frac{D'}D-\frac{Q'}Q.}
\tag{7}
$$



## 3. Uniform degrees, and sharper degrees depending on q

Directly from (6),



$$
\deg A_3\le6,\qquad\deg A_2\le6,\qquad
 \deg A_1\le5,\qquad\deg A_0\le4.
\tag{8}
$$



Here is a degree check for the last two bounds. At infinity
F^(j)=O(z^(-j-1)), so the nonpolynomial part of E_r is O(z^(n-r-1)).
In W023, the polynomial part has degree at most3n-3: every potentially
largest two-column factor A C^(j)-A^(j) C loses its top equal-degree
term. The rational terms have the same upper growth3n-3. Multiplication
by D^3 gives degree at most3n+3, then removing z^(3n-2) gives5.
For W123 the corresponding bounds are3n-4,3n+2,4. These estimates remain
valid when a polynomial has smaller degree or a derivative vanishes.

There is a sharper all-index description. Near infinity, fix a local
constant F_infinity and put
$H=A+C(F-F_\infty)$. This is a convergent Laurent germ, with highest
power at most n. The two-dimensional span of C,H has a basis with
distinct highest integer powers c,d. One basis vector can be C, so
c=deg C; cancel its highest coefficient from H when necessary. The
remaining vector is nonzero because F is not rational. Let b=deg B.
Then



$$
U\sim u z^b e^z,\qquad C\sim v z^c,
 \qquad H_{\rm reduced}\sim h z^d,\qquad c\ne d.
$$



The leading Wronskian is a nonzero multiple of
$e^zz^{b+c+d-1}$, since the algebraic two-column derivative contributes
the nonzero factor d-c. Comparing with (2) gives



$$
\boxed{b+c+d=3n+q-4.}
\tag{9}
$$



All three powers are at most n, and c,d are distinct, so each differs
from n by at most4; in particular b>=n-3. These are formal degrees of
the actual solutions, not fitted degree patterns.

More explicitly, the nonnegative integer defects obey
$(n-b)+(n-c)+(n-d)=4-q$, with n-c and n-d distinct. Thus only finitely
many infinity degree types are possible, independently of n. In
particular q=3 forces b=n and the unordered pair {c,d}={n,n-1}.

The same cofactor comparison at infinity gives



$$
\frac{A_1}{A_3}=\frac{c+d-1}{z}+O(z^{-2}),\qquad
 \frac{A_0}{A_3}=-\frac{cd}{z^2}+O(z^{-3}).
\tag{10}
$$



Consequently



$$
\boxed{\deg A_1\le q+2,\qquad\deg A_0\le q+1.}
\tag{11}
$$



If q_q is the leading coefficient of Q, the coefficients of z^(q+2)
and z^(q+1) in A1,A0 are respectively
$(c+d-1)q_q$ and $-cdq_q$, with zero allowed. Whenever q=3 these
become $(2n-2)q_3$ and $-n(n-1)q_3$, without needing to assume
which member of the unordered pair {c,d} is the degree of C.

Infinity remains irregular: one exact solution has the exponential
factor e^z and the other two have Laurent expansions. Polynomial
degree bounds do not turn it into a three-branch Fuchsian problem.

## 4. Local exponents at the fixed finite points

Assume first Q(0)Q(i)Q(-i)!=0. All assertions in this paragraph follow
from the displayed polynomial equation, without a generic-normality
assumption about other degrees.

At zero, A3 has a simple zero; A2/A3 has residue -(3n-1), while A1/A3
and A0/A3 have at most simple poles. The indicial polynomial is



$$
r(r-1)(r-2)-(3n-1)r(r-1)=r(r-1)(r-3n-1).
$$



The local exponents are therefore 0,1,3n+1. At either xi=i or -i,
A2/A3 has residue2 and the other coefficients again have at most
simple poles. The indicial polynomial is r^2(r-1), giving 0,0,1.
The actual monodromy is the rank-one logarithmic transformation
R -> R+2pi*i*res_xi(F')*C, with U,C unchanged.

When Q vanishes at a fixed point, these generic indicial computations
must not be reused. At zero there is an exact defect ledger: let
l0<l1 be the two vanishing orders of a local echelon basis of span(U,C),
and M=ord(R). The two-function bound ensures l1<=2n+1<M. Hence



$$
M+l_0+l_1=3n+2+\operatorname{ord}_0Q,
 \quad (M-3n-1)+(l_0+l_1-1)=\operatorname{ord}_0Q\le3.
\tag{12}
$$



This tracks all origin defects exactly. At a logarithmic pole shared
with Q, the indicial calculation requires the actual coefficient
valuations and jets. No all-index exclusion of these exceptional
cases is assumed in this note.

## 5. Explicit no-log equations at the accessory roots

Let a be a simple root of Q with aD(a)!=0. All three actual solutions
are analytic there. Their Wronskian has a simple zero, so their echelon
vanishing orders are exactly0,1,3. Such a root is an apparent singularity
of the scalar equation, and (7) gives residue -1 for A2/A3.

There are two useful exact algebraic constraints. Put x=z-a and divide
(5) by A3/x, obtaining



$$
x y'''+b(x)y''+c(x)y'+d(x)y=0,\quad b(0)=-1.
$$



For y=y0+y1*x+y2*x^2+..., the constant equation is
2y2=c0*y1+d0*y0. At the next equation the y3 coefficient vanishes.
For both y0 and y1 to be free, its two remaining coefficients must
vanish:



$$
(b_1+c_0)c_0+c_1+d_0=0,\qquad
 (b_1+c_0)d_0+d_1=0.
\tag{13}
$$



Here subscripts denote Taylor coefficients at x=0. These conditions
are also sufficient locally for three analytic solutions: y0,y1,y3
are then free, and all later recurrence coefficients are nonzero.
The coefficients are analytic at x=0, so the regular-singular power
series recurrence converges in a sufficiently small disk.

Since A2(a)=-A3'(a), substituting the derivatives of the quotients into
(13) cancels all A3'' terms. It gives the particularly simple identities



$$
\begin{aligned}
 A_1(A_2'+A_1)+A_3'(A_1'+A_0)&=0,\\
 A_0(A_2'+A_1)+A_3'A_0'&=0
 \end{aligned}\qquad\text{at }z=a.
\tag{14}
$$



Thus, if Q is squarefree and coprime to zD, the actual accessory
polynomials satisfy



$$
\boxed{Q\mid A_1(A_2'+A_1)+A_3'(A_1'+A_0),\qquad
 Q\mid A_0(A_2'+A_1)+A_3'A_0'.}
\tag{15}
$$



If Q has exceptional or repeated roots, (14) still applies individually
at every simple root outside {0,i,-i}; the global divisibility assertion
must then be restricted to that factor. Conditions for repeated roots
require additional local recurrences.

## 6. What is finite, and what is still uncontrolled

After common scaling, Q,A1,A0 have at most3q+5 coefficients, at most14.
A2 is determined by Q,n. Formula (10) fixes two leading coefficients;
(15) supplies explicit apparent-singularity constraints when its
hypotheses hold. These are a bounded number of polynomial equations
in accessory coefficients, with n entering explicitly. They are a
finite parameter system, not a claim that the listed constraints are
independent or that they uniquely select the actual solution.

To select the actual family one must also impose the origin analytic
resonance, polynomial solutions C and e^zB of the required degrees,
and the original endpoint connection condition. For example, absence
of an origin logarithm with exponents0,1,3n+1 involves the recurrence
through that growing resonance. Its existence does not become a
fixed-length asymptotic estimate merely because there are finitely
many accessory coefficients.

A conditional characteristic curve can be written on the natural
exponential scale z=n*zeta. Work on a subsequence with fixed q, divide
Q by its leading coefficient, and suppose the following fixed-degree
polynomials converge coefficientwise:



$$
\widehat Q_n(\zeta)=\frac{Q_n(n\zeta)}{q_qn^q},\quad
 \widehat P_{1,n}(\zeta)=\frac{A_{1,n}(n\zeta)}{q_qn^{q+3}},\quad
 \widehat P_{0,n}(\zeta)=\frac{A_{0,n}(n\zeta)}{q_qn^{q+3}}.
\tag{16}
$$



Their limits have leading coefficients1,2,-1, respectively, by (9)–(11).
Away from zero and the limiting Q roots, the monic coefficients tend
to -1-3/zeta, P1/(zeta^3 Q), P0/(zeta^3 Q). If an actual solution also
has locally uniform logarithmic-derivative convergence
$y_n'(n\zeta)/y_n(n\zeta)\to p(\zeta)$, with the corresponding
derivative terms controlled, its limiting equation is



$$
\boxed{\zeta^3\widehat Q\,p^3
 -\zeta^2(\zeta+3)\widehat Q\,p^2
 +\widehat P_1p+\widehat P_0=0.}
\tag{17}
$$



In a zero-free domain, local holomorphic convergence of the logarithmic
derivatives supplies that derivative control by Cauchy estimates: the
derivative in z introduces a factor1/n. Neither the coefficient bounds
in (16), their convergence, nor the required zero-free domains have
been proved here. In particular the local finite exponents fix neither
the two remaining limiting polynomials nor the selected branch or its
connection constant. The collapse of +/-i to zeta=0 also forbids an
unjustified interchange of this limit with the fixed-point Frobenius
expansion.

## 7. Primary-source precedent and exact boundary of applicability

[Martínez-Finkelshtein–Rakhmanov–Suetin, *Asymptotics of type I
Hermite–Padé polynomials for semiclassical functions*](https://arxiv.org/pdf/1502.01202),
Theorem1.1 and Section3.1, use a Wronskian method to obtain bounded-degree
equations for their stated algebraic-product class. Their hypotheses
include rational logarithmic derivatives and normalization at infinity.
The raw arctangent has a rational derivative, but not a rational
logarithmic derivative; exp is not in the displayed finite
algebraic-product class. That theorem is methodological precedent and
does not supply the missing coefficient limits or asymptotics for this
mixed family. The independent column subtraction in (6) is what proves
the present equation despite that mismatch.

The most useful next steps are an exact degree-shift compatibility
system retaining these accessory coefficients, and an actual bound on
their scaled roots or coefficients. Bounded degree alone supplies
neither. The endpoint denominator and its gcd remain separate arithmetic
inputs even after an analytic characteristic curve has been obtained.

## 8. Companion normalization for a degree-shift compatibility check

For the jet fundamental matrix with columns R,U,C and rows0,1,2,



$$
\Psi_n' =\mathcal A_n\Psi_n,\qquad
 \mathcal A_n=\begin{pmatrix}
 0&1&0\\0&0&1\\
 -A_0/A_3&-A_1/A_3&-A_2/A_3
 \end{pmatrix},\qquad
 \det\Psi_n=\frac{e^zz^{3n-1}Q_n}{D^2}.
\tag{18}
$$



This fixes the signs and gauge for an independent n-to-n+1 transfer
calculation. Under common scaling of the original polynomial triple by
c, Psi scales by c and Q by c^3; the companion matrix does not change.
A degree-shift determinant must retain the corresponding ratio of Q's.
Existence of a finite-degree rational transfer and a usable recursively
closed accessory update are distinct statements.

## 9. Exact original-row controls

`check_raw_hp_homogeneous_ode.py` constructs the actual raw rows directly
from their Taylor equations for n=1,2,4, independently of the cubic
formula. It then checks all four cofactor formulas, polynomial division
and degree bounds, direct annihilation of the three functions, the
infinity degree ledger, both leading coefficients, and both apparent
congruences after verifying their squarefree/coprimality hypotheses.
All checks pass. The exact output is
`check_raw_hp_homogeneous_ode.json`. This finite verification supplements
the all-index derivations; no all-degree genericity or asymptotic pattern
is inferred from the three rows.
