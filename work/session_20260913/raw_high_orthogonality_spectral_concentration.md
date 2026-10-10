> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# High Borel orthogonality forces concentration in a sublinear Legendre band

Date: 2026-09-13. Original quantitative continuation by audit_sources.
This theorem concerns every polynomial satisfying the actual high
orthogonalities, so in particular the normalized raw polynomial. It
does not assume positivity, a Chebyshev property, a root bound, or an
upper bound for that polynomial's norm.

## 1. Statement

Let F_k be the actual raw Borel–Legendre polynomials and let

    H_n=span(F_(n+1),...,F_(2n-1)) in L2(0,1).

For P in the degree-at-most-n polynomial space suppose P is nonzero and

    integral_0^1 P(x)F_k(x) dx=0,
                    n+1<=k<=2n-1.                    (1)

Let phi_l(x)=sqrt(2l+1) P_l(2x-1), where P_l is the usual Legendre
polynomial, and let Pi_<=d denote orthogonal projection onto the first
d+1 such modes. For n>=4 and 0<=d<=n, this note proves

    ||Pi_<=d P||_2/||P||_2
      <= 4n^2 (d+1)^(7/2) sqrt(2d+1)
           8^d (2e^3)^n d!/n!.                        (2)

Put c_0=log(16e^3)=log16+3. For any fixed A>c_0, let

    w_n=ceil(A n/log(n+1)),  d_n=n-w_n,

for all sufficiently large n, when 0<=d_n<n. Then

    ||Pi_<=n-w_n P||_2/||P||_2
       <= exp(-(A-c_0+o(1))n),                        (3)

uniformly for all P satisfying (1). In particular A=8 gives an
exponentially vanishing low-mode fraction while w_n=o(n).

The endpoint normalizations are not used. Thus this is a uniform
geometric statement about the entire two-dimensional actual
high-orthogonal polynomial space, not merely a fitted description of
one selected sequence.

## 2. The previously proved approximation input

For k of parity sigma put q_(k,sigma)=[t^sigma]Q_k(t)>0 and
f_k=F_k/q_(k,sigma). Sections 2–3 of
`raw_arctan_dual_factorial_mass.md` prove that for every 0<=k<=n
there is I_(n,k) in H_n such that

    ||f_k-I_(n,k)||_infinity
       <= epsilon_n,
    epsilon_n=4n^2(2e^3)^n/n!,  n>=4.                  (4)

This follows from the explicit parity spectral interpolation and its
factorial tail. It applies to both parities, including the slightly
different retained monomial degrees for even n. No collocation sign
or Chebyshev assertion enters it.

The new step is to transfer (4) to low shifted Legendre modes while
keeping the growth of the change of basis explicit. A fixed-width
perturbation argument would lose too much; the factorial ratio below
recovers control after discarding a sublinear top band.

## 3. An explicit inverse-Borel coefficient bound

Fix l>=0. Write phi_l(x)=sum_(j=0)^l u_j x^j and define its inverse
Borel polynomial

    R_l(t)=sum_(j=0)^l j! u_j t^j.

The exact shifted Legendre coefficient formula is

    u_j=sqrt(2l+1)(-1)^(l-j)
                    binom(l,j) binom(l+j,j).

Since binom(l+j,j)<=4^l and sum_j binom(l,j)=2^l,

    sum_j |u_j| <= sqrt(2l+1)8^l,
    sup_(-1<=u<=1) |R_l(iu)|
       <= l! sqrt(2l+1)8^l =: B_l.                   (5)

Let m_k=2^k/binom(2k,k), the reciprocal leading coefficient of the
usual Legendre polynomial. The actual monic raw polynomial satisfies

    Q_k(iu)=i^k m_k P_k(u).                            (6)

Expand R_l(iu) in the ordinary Legendre basis:

    R_l(iu)=sum_(k=0)^l d_k P_k(u).

Orthogonality and |P_k(u)|<=1 on [-1,1] give

    |d_k| <= (2k+1)B_l.                               (7)

The elementary bound |P_k|<=1 follows, for example, by taking the
modulus in the integral representation
P_k(u)=pi^(-1) integral_0^pi
(u+i sqrt(1-u^2)cos theta)^k dtheta; the integrand has modulus at most
one. Thus no growing-degree norm-equivalence constant is hidden in
(7).

If R_l(t)=sum c_k Q_k(t), equation (6) gives
c_k=d_k/(i^k m_k). At an even k the ratio q_(k,0)/m_k is |P_k(0)|<=1.
At an odd k it is |P_k'(0)|<=k, using
P_k'(0)=k P_(k-1)(0). Therefore

    |c_k q_(k,k mod2)| <= (2k+1)max(1,k) B_l.

Applying the Borel transform now gives the exact expansion

    phi_l=sum_(k=0)^l a_(l,k) f_k,
    a_(l,k)=c_k q_(k,k mod2),

with the bound

    sum_(k=0)^l |a_(l,k)|
      <= (l+1)^3 sqrt(2l+1)8^l l!.                    (8)

