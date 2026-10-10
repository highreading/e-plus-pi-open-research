> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The terminal monic norm as an exact ternary digit-sum identity

Coordinator author application, October5,2026; review pending. The starting
norm formula is the already derived exact Jacobi norm in A1 prior turn21,
equation3, for the original base weight t^(-1/2)(1-t)^A on(0,1). That
classical norm and Legendre factorial valuations are reused. Focused searches
of the A1 continuation reports found the general norm formula but no displayed
terminal digit-sum specialization below. No novelty claim is made for Jacobi
orthogonality, the half-gamma formula, or Legendre's theorem.

For the retained monic polynomial p_s and its leading normalization L_s,

h_s=Gamma(s+A+1)Gamma(s+1/2)/
 [(2s+A+1/2)s!Gamma(s+A+1/2)L_s^2],
L_s=Gamma(2s+A+1/2)/[Gamma(s+A+1/2)s!].

Substitute Gamma(q+1/2)=(2q)!sqrt(pi)/(4^q q!). Every sqrt(pi) and
nonintegral parameter cancels. The EXACT rational result is

h_s=2*4^(2s+A)*(2s)!*(2s+2A)!*((2s+A)!)^2 /
 [(4s+2A+1)*((4s+2A)!)^2].                       (1)

For m=(A+1)/2, this gives

v3(h_m)=v3((A+1)!)+v3((3A+1)!)+2v3((2A+1)!)
       -2v3((4A+2)!)-v3(4A+3).                 (2)

On the actual original resonance family, 3^5 divides A, so v3(4A+3)=1.
Using Legendre v3(N!)=(N-s3(N))/2, the linear N terms cancel exactly.
Since 3 divides A,

s3(A+1)=s3(A)+1,
s3(3A+1)=s3(A)+1,
s3(2A+1)=s3(2A)+1,
s3(4A+2)=s3(4A)+2.

For any3-divisible A, the last term is -v3(4A+3). On the actual
family v3(A)=5, that term is exactly -1. Therefore the terminal norm valuation is

v3(h_m)=s3(4A)-s3(A)-s3(2A)-1.                (3)

This is a valuation of the ACTUAL monic Jacobi norm, retaining all
factorial cancellations. It is not a monomial-coordinate Smith invariant.
No claim of an integral change of orthogonal basis is being made.

Let H=3^N (N=h-1), A=H-D with0<D<H/972 as in the original domain.
For1<=q<=4, qD<H, and complement digit identities give

s3(A)=2N-s3(D-1),
s3(2A)=1+2N-s3(2D-1),
s3(4A)=1+2N-s3(4D-1).

In the third line 4A=3H+(H-4D), and3H is a single digit above the
complement block, so its digit sum is1. Thus equivalently

v3(h_m)=-2N-1+s3(D-1)+s3(2D-1)-s3(4D-1).      (4)

On the quantitative family v3(A)=5, N>5, hence v3(D)=5. Write D=3^5 e.
Then

v3(h_m)=-2N+9+s3(e-1)+s3(2e-1)-s3(4e-1).      (5)

These formulas simplify one missing scalar valuation in the terminal
Wronskian identity. They do not evaluate that Wronskian, remove monomial
inverse losses, or repair the actual precision of only3^6. A1 turn21's
accepted integral elimination already says the first residual digit at that
precision is undetermined. It must be reused rather than ignored simply
because the norm can now be expressed without gamma functions.
