> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A cubic branch and an exact two-scalar reduction of the b=2 maximal-minor gcd

Date: 2026-09-27. Author: audit_results.
Status: FULL PASS in hp_b2_cubic_maximal_minor_independent_review.md.
No degree or prime scan is used.

This continues the independently passed
../session_20260913/hp_b2_contiguous_endpoint_arithmetic.md, Section 4.
Its actual endpoint-gcd theorem applies to p>2n+4. The present note
preserves that cutoff and does not apply its conclusion to fixed small
primes. All local equalities below concern the actual three maximal
minors in that theorem, not a substitute moment matrix.

## 1. Statement

Put


$$
H_n(x)=n![s^n]e^{xs}(1-s+s^2/2)^n,\qquad
 h=H_n(1),\quad u=H_n'(1),\quad v=H_n''(1).
$$


Use the earlier derivative combinations


$$
J_k=(x^kH_k(x))'|_{x=1},\quad
 K_k=(x^kH_k(x))''|_{x=1},\quad
 M_k=(x^kH_k(x))'''|_{x=1},
$$


and the exact integer matrix and content


$$
{\bf B}_n=
 \begin{pmatrix}H_n(1)&J_n\\J_{n+1}&K_{n+1}\\K_{n+2}&M_{n+2}\end{pmatrix},
 \qquad \Omega_n=\gcd\{\text{its three maximal minors}\}.
                                                               \tag{1}
$$


For n>=2 define the two integers


$$
D_n=2(n+1)h^2-2hu-(n-1)u^2-uv,
$$




$$
C_n=u^3+(n-2)hu^2+4h^2u-2(n+2)h^3.                \tag{2}
$$


These D_n,C_n are new local scalars, not the endpoint scalars with
similar letters in the previous note.

**Theorem.** At every prime p>2n+4,


$$
\boxed{
 v_p(\Omega_n)=
 \begin{cases}
 0,&p\mid h,\\
 \min\{v_p(D_n),v_p(C_n)\},&p\nmid h.
 \end{cases}}                                                    \tag{3}
$$


In particular p dividing Omega_n forces h and u both to be p-units.
Set z=u/h and t=n+z in this case. At every depth d>=1,


$$
p^d\mid\Omega_n
 \quad\Longleftrightarrow\quad
 D_n=0,\quad
 f_n(z)=0\pmod {p^d},
$$




$$
f_n(z)=z^3+(n-2)z^2+4z-2(n+2).                    \tag{4}
$$


Equivalently the ratio t solves the fixed-degree cubic


$$
\boxed{P_n(t)=t^3-(2n+2)t^2+(n+2)^2t
                       -2(n+1)(n+2)=0\pmod {p^d}.} \tag{5}
$$


The equivalence in (4) is asserted with h a p-unit; if p divides h,
(3) says no positive depth is possible.

For a primitive full integral b=2 endpoint-matched triple let
d_p=v_p gcd(A(1),B(1)). The previous, independently reviewed theorem
and (3) give the actual full-depth bound


$$
d_p\le v_p(\Omega_n)
$$


with the exact right-hand side (3). If d_p>0, then over Z/p^(d_p)
the exponential polynomial has the more precise form


$$
\boxed{B(z)=b_2(z-1)(z-t),\quad b_2\text{ a unit},\quad
 t=n+H_n'(1)/H_n(1),\quad P_n(t)=0.}                 \tag{6}
$$


The quantities t and t-n are units. Thus B(0) and its leading
coefficient are p-units. If additionally p does not divide
n^2+4n+1, then t-1 and B'(1) are units: the forced common endpoint
factor is simple in B modulo p. The displayed quadratic is a real
exceptional multiplier and is not omitted.

This is a necessary condition on actual endpoint cancellation, not
an equivalence between that cancellation and p dividing Omega_n.

## 2. A third-order differential identity and a primitive state

The preceding archive proves the two polynomial identities


$$
H'_{n+1}=(n+1)(H_n-H_n'+H_n''/2),
$$




$$
H_{n+1}=xH_n''/2+(n+1-x)(H_n'-H_n).
                                                               \tag{7}
$$


Differentiate the second and subtract the first. The result is


$$
\boxed{xH_n'''+(n+2-2x)H_n''
                  +2(x-1)H_n'-2nH_n=0.}            \tag{8}
