> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Coordinator proposal: the first lifted low block is independent of Q modulo 9

2026-10-04, ongoing research. For independent audit, not a final q-law.

Use A1turn6/A4turn7's exact class n=4^j+1,
3^h>=3n-2, 3^h<=4n-3, m=(n-1)/2,
r=(3^h-1)/2, tau=r-(n-2), s=2n-2-r, d=m+1-s.
Write H=3^(h-1), so d=(3H-3n+4)/2,
s=(4n-3-3H)/2 and r1=(H-1)/2.

The actual class has s>=1. Indeed s=0 would require
3^h=4n-3=4^(j+1)+1. Modulo 3, the right side equals 2 while
the left side is 0. The low block consists of degrees 0,...,d-1.
For i,j in this block, the exact quotient
C_ij=(Q f_i f_j-Q(-1)f_i(-1)f_j(-1))/(y+1)
has degree <=n+i+j-1<=n+2d-3. But
r-(n+2d-3)=s>=1. Thus [y^r]C_ij=0 EXACTLY,
independently of every coefficient of Q. Its divided coefficient is zero.

Also the next denominators of depth h-1 include only H itself on this
class. The candidate 5H satisfies 5H>4n-3 because
3H>=3n-2 gives 5H>=5n-10/3>4n-3 for n>=5;
7H is larger. Consequently the low-block Schur matrix S in A4turn7 has

  Sbar_ij = 4 ulambda u [y^r1] (y-1)^(n-2) f_i f_j, 0<=i,j<d.

No Q-modulo-9 digit is required for this FIRST lifted low block.
The eliminated cross correction is divisible by 9 before division by 3,
as already proved by A4. Further lifted layers can still depend on Q digits.

The endpoint basis is a unit-triangular change from monomials. Thus this
residue block is congruent, up to a scalar unit, to

  H_ij=[y^(r1-i-j)](y-1)^A, A=n-2.

Reversing rows turns its unsigned binomial part into a Toeplitz binomial
matrix with L=r1-d+1=(3n-2H-3)/2. The familiar determinant product is

  product_(i=0)^(d-1) ((A+i)! i!)/((L+i)! (A-L+i)!).

Signs are units and do not affect 3-valuations. This is a classical
binomial determinant, to be reused and verified with its nonnegative
factorial range, not claimed as new. A single bounded arithmetic check
of this product at n65,d26,A63,r1=40,L15 has v3=9, hence the proposed
Sbar is singular there. This product valuation is a property of an integer
representative of Sbar; it is NOT the valuation of the ACTUAL lifted S.

The distinguished inverse entry also changes under the endpoint basis:
if f=C monomials in column convention, then C^T v=e0 gives
v_i=(-1)^i. Therefore the relevant inverse contraction in monomial
coordinates is v^T H^-1 v, not H^-1_00. Cofactor S^(0) comes from the
endpoint-zero polynomials (y+1)y^i and has the modified weight
(y+1)^2(y-1)^A. Retain this coordinate under any Smith calculation.

New task: audit this simplification, derive exact rank and endpoint cofactor
information for this binomial residue matrix on an explicit infinite class,
then identify what genuinely remains at the NEXT lift. A singular residue
does not permit subtracting determinant lower bounds to infer an actual q.
