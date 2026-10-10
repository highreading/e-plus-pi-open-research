> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Bounded rational degree transfer for the actual raw Hermite–Padé family

Date: 2026-09-13. Root proposed the mixed-Wronskian transfer; this note
derives it rigorously, records its compatibility, and turns its first
row into a fixed-size exact construction of the next normalized triple.
The degree transfer replaces the growing raw-jet mechanism in
`raw_balanced_recurrence_state.md`. Its accessory coefficients are not
yet known explicitly as functions of n, and no asymptotic modes are
claimed.

Further continuation: `raw_hp_generic_accessory_update.md` proves an
explicit20-by20 update from bounded accessory coefficients plus carried
endpoint jets when Q is cubic, squarefree, and coprime to z(1+z^2).
That generic local-to-global theorem supplies the smaller update left
open in Section4 here. It neither proves all-degree genericity nor
controls the asymptotic orbit.

## 1. Normalization and a universal rational gauge

For every n>=1 take the unique canonical triple with B_n(1)=1 and
C_n(1)=4. Put



$$
R_n=A_n+B_ne^z+C_n\arctan z=O(z^{3n+1}),\quad
 U_n=B_ne^z,\quad D=1+z^2.
$$



Let Psi_n be the three-by-three matrix with derivative rows 0,1,2
and columns (R_n,U_n,C_n). Define the polynomial matrix



$$
K_n=\begin{pmatrix}
 D^2A&B&C\\
 D^2A'+DC&B+B'&C'\\
 D^2A''+2DC'-D'C&B+2B'+B''&C''
 \end{pmatrix}.
\tag{1}
$$



Here A,B,C are the degree-n polynomials. Direct differentiation gives



$$
\Psi_n=K_n S G,\qquad S=\operatorname{diag}(D^{-2},1,1),
 \quad G=\begin{pmatrix}1&0&0\\e^z&e^z&0\\\arctan z&0&1\end{pmatrix}.
\tag{2}
$$



Both S and G are independent of n. In particular



$$
\det K_n=D^2e^{-z}\det\Psi_n=z^{3n-1}Q_n(z),
 \qquad 0\ne Q_n\in\mathbb Q[z],\quad\deg Q_n\le3.
\tag{3}
$$



The homogeneous-ODE note `raw_hp_homogeneous_ode.md` proves this
Wronskian factorization. Its degree bound can also be checked directly:
after removing e^z, the ordinary Wronskian of A,Be^z,C has degree at
most3n-2, because the leading terms in each A,C minor cancel. Multiplying
by D^2 gives degree at most3n+2. The remaining arctangent-derivative
terms have no larger degree. At zero, the first-column remainder jets
vanish to orders at least3n+1,3n,3n-1.

The determinant is not identically zero. A constant linear relation
between R_n,U_n,C_n would, by the logarithmic monodromy at i, first
force the coefficient of R_n to vanish. It would then make a nonzero
polynomial times e^z rational, unless its remaining two coefficients
also vanish. Since B_n and C_n are nonzero, the three analytic functions
are linearly independent.

## 2. The rational transfer and its degree bounds

Define meromorphically



$$
T_n=\Psi_{n+1}\Psi_n^{-1}=K_{n+1}K_n^{-1}.
\tag{4}
$$



For entry (r,j), r,j in {0,1,2}, Cramer's rule replaces row j of K_n
by derivative row r of K_(n+1). The resulting determinant is polynomial.
Equivalently, undoing (2), its determinant is D^2e^(-z) times the same
mixed-row determinant in the analytic jet matrices. Every first-column
remainder jet in that mixed determinant vanishes to order at least3n-1.
Therefore its polynomial numerator is divisible by z^(3n-1), and



$$
\boxed{T_n(z)=N_n(z)/Q_n(z),\qquad
 N_n\in\operatorname{Mat}_3(\mathbb Q[z]),\quad
 \deg (N_n)_{rj}\le6.}
\tag{5}
$$



This proves the absence of a pole set whose size grows with n. It does
not assert that Q_n has three distinct roots or avoids zero or one.

The row-degree bounds in K_n sharpen(5) to



$$
(\deg N_{rj})\le
 \begin{pmatrix}5&6&6\\4&5&5\\3&4&4\end{pmatrix},
 \qquad z\mid N_{r2}\quad(r=0,1,2).
