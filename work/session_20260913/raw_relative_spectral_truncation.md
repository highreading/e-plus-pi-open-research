> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A relative bound for truncating the actual spectral high-row equations

Date: 2026-09-13. Root continuation. This deduction uses the actual
spectral amplitude theorem and the new shifted branch positivity
theorem. It controls an omitted spectral tail relative to two actual
retained column values. It does not prove a finite matrix inverse bound.

Use real orthonormal prolate eigenfunctions psi_l with the positive
central-coordinate phases. Put

    u_k(l)=<E_k,psi_l>=g_l p_k^(l mod2)(xi_l).

For k>=1 and l>=1, the shifted positivity theorem proves u_k(l)>0.
The fixed positive row and branch normalization factors do not alter
ratios within a parity branch. The exceptional zero odd branch at k0
will not be used below.

Let Q_<=n be the spectral projection onto psi_0,...,psi_n, and let
P be any polynomial of degree at most n. The polynomial convention
in the plus high equations is the original U; reflected polynomials
use reflected test functions. Reflection commutes with Q and changes
only spectral signs, so every absolute estimate below is identical
in either convention.

## 1. Uniform same-parity high-row ratio

The proved amplitude asymptotic gives an integer L such that

    g_(l+2)/g_l <=1/(32l²) for every l>=L.             (1)

Here1/32 is an eventual bound, twice the limiting constant1/64.
No claimed explicit numerical L is needed for this asymptotic theorem.
For n sufficiently large, k in{n+1,...,2n−1}, and l>=n−1,
the shifted positivity theorem and degree caps give

    p_k^sigma(xi_(l+2))/p_k^sigma(xi_l)
     <=[((l+2)(l+3))/(l(l+1)−1/4)]^(n−1)
     <=(1+6/l)^(n−1) <=exp(6).                       (2)

The elementary middle inequality holds for every l>=1: after clearing
positive denominators it reduces to
2l²−l/4−3/2>=0. The last step uses n−1<=l.
Combining (1)-(2), set C0=exp(6)/32 and obtain

    0<u_k(l+2)<=C0 l^(−2) u_k(l),
          n+1<=k<=2n−1, l>=n−1.                     (3)

This is uniform over the whole growing high-row block. It is stronger
than merely knowing that each branch value has some exponential bound.

## 2. Tail norm relative to the two retained endpoint columns

Put

    q_n=C0/(n−1)²,
    d_(k,n)=sqrt(u_k(n−1)²+u_k(n)²)>0.

For all sufficiently large n we have n−1>=L and q_n<=1/2.
Start the two parity chains at l=n−1 and l=n. Repeated application
of (3) and summation of their two geometric upper bounds give

    ||(I−Q_<=n)E_k||²
      =sum_(l>n)u_k(l)²
      <=[q_n²/(1−q_n²)] d_(k,n)².                  (4)

In particular this is O(n^-4) times the squared norm of those actual
two column entries, uniformly in k. No spectral coefficient has been
replaced by an unrelated absolute upper bound in the denominator.

The independent spectral-projection theorem gives, for every P of
degree at most n,

    ||(I−Q_<=n)P||<=||P||/(16n+15).                  (5)

Consequently Cauchy-Schwarz proves the absolute omitted-series bound

    sum_(l>n)|<P,psi_l>u_k(l)|
      <= [q_n/((16n+15)sqrt(1−q_n²))]
                                 ||P|| d_(k,n).      (6)

Its prefactor is O(n^-3), uniformly for all the actual high rows.
This proves controlled truncation, rather than setting the tail to
zero because P has finite polynomial degree. The latter would still
be incorrect.

## 3. A finite residual with a quantitative, normalized error

Suppose now that P is in the actual original high kernel, so
<P,E_k>=0 for n+1<=k<=2n−1. Write a_l=<P,psi_l>. Define the finite
row-normalized matrix

    Mtilde_(k,l)=u_k(l)/d_(k,n),
       n+1<=k<=2n−1, 0<=l<=n.                        (7)

Its final two entries in every row have squared sum one. Equation(6)
shows exactly that

    Mtilde (a_0,...,a_n)^T =r,
    ||r||_2 <=sqrt(n−1) q_n/[(16n+15)sqrt(1−q_n²)]
                                     *||P||
             =O(n^-5/2)||P||.                       (8)

Also ||(a_0,...,a_n)||>=sqrt(1−(16n+15)^−2)||P||.
The reflected convention has an additional diagonal sign matrix on
these columns and on the omitted series; all bounds are unchanged.

This gives an explicit finite spectral matrix target with a rigorously
controlled residual. It does not establish that its rows are independent
or that its smallest singular value is bounded below.

For clarity, a useful conditional implication is available. If Mtilde
has full row rank and its smallest singular value is at least c/n²
for a fixed c>0, its pseudoinverse gives a vector in ker Mtilde within
O(n^-1/2)||P|| of the retained coefficient vector. This error is
itself o(sqrt(log n/n))||P||. To infer the desired top-two concentration,
one would additionally need that finite kernel's corresponding
low-coordinate bound. Neither assertion is proved here. The relative
truncation estimate removes the previously uncontrolled infinite tail;
it does not solve the remaining finite cofactor problem.

## 4. Dependencies and verification scope

The inputs are raw_spectral_amplitude_factorial_theorem.md,
raw_branch_shifted_positivity_theorem.md, and the uniform projection
bound in raw_boundary_free_moment_intertwiner.md. The proof consists
of their uniform inequalities, an elementary rational inequality, and
two geometric series; it requires no new canonical degree or numerical
sample. The constants in(6)-(8) are explicit once an eventual amplitude
threshold L from(1) is chosen. This note makes no assertion about the
primitive denominator or the signed whole remainder.
