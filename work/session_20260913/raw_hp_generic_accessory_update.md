> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A generic fixed-state update from the scalar equation and endpoint jets

Date: 2026-09-13. This note strengthens
`raw_hp_rational_degree_transfer.md` in a stated generic case. It gives
an explicit square rational linear system using bounded accessory data,
n, and a fixed collection of endpoint jets. It does not prove that the
generic hypotheses hold at every degree, nor give asymptotic modes.

## 1. Hypotheses, state and result

Take the actual normalized degree-n raw family, n>=1, with B_n(1)=1,
C_n(1)=4 and R_n=O(z^(3n+1)). Use the exact scalar equation



$$
A_3y'''+A_2y''+A_1y'+A_0y=0,
 \quad A_3=zD Q,\quad D=1+z^2
$$



from `raw_hp_homogeneous_ode.md`. Assume only for this step that



$$
\boxed{\deg Q=3,\qquad Q\text{ is squarefree},\qquad
              \gcd(Q,zD)=1.}\tag{1}
$$



No condition Q(1)!=0 is imposed. The state consists of n, Q and the
four bounded-degree equation coefficients, together with the rational
endpoint jets U_n^(j)(1)/e and C_n^(j)(1), 0<=j<=5. The latter are a
fixed finite collection of connection data, not inferred from Q alone.

There is an explicit20-by20 rational linear system in the coefficients
of N_0,N_1,N_2, with degrees at most5,6,6. It has a unique solution.
The rational operator



$$
S_n=\frac{N_0+N_1D_z+N_2D_z^2}{Q}
\tag{2}
$$



sends the actual fundamental columns R_n,U_n,C_n to the canonical
next-degree columns. The equation and its accessories then update
through the rational compatibility formulas of the transfer note.
Thus this is a fixed-state exact update with endpoint data retained.

The hypotheses concern the current degree only. The output can have
degenerate Q_(n+1). In that event this generic system is not automatically
valid for the following step; the unrestricted21-unknown construction
using current polynomial data remains available.

## 2. Six conditions at the accessory poles

At a root a of Q, the three actual solutions are analytic and have
echelon orders0,1,3. In particular y(a),y'(a) are free, and the equation
at a gives



$$
A_2(a)=-A_3'(a),\qquad
 y''(a)=\frac{A_0(a)y(a)+A_1(a)y'(a)}{A_3'(a)}.
$$



The denominator is nonzero by(1). Since Q has a simple zero, S_n y
is analytic at a for every solution if and only if its numerator
vanishes there for both free values. Equivalently impose



$$
\boxed{Q\mid A_3'N_0+A_0N_2,\qquad
        Q\mid A_3'N_1+A_1N_2.}\tag{3}
$$



The two Euclidean remainders each have three coefficients, giving six
rational linear equations. These are conditions on the entire local
solution space; no global evaluation of A_n,B_n,C_n at the accessory
roots is needed.

## 3. Four conditions at the logarithmic points

At a=i or -i, Q(a)!=0, so S_n has analytic coefficients. The original
logarithmic column has the form C(z)gamma log(z-a)+H(z), with H analytic
and gamma!=0. Moreover C(a)!=0. To see the latter directly, the known
Wronskian has a pole of order exactly2 at a. If C(a)=0, derivatives
through order2 of C log(z-a) have poles of order at most1, so the
Wronskian could not have a pole of order2.

Write t_j=N_j/Q. Subtract the new logarithmic coefficient (S_n C)
gamma log(z-a) from S_n R. The potentially singular additional part is



$$
\gamma\left(\frac{t_1 C+2t_2C'}{z-a}
                       -\frac{t_2C}{(z-a)^2}\right).
$$



Its double pole vanishes exactly when t_2(a)=0. Its remaining simple
pole then vanishes exactly when t_1(a)=t_2'(a). Because Q(a)!=0, the
conditions at both points are therefore



$$
\boxed{D\mid N_2,\qquad D\mid(N_1-N_2').}\tag{4}
$$



These are four rational linear conditions. After they hold, S_n maps
each analytic column to an analytic column at ±i, and maps the
logarithmic column to one with an analytic logarithmic coefficient and
an analytic nonlogarithmic part.

## 4. Five origin conditions from accessory coefficients alone

Put M=3n+1. Since Q(0)!=0, the actual local solution orders at zero
are0,1,M. The high solution R_n is a nonzero multiple of the uniquely
normalized Frobenius series



$$
f(z)=z^M(1+u_1z+u_2z^2+\cdots).
$$



Only u_1,...,u_4 are required here. They are obtained from the scalar
equation in fixed rational work. If u_0=1, substituting the terms already
known into the equation gives u_r by division by



$$
Q(0)(M+r)(M+r-1)r\ne0\quad(r=1,\ldots,4).
\tag{5}
$$



This is the coefficient of u_r at power z^(M+r-2). All other terms at
that power use earlier u's and bounded-degree equation coefficients.
Using the exponent M symbolically avoids constructing a long Taylor
prefix. The coefficient denominator in(5) is the indicial polynomial
at M+r, not an assumed generic nonresonance condition.

Impose the five equations



$$
\boxed{[z^k](N_0f+N_1f'+N_2f'')=0,
                 \quad k=M-2,\ldots,M+2.}\tag{6}
$$



The numerator has no lower powers. Since Q is a unit at zero, (6) is
equivalent to S_nR_n=O(z^(M+3))=O(z^(3(n+1)+1)). Multiplying f by its
unknown actual leading coefficient does not change these homogeneous
conditions.

## 5. Three infinity conditions, with both Laurent branches retained

Write a_(j,d)=[z^d]N_j. The degree identity in the scalar-ODE note shows
that q=3 gives one exponential branch e^z z^n times a Laurent unit,
and two Laurent branches with distinct highest powers n,n-1. This
statement concerns the whole Laurent plane. It does not assume that
the particular polynomial C_n has degree n rather than n-1.

The numerator degree bounds in(2) imply that the degree-(n-1) Laurent
branch already maps to growth at most z^(n+1). On a degree-n Laurent
branch, the only possible larger term is z^(n+2), whose coefficient is
a nonzero leading branch constant times a_(0,5)+n a_(1,6), divided by
the leading coefficient of Q. Thus impose



$$
a_{0,5}+n a_{1,6}=0.
$$



For the exponential branch, remove e^z and expand the numerator as



$$
N_0B+N_1(B+B')+N_2(B+2B'+B'').
$$



The potential quotient degrees above n+1 are n+3 and n+2. Their
successive cancellation is equivalent to



$$
a_{1,6}+a_{2,6}=0,
$$




$$
a_{0,5}+a_{1,5}+a_{2,5}
                  +n a_{1,6}+2n a_{2,6}=0.
$$



The next coefficient of B multiplies a_(1,6)+a_(2,6) in the second
equation, so disappears after the first equation is imposed. Therefore
no formal connection coefficient or actual leading coefficient of B
is needed. In total the three infinity conditions are



$$
\boxed{a_{0,5}+n a_{1,6}=0,\quad
        a_{1,6}+a_{2,6}=0,\quad
        a_{0,5}+a_{1,5}+a_{2,5}
                     +n a_{1,6}+2n a_{2,6}=0.}\tag{7}
$$



## 6. Global sufficiency of the eighteen homogeneous conditions

For an operator satisfying(3),(4),(6),(7), define the rational
expressions Ahat,Bhat,Chat by formula(11) of the degree-transfer note.
They obey identically



$$
S_nU_n=e^z\widehat B,\quad S_nC_n=\widehat C,\quad
 S_nR_n=\widehat A+e^z\widehat B+\widehat C\arctan z.
$$



The only possible finite poles of Bhat and Chat are roots of Q.
Condition(3) removes them; hence they are polynomials. The only
additional possible poles of Ahat are ±i. Condition(4), with the
displayed logarithmic coefficient subtracted, removes those poles.
Condition(3) already removes Ahat's accessory poles, since arctan is
analytic there. Thus Ahat is also a polynomial.

Condition(7) bounds Bhat's degree by n+1. It bounds the image of the
entire Laurent plane by z^(n+1), and therefore bounds Chat's degree
by n+1. On a fixed infinity branch put
H=A_n+C_n(arctan z-F_infinity). Both H and C_n belong to that Laurent
plane. Now



$$
S_nH=\widehat A+
             \widehat C(\arctan z-F_\infty).
$$



The second term has growth at most z^n, because arctan z-F_infinity
is O(1/z). Consequently Ahat also has degree at most n+1. Finally (6)
supplies precisely the next required origin order.

We have proved that the eighteen homogeneous equations map every
solution to an actual *unmatched* next-degree triple. Conversely,
every unmatched next-degree triple gives such an operator through the
mixed-row Cramer construction. Its numerator degrees are at most5,6,6,
and the four local/global tests are necessary by the arguments above.
The correspondence is injective because an order-at-most2 operator
annihilating all three old fundamental solutions is zero.

The unmatched next-degree Taylor solution space has dimension2: adding
the one matching row gives the known one-dimensional canonical line,
and the original number of Taylor equations leaves dimension at least2.
Thus these eighteen homogeneous equations have rank18 on twenty
unknowns. This also proves that the formal conditions are sufficient
for the required global branch selection; no positivity or unproved
connection identity is used.

## 7. Two endpoint conditions and the square update

Write u_j=U_n^(j)(1)/e and c_j=C_n^(j)(1), rational stored data.
If Q(1)!=0, impose



$$
\sum_{j=0}^2N_j(1)u_j=Q(1),\qquad
 \sum_{j=0}^2N_j(1)c_j=4Q(1).
\tag{8}
$$



If Q(1)=0, it is a simple root by(1), and(3) already makes both
numerators vanish there. Their analytic quotient values are obtained
by one derivative. Replace(8) by



$$
\sum_{j=0}^2\bigl(N_j'(1)u_j+N_j(1)u_{j+1}\bigr)=Q'(1),
$$




$$
\sum_{j=0}^2\bigl(N_j'(1)c_j+N_j(1)c_{j+1}\bigr)=4Q'(1).
\tag{9}
$$



These conditions are exactly Bhat(1)=1 and Chat(1)=4. In the first
equation of(9), differentiating the removed exponential contributes a
multiple of the zero numerator, so the displayed u-jet formula is
correct without an additional term.

The canonical rank and endpoint theorem makes these two conditions
independent on the unmatched two-dimensional space. Together with
the eighteen homogeneous equations they therefore give a nonsingular
twenty-by-twenty rational system. Its unique solution is the desired
actual degree transfer.

## 8. Updating the bounded state and the exact remaining limitation

The first transfer row t=(N_0,N_1,N_2)/Q determines its next two rows
by t_1=t'+t C_n and t_2=t_1'+t_1 C_n, using the current companion
matrix. Form T from these rows. Then



$$
C_{n+1}=(T'+T C_n)T^{-1},\qquad
 Q_{n+1}=\det(T)Q_n/z^3.
\tag{10}
$$



These identities preserve the exact common scaling because the two
endpoint conditions fixed the new polynomial normalization. The
remaining scalar-ODE coefficients are recovered from the last
companion row with A_(3,n+1)=zD Q_(n+1).

Six endpoint jets remain a fixed sufficient state. The companion
equation generates the finitely many higher old jets needed when
differentiating S through order5. At z=1 its analytic solution space
has echelon exponents at most5, as proved by the Wronskian order bound.
The local recurrence therefore has no undetermined coefficient beyond
those six jets. In the present squarefree case any zero of Q at1 is
simple, so only the familiar analytic exponents0,1,3 occur there.
Division by Q at such a point requires one extra old Taylor coefficient;
all required work is bounded independently of n. Store U-jets divided
by e, so the state and its update remain rational.

To follow the actual remainder values, carry its six endpoint jets as
an additional fixed column and propagate them by the same transfer.
Equivalently carry three formal rational coefficient columns attached
to 1,e,pi. No rational linear independence or uniqueness of real-number
representation is assumed. These columns are initialized by the known
seed triple; they are not reconstructed from a claimed local connection
formula.
The update of N itself needs only the rational U/e and C endpoint data
specified above.

This proves a finite rational update on the generic locus, with endpoint
connection data retained. The equations can be solved by rational
linear algebra; writing the resulting coefficient map as expanded
quotients of large determinant polynomials is unnecessary. We have
not bounded its orbit, its accessory roots, or its endpoint transfer
products. Nor have we proved that the actual orbit stays on the generic
locus. These are specific remaining requirements before this update
could yield an asymptotic theorem for R_n(1), and the primitive
endpoint denominator remains a separate arithmetic issue.

## 9. Independent construction controls

`check_raw_generic_accessory_update.py` carries out the new20-by20
solve at the two preselected current degrees n=1 and n=2. The equations
use only the old scalar coefficients, cubic Q, n, and carried endpoint
jets. In particular the solve does not contain polynomial-division
conditions on A_n,B_n,C_n, and its high origin jet is reconstructed
from the scalar Frobenius recurrence rather than copied from R_n.

Both matrices have rank20. Both resulting first-row operators agree
exactly with the separately obtained21-unknown polynomial-transfer
construction. The generic hypotheses are checked exactly before each
test. The results are saved in `raw_generic_accessory_update_checks.json`.
These controls supplement the rank and global-sufficiency proof; they
are not evidence that all later degrees remain generic. The tested
degrees have Q(1)!=0, so the simple-root endpoint branch(9) is justified
by its analytic quotient proof, not by these two controls.