Indeed sum_(k=0)^l (2k+1)max(1,k)
=1+l(l+1)(4l+5)/6 <=(l+1)^3. The coefficients may be written using
complex intermediate expressions, but the final polynomial expansion
is real because both bases are real and linearly independent. Only
their absolute values are needed.

## 4. Approximation of an entire low spectral block

For l<=n define

    A_(n,l)=sum_(k=0)^l a_(l,k) I_(n,k) in H_n.

Combining (4) and (8) yields

    ||phi_l-A_(n,l)||_2
      <= ||phi_l-A_(n,l)||_infinity
      <= epsilon_n (l+1)^3 sqrt(2l+1)8^l l!.          (9)

Let p_l=<P,phi_l>. Since P annihilates H_n,

    |p_l|=|<P,phi_l-A_(n,l)>|
      <= ||P||_2 epsilon_n
                    (l+1)^3 sqrt(2l+1)8^l l!.

The last factor is nondecreasing with l. Summing its square for
0<=l<=d and taking a square root gives exactly (2). This argument
requires no inversion of the monomial Gram matrix and no lower bound
for a growing determinant.

For d=n-w with w=o(n), the elementary factorial estimate is

    log(d!/n!)=-w log n+O(w^2/n+w/n).

The polynomial factor in (2) has logarithm O(log n), and

    d log8+n log(2e^3)<=n log(16e^3)=c_0 n.

With w=ceil(A n/log(n+1)), these estimates give (3). The error is
uniform in P because every previous bound was uniform in P and its
nonzero norm was divided out only once.

## 5. Absolute endpoint weights also concentrate

At either endpoint, |phi_l(0)|=|phi_l(1)|=sqrt(2l+1). Define the
absolute endpoint-weighted tail ratio

    eta_(n,d)=
      sum_(l=0)^d sqrt(2l+1)|p_l|
       /sum_(l=0)^n sqrt(2l+1)|p_l|.

The denominator is at least ||P||_2. Cauchy–Schwarz and
sum_(l=0)^d(2l+1)=(d+1)^2 give

    eta_(n,d) <= (d+1)||Pi_<=d P||_2/||P||_2.          (10)

Thus the same sublinear window has exponentially small absolute
endpoint-weighted mass outside it. This says nothing about signed
cancellation in P(0) or P(1). In particular it does not lower-bound
|sum p_l phi_l(0)| relative to the sum of absolute terms.

The statement is unchanged by reflection x->1-x or by replacing each
Legendre basis vector with its negative: those operations multiply
individual modal coefficients by signs and preserve both the low
spectral subspace and all bounds here.

More precisely, in the coordinate used here put

    kappa_n=|P(0)|/sum_l sqrt(2l+1)|p_l|.

If P(0)!=0, the endpoint identity
phi_l'(0)=-l(l+1)phi_l(0) gives

    |P'(0)/(n(n+1)P(0))+1|
       <= (2w/n+eta_(n,n-w))/kappa_n.                 (11)

To verify the bound, split the signed endpoint sum at l=n-w. On the
top band, the relative eigenvalue defect
[n(n+1)-l(l+1)]/[n(n+1)] is at most 2w/n; on the remaining modes it
is at most one. Divide their absolute weighted sums by the signed
endpoint value. Thus, with the window proved here, the separate
condition kappa_n log n tending to infinity would suffice to make
the left side of (11) tend to zero. A fixed positive lower bound on
kappa_n is stronger than necessary. No such lower bound or limiting
condition is proved here. Reflection changes the derivative sign as
usual; the corresponding raw B-coefficient quotient must retain the
coordinate convention of its own note.

## 6. Consequences and limitations

The requested sublinear-band concentration is proved. It is compatible
with the endpoint-functional normalization forcing cancellation
between the top adjacent modes. It does not assert domination by the
single top mode, by any fixed number of modes, or concentration in a
window of logarithmic or square-root width.

In particular this theorem does not bound ||P_n||, the angle between
the two projected endpoint functionals, or the inverse-Gram residual.
The selected vector can still have an extremely large normalization
inside the concentrating band. It also does not estimate signed
endpoint cancellation, the whole-remainder cancellation ratio, or the
primitive rational denominator.

There is a direct obstruction to obtaining endpoint noncancellation
from high orthogonality alone. The exact rank theorem makes the
degree-at-most-n high-orthogonal space two-dimensional. Evaluation at
either endpoint is one linear functional on that space, so it always
has a nonzero vector in its kernel. Such a vector still satisfies the
concentration theorem but has complete endpoint cancellation. Any
positive endpoint-angle bound must therefore use the actual endpoint
selection in addition to the high rows; it cannot hold uniformly on
the full space covered by this theorem.

For the banded transfer and accessory-root-sum work, (10) supplies the
absolute weighted-tail part of a potential endpoint estimate. A
separate quantitative noncancellation statement for the signed endpoint
sum is still needed. The previously disproved Chebyshev shortcuts are
not revived or used.

Independent verification: audit_computations checked the inverse-Borel
expansion, the imaginary-axis normalization in both parities, the
coefficient-sum constant, the all-l and all-P quantifiers, the modal
square summation, and the sublinear-window asymptotic. It accepted the
proof with no substantive gap. No finite numerical experiment is used
as evidence for the all-index concentration assertion.