$$


At x=1 this says H_n'''(1)=2nh-nv. Consequently (7) and its
derivative give the exact three-state recurrence


$$
\begin{pmatrix}H_{n+1}(1)\\H'_{n+1}(1)\\H''_{n+1}(1)\end{pmatrix}
 =T_n\begin{pmatrix}h\\u\\v\end{pmatrix},\qquad
 T_n=
 \begin{pmatrix}
 -n&n&1/2\\
 n+1&-n-1&(n+1)/2\\
 n(n+1)&n+1&-(n+1)(n+2)/2
 \end{pmatrix},
$$




$$
\boxed{\det T_n=(n+1)^4/2.}                         \tag{9}
$$


The initial state is (1,0,0). For every odd p>n, all matrices
T_0,...,T_(n-1) are invertible over Z_p. Hence


$$
\boxed{\min\{v_p(h),v_p(u),v_p(v)\}=0\quad(p>n).}    \tag{10}
$$


This is a content assertion about the full three-coordinate state;
it is stronger than assuming individual H values are nonzero.
It is also the step that prevents a spurious common zero of (2).

## 3. Exact row reduction of the actual three-row gate

Every row of B_n is a linear function of (h,u,v). The first row is
(h,nh+u). The two coefficient rows for the second row are


$$
\begin{pmatrix}
 1-n^2&n^2-1&n+1\\
 -n^3+2n^2+5n+2&n^3-n^2-3n-1&n(n+1)
 \end{pmatrix}.                                      \tag{11}
$$


They follow by multiplying the appropriate derivative rows by T_n.
For the third row, take k=n+2 and multiply


$$
\begin{pmatrix}
 k(k-1)&2k&1\\
 k(k-1)(k-2)+2k&3k(k-1)&2k
 \end{pmatrix}T_{n+1}T_n.                            \tag{12}
$$


The last 2k entry uses (8); no fourth or higher independent derivative
has been introduced.

Let I_01,I_02,I_12 be the minors in natural row order. Direct expansion
of (11)-(12) gives


$$
I_{01}=(n+1)D_n,\qquad
 I_{02}=(n+2)(2n+3)E_n,                              \tag{13}
$$


where


$$
E_n=-2n(n+2)h^2+4nhu+(n+2)hv
                    +(n^2-2n-1)u^2+nuv.
$$


The crucial homogeneous elimination identity is


$$
\boxed{uE_n+(nu+(n+2)h)D_n=-(n+1)C_n.}             \tag{14}
$$


It can be verified by collecting the five cubic monomials. Thus the
cubic arises from the actual two minors, not from a formal spectral
analogy.

We also need the following two evaluations:


$$
I_{12}|_{h=u=0}=(n+1)(n+2)^2(2n+3)v^2,             \tag{15}
$$


and the determinant of the three first-column coefficient rows is


$$
-(n+1)^2(n+2)(2n+3).                               \tag{16}
$$


All these prefactors are p-units for p>2n+4.

## 4. Proof of the exact depth formula

Suppose first p divides h. If u is a unit, then modulo p


$$
D_n=-u((n-1)u+v).
$$


If D_n vanishes, substitution v=-(n-1)u into E_n gives
E_n=-(n+1)u^2, a unit. Thus one of I_01,I_02 is a unit.
If u also vanishes modulo p, (10) makes v a unit, and (15) makes
I_12 a unit. This proves the first case of (3).

Now suppose h is a unit. Subtract t=n+u/h times the first column
from the second column of B_n. Its first row becomes (h,0).
The ideal of all three minors over Z_p is therefore precisely
(I_01,I_02): the third minor is a Z_p-linear combination of these
two by expansion against the unit h. Equations (13) give


$$
(\text{three minors})=(D_n,E_n).
$$


If u is a unit, (14) implies
(D_n,E_n)=(D_n,C_n). If u is not a unit, D_n is already a unit
because D_n=2(n+1)h^2 modulo p; C_n is a unit as well because
C_n=-2(n+2)h^3 modulo p. The same equality of unit ideals holds.
This proves (3), including every prime-power exponent, and also
proves that p dividing Omega_n forces u to be a unit.

Dividing C_n by h^3 proves (4). Substituting z=t-n gives (5).
Equation (14) is indispensable: retaining only the cubic would lose
the independent second-derivative compatibility D_n.

## 5. The actual primitive endpoint factor

Let d_p>0. In the prior proof, dividing the primitive full triple
by z-1 modulo p^(d_p) gives degree caps (n-1,1,n-1).
Its quotient exponential vector (b_0,b_1) is primitive and satisfies
B_n(b_0,b_1)^T=0 modulo p^(d_p), up to unit row scalings.
Since h is a unit, its first row forces
b_0=-t b_1. Primitivity forces b_1 to be a unit. Restoring z-1
gives (6), with b_2=b_1.

The three evaluations


$$
P_n(0)=-2(n+1)(n+2),\quad
 P_n(1)=-(n^2+4n+1),\quad
 P_n(n)=-2(n+2)
$$


give the claimed unit restrictions, with the stated exception at 1.
More generally the polynomial difference identity gives the exact
truncated restriction


$$
\min\{d_p,v_p(B'(1))\}
       \le \min\{d_p,v_p(n^2+4n+1)\}.                \tag{16a}
$$


Indeed P_n(t)=0 modulo p^(d_p) and 1-t divides P_n(1)-P_n(t).
Also B'(1)=b_2(1-t) modulo p^(d_p), with b_2 a unit.

## 6. A precise resultant and Hensel refinement, with its limitation

The cubic discriminant is


$$
\boxed{\operatorname{disc}P_n=
 4(n+2)(2n^3-12n^2-35n-22).}                         \tag{17}
$$


Thus if P_n has no root modulo a prime p>2n+4, then
p does not divide Omega_n or the actual primitive endpoint gcd.
If p also avoids (17), every possible residue t lifts to a unique
Z_p root tau of P_n. For the actual ratio t=n+u/h in that residue,
the simple-root factorization gives


$$
v_p(P_n(t))=v_p(t-\tau),\qquad
 v_p(\Omega_n)=\min\{v_p(D_n),v_p(t-\tau)\}.           \tag{18}
$$


The h^3 factor is a unit. This is an exact branch-depth formula,
not an assertion that either depth is bounded.

In particular separability of the cubic does not bound the actual
depth: it still requires controlling how closely the fixed state
ratio approaches tau and how deeply D_n vanishes. For instance the
local equations themselves allow arbitrarily precise approximations
to a simple root while solving the linear v-compatibility in D_n;
that observation is about the equations and does not construct
another actual HP index.

The cutoff cannot be discarded. At p<=n the transition determinants
in (9) need not be units, and the earlier primitive-kernel argument
also has factorial and moment losses. Equations (8)-(17) remain
algebraic identities at small primes, but (3), (6), and the actual
endpoint consequence have only the stated range. No fixed-small-prime
q lower bound or irrationality theorem is claimed.

## 7. Verification

A saved symbolic checker reconstructs (11)-(12) from T_n and verifies
(9), (13)-(17), and det(B_second-t B_first) =
(n+1)^2(n+2)(2n+3)P_n(t) with formal n,h,u,v,t.
It does not evaluate any new canonical degree or scan primes.
The proof of the valuation statement is the local ideal argument
above, not the symbolic check alone.