\tag{6}
$$



For the degree estimate, the three mixed rows have total base degree
3n+1. Choosing first and third columns incurs derivative orders from
two distinct rows, and the first column adds4. Subtract the two smallest
available derivative orders, then subtract the common origin factor
3n-1. This gives every bound in(6) except its last entry, initially5.
For that entry, the minimum pair consists of the old derivative rows
0 and1; their leading A,C minor cancels, lowering the bound to4.
For the last-column divisibility, replacing old row2 leaves old
remainder jets only of orders0,1. Their minimum vanishing order is3n,
while the new jet has order at least3n+2. There is therefore one extra
factor z in those mixed determinants.

Taking determinants gives the exact normalization identity



$$
\boxed{\det T_n=z^3\frac{Q_{n+1}}{Q_n},\qquad
 \det N_n=z^3Q_n^2Q_{n+1}.}
\tag{7}
$$



If unnormalized triples are used instead, their scaling changes T by
the ratio of the two scales and Q by the cube of each scale. Formula(7)
remains consistent, but the normalization B_n(1)=1 is necessary for the
specific next-step construction below.

## 3. Differential compatibility

Let the exact third-order scalar equation from the ODE note be



$$
A_{3,n}y'''+A_{2,n}y''+A_{1,n}y'+A_{0,n}y=0,
 \qquad A_{3,n}=zD Q_n.
$$



Write its companion matrix as



$$
\mathcal C_n=\frac{M_n}{zDQ_n},\qquad
 M_n=\begin{pmatrix}
 0&zDQ_n&0\\0&0&zDQ_n\\
 -A_{0,n}&-A_{1,n}&-A_{2,n}
 \end{pmatrix}.
$$



The three columns of Psi_n form a fundamental matrix, so
Psi_n'=C_n Psi_n. Differentiating(4) gives



$$
\boxed{T_n'=\mathcal C_{n+1}T_n-T_n\mathcal C_n.}
\tag{8}
$$



Equivalently, this is the bounded-degree polynomial identity



$$
\boxed{zD Q_{n+1}(Q_nN_n'-Q_n'N_n)
 =Q_nM_{n+1}N_n-Q_{n+1}N_nM_n.}
\tag{9}
$$



There is also a direct rational gauge check. Put



$$
\mathcal B=
 \begin{pmatrix}-2D'/D&0&0\\0&1&0\\D&0&0\end{pmatrix}.
$$



Differentiating the universal factor SG in(2) gives



$$
\mathcal C_n=(K_n'+K_n\mathcal B)K_n^{-1}.
\tag{10}
$$



This verifies(8) without importing a sign convention from the scalar
cofactor equation. The first row of T defines a rational differential
operator of order at most2 which sends each of R_n,U_n,C_n to its
next-degree counterpart. The remaining rows are obtained by
differentiation and the current companion equation. This is an exact
differential transfer, but its coefficients are not known functions
of n until the accessory data have been determined.

## 4. A fixed-size exact construction of the next triple

There is a useful constructive consequence of(5). Given the current
normalized polynomials and their Q_n, introduce three trial polynomials
N_0,N_1,N_2, each of degree at most6. There are21 scalar unknowns.
Define rational trial next polynomials by



$$
\widehat C=\frac{N_0C+N_1C'+N_2C''}{Q_n},
$$




$$
\widehat B=\frac{N_0B+N_1(B+B')+N_2(B+2B'+B'')}{Q_n},
$$




$$
\widehat A=
 \frac{N_0D^2A+N_1(D^2A'+DC)
             +N_2(D^2A''+2DC'-D'C)}{D^2Q_n}.
\tag{11}
$$



Impose the following **linear** conditions on those21 unknowns.

1. Each expression in(11) is a polynomial of degree at most n+1.
2. The numerator N_0R_n+N_1R_n'+N_2R_n'' vanishes to order at least
   3n+4+h, where h=ord_0 Q_n<=3.
3. The polynomial quotients satisfy Bhat(1)=1 and Chat(1)=4.

All these are exact rational linear conditions. The use of polynomial
quotients in the last step is deliberate: Q_n(1) may be zero.

The system has at most29 rows, independently of n. To count them,
put q=deg Q_n<=3. The B and C numerators have degree at most n+6.
Euclidean remainder zero contributes q equations for each; the
coefficients above quotient degree n+1 contribute at most5-q more.
Thus each gives at most5 conditions. The A numerator has degree at
most n+10, with denominator of degree q+4. Its remainder and upper
quotient coefficients give at most(q+4)+(5-q)=9 conditions. The total
from polynomiality and degree is at most19.

The second condition starts at degree3n-1 automatically, since
R_n=O(z^(3n+1)). It therefore imposes at most5+h<=8 coefficients.
It uses at most the first eight unconstrained Taylor coefficients of
R_n, through degree3n+8, after the two derivatives are taken. Finally
there are two endpoint equations. This proves the row count29.

The system is consistent because the actual first row in(5) satisfies
it. It has exactly one solution. Indeed any solution of(11) has the
required next degree, remainder order and endpoint normalization;
the accepted all-degree rank theorem identifies it with the canonical
next triple. If two coefficient vectors gave this same triple, their
difference would define a rational differential operator of order at
most2 annihilating R_n,U_n,C_n. Multiplication by the invertible jet
matrix Psi_n forces all three operator coefficients to be zero.

Consequently



$$
\boxed{\text{The next actual normalized triple is recovered uniquely
 from a rational linear system of at most29 equations in21 unknowns.}}
\tag{12}
$$



This avoids a linear solve whose number of unknowns grows with n.
It still uses the current polynomial triple to form the remainder and
division data. Thus(12) is not yet a birational update in only the
cubic Q and bounded-degree scalar-ODE coefficients. Obtaining that
smaller explicit update, or controlled asymptotics for its coefficients,
is an additional mathematical problem.

## 5. Endpoint transfer, including apparent zeros at one

When Q_n(1)!=0, equation(4) directly propagates the three-jet column
(R_n,R_n',R_n'')(1) to its next-degree column with rational coefficients.
There is no current all-degree theorem that Q_n(1) is nonzero, so this
three-jet evaluation must be stated conditionally.

A uniform six-jet version avoids that issue. At z=1 the order h of the
Wronskian zero equals ord_1 Q_n and is at most3. The h-th derivative of
its determinant is nonzero. Expanding that derivative shows that some
three-by-three minor of derivative rows0,...,h+2 is nonzero. Therefore
the six-by-three jet matrix with rows0,...,5 has full column rank at1.

Remove the same universal G(1) factor from that six-row matrix and call
the resulting rational matrix H_n. Its rows are



$$
\bigl(A_n^{(r)}+
   \sum_{j=1}^r\binom rj C_n^{(r-j)}(\arctan)^{(j)},
   (D_z+1)^rB_n,C_n^{(r)}\bigr)\big|_{z=1},
 \quad0\le r\le5.
$$



All entries are rational and H_n has rank3. Its rational left inverse
L_n=(H_n^T H_n)^(-1)H_n^T consequently exists. The matrix



$$
\boxed{\mathcal T_n^{(6)}=H_{n+1}L_n\in\operatorname{Mat}_6(\mathbb Q)}
\tag{13}
$$



propagates the six endpoint jets of each actual fundamental column,
including R_n, without any condition on Q_n(1). It is a rank-three
transfer on the actual solution subspace, not an invertible map on all
six arbitrary coordinates. It uses actual coefficients; no explicit
scalar recurrence in n or asymptotic bound follows from(13) alone.

## 6. Verification and remaining limit

`check_raw_rational_transfer.py` constructs the transitions n=1 to2
and n=2 to3 through the21-unknown system, starting from the exact
normalized n=1 triple. It checks the original Taylor equations and
endpoint normalization, compares the new endpoint rational with the
frozen archive, and verifies(6), (7), and (8) by rational arithmetic.
This is a normalization control on the proof, not recurrence fitting.

The transfer gives a bounded rational differential system for the
actual family. Compatibility(9), determinant identity(7), origin order,
apparent-singularity conditions and endpoint normalization are concrete
constraints on its accessory coefficients. We have not proved that a
particular subset of those bounded algebraic conditions determines the
next accessory tuple without reference to the polynomial data, nor
identified the asymptotic modes of its endpoint products. In particular,
the construction does not establish primitive shrinking or decide the
arithmetic nature of e+pi.
