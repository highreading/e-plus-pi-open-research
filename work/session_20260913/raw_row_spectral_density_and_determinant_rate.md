> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Explicit row spectral density and the adjacent determinant's exponential rate

Date: 2026-09-13. Original root derivation by finite traces.
Independent review requested. This concerns the row compression K_N
and the adjacent branch determinant; it does not concern the
roots of the accessory cubic Q_n.

## 1. A compactly supported limit from exact finite traces

Let mu_N be the probability measure giving mass 1/N to each
eigenvalue of K_N/N^2, counted with multiplicity. The reviewed
spectral enclosure puts its support in

    [-1+3/(8N^2), 1/N+3/(4N^2)].

For every fixed integer m>=0,

    lim integral x^m dmu_N(x)
      =(-1)^m binom(2m,m)/(4^m(2m+1)).             (1)

Proof. At row k with k/N -> t, the diagonal and distance-two
entries of K_N/N^2 tend respectively to -t^2/2 and t^2/4.
The distance-one entries tend uniformly to zero. These assertions
follow directly from a_j=j/2+O(1/j), with the finitely many
small j included in a uniform O(1/N) coefficient error.

Expand trace(K_N/N^2)^m as closed paths of length m in the
five-diagonal matrix. There are only finitely many step patterns
for fixed m, and each visits indices within 2m of its starting
row. Starting rows within 2m of either boundary contribute O(1/N)
to the normalized trace, since all matrix entries are uniformly
bounded. For the remaining rows, the local coefficient products
converge uniformly to the constant-coefficient closed-path sum
at t. The Riemann sum limit is therefore

    integral_(0)^1 integral_(0)^(2pi)
       [-t^2/2+(t^2/4)(exp(2i theta)+exp(-2i theta))]^m
                           dtheta/(2pi) dt.

The bracket is -t^2 sin^2(theta). Its angular moment is
(-1)^m t^(2m) binom(2m,m)/4^m, proving (1).

Uniform compact support and polynomial approximation now give
weak convergence to the law of

    X=-T^2 sin^2(Theta),

where T is uniform on [0,1] and Theta is independent and uniform
on [0,pi]. This last representation identifies all the moments
in (1), so no unproved moment-determinacy assumption is needed.

## 2. The explicit density and Stieltjes transform

The limiting probability measure has density

    rho(x)= arcosh(1/sqrt(-x))/(pi sqrt(-x)),
                     -1<x<0,                     (2)

and zero density elsewhere, with no endpoint atoms.

Indeed Y=sqrt(-X)=T sin(Theta) has density

    f_Y(y)=(1/pi) integral_(arcsin y)^(pi-arcsin y)
                       dtheta/sin(theta)
           =(2/pi) arcosh(1/y), 0<y<1.

Changing variables x=-y^2 proves (2). Conditional uniform
distributions also show directly that the law has total mass one
and no endpoint atoms.

For c>0 its Stieltjes transform is

    integral dx rho(x)/(c-x)
       =asinh(1/sqrt(c))/sqrt(c).                  (3)

To check it, first integrate 1/(c+t^2 sin^2 theta) in theta,
giving 1/(sqrt(c)sqrt(c+t^2)); the t integral is (3).
All integrands are positive and bounded for fixed c>0, so these
integrations and changes of order are justified.

## 3. Exact determinant identity and its limiting rate

Let P_N(x) be the two-by-two branch matrix in the symmetric row
normalization, with rows R_N(x),R_(N+1)(x), and put

    c_N=prod_(j=0)^(N-1) a_(j+1)a_(j+2).

The independently reviewed Casoratian identity gives

    |det P_N(cN^2)|=det(cN^2 I-K_N)/c_N           (4)

for every fixed c>0 and all sufficiently large N. Its numerator
is positive once cN^2>N+3/4. The coefficient expansion

    log a_j=log(j/2)+O(j^(-2))

has summable error, and hence

    log c_N=log(N!)+log((N+1)!)-N log4+O(1)
            =2N log N-(2+log4)N+O(log N).         (5)

Taking logarithms in (4), using (5) and the weak limit in Section 1,
gives

    lim (1/N)log|det P_N(cN^2)|
       =2+log4+integral log(c-x)rho(x)dx
       =S(c),                                    (6)

where the explicit answer is

    S(c)=2 asinh(sqrt(c))
            +2 sqrt(c) asinh(1/sqrt(c)).           (7)

The convergence in (6) is uniform for c in each compact subset
of (0,infinity): the logarithms and their c-derivatives are
uniformly bounded on the common spectral support for large N,
and compact-parameter approximation follows from the weak limit.

One way to evaluate (6) is to differentiate in c and use (3).
The derivative of (7) is exactly asinh(1/sqrt(c))/sqrt(c).
Both sides of (6) behave as log c+2+log4 when c tends to infinity,
which fixes the integration constant. Equivalently,

    S(c)=2 integral_(0)^1 asinh(sqrt(c)/t) dt,

and integration by parts gives (7); t log(1/t) tends to zero at
the lower endpoint.

The rational branch normalization changes log|det| by only
O(log N), so the same exponential rate holds there.

## 4. Scope of the result

The limit is an exact statement about the combined adjacent
determinant, and supplies its sharp exponential rate on a positive
growing parameter scale. It is consistent with the local forward
factor lambda(c)=(sqrt(c)+sqrt(c+1))^2 being studied separately.
It does not by itself assign this rate equally to the two singular
values; that needs a subexponential condition-number estimate.

It also does not control the high-row remainder matrix A_rem or
the gcd of the primitive endpoint forms. The eigenvalues here
are those of the real symmetric row matrix, and are unrelated to
an assertion that the accessory cubic has only negative roots.

The general qualitative framework is the slowly varying block
recurrence theory reviewed in matrix_orthogonal_ratio_literature.md.
The density and determinant rate above have been derived directly
from this family's finite coefficients and trace identities.
