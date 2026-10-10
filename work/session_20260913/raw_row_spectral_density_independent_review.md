> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: row spectral law and adjacent determinant rate

Date: 2026-09-13. Reviewer: audit_sources.

**Result: pass; the notation clarification was incorporated.** I
checked `raw_row_spectral_density_and_determinant_rate.md` against
the exact matrix and Casoratian formulas in
`raw_branch_boundary_pencils_and_casoratian.md`. The density,
transform, and determinant exponent are correct. The 2-by-2
branch matrix P_N is in the symmetric row normalization; P_N
itself is not generally symmetric. The author has clarified that
wording in Section 3. This does not change any formula.

## 1. Exact finite trace expansion

The actual matrix entries are

    K_(j,j)=a_j^2+a_(j+1)^2-j(j+1),
    K_(j,j+1)=-a_(j+1),
    K_(j,j+2)=a_(j+1)a_(j+2),

where a_0=0 and a_j=j^2/sqrt(4j^2-1). The expansion
a_j=j/2+O(1/j) gives, uniformly for 0<=j<N,

    K_(j,j)/N^2 = -(j/N)^2/2+O(1/N),
    K_(j,j+2)/N^2 = (j/N)^2/4+O(1/N),
    K_(j,j+1)/N^2 = O(1/N).

The finitely many small indices fit these uniform error bounds
by enlarging an absolute constant. The same bounds hold when a
path visits an index within a fixed distance of j.

For each fixed moment order m, the trace is a sum over at most
5^m step patterns, each confined within 2m of its initial index.
Uniform boundedness of the scaled entries makes the contribution
of O(m) boundary starting indices O_m(1/N). For interior starts,
replacing each entry by the displayed local coefficient changes
the finite product sum by O_m(1/N). The remaining normalized
trace is a Riemann sum of the constant-coefficient closed-path
sum. Its Fourier representation is the angular average of

    [-t^2/2+(t^2/4)(exp(2i theta)+exp(-2i theta))]^m
      =[-t^2 sin^2(theta)]^m.

Integration over t in [0,1] gives precisely

    (-1)^m binom(2m,m)/(4^m(2m+1)).

The m=0 case is the total mass one. The previously reviewed
spectral enclosure gives common compact support. Polynomial
approximation on a compact interval therefore turns the moment
convergence into weak convergence. The explicit law
X=-T^2 sin^2(Theta) has those moments and is compactly supported;
no noncompact moment-determinacy theorem is being invoked.

## 2. Density and transform

Conditional on Theta, Y=T sin(Theta) is uniform on
[0,sin(Theta)], apart from the two probability-zero endpoints of
Theta. Its density for 0<y<1 is

    (1/pi) integral_(arcsin y)^(pi-arcsin y) csc(theta) dtheta
      = (2/pi) arcosh(1/y).

Changing variables x=-y^2 divides this density by 2y and gives

    rho(x)=arcosh(1/sqrt(-x))/(pi sqrt(-x)), -1<x<0.

The conditional representation proves normalization and absence
of endpoint atoms directly. In particular the divergence of the
density at zero is integrable and does not represent an atom.

For c>0, the angular integral of
1/(c+t^2 sin^2(theta)) is
1/(sqrt(c)sqrt(c+t^2)). Its remaining integral over t in [0,1]
is asinh(1/sqrt(c))/sqrt(c), as claimed. Positivity, or the
uniform bound 1/c, justifies the integrations and order changes.

## 3. Casoratian scale and the logarithmic limit

The reviewed exact identity in symmetric row normalization is

    det(K_N-xI)=c_N det P_N(x),
    c_N=product_(j=0)^(N-1) a_(j+1)a_(j+2)>0.

Taking absolute values at x=cN^2 gives equation (4) once
cN^2 exceeds the largest eigenvalue. The sign (-1)^N is thereby
handled correctly. The row compression has size N, and its
corresponding branch rows are N and N+1, so the product endpoints
and determinant dimension are consistent.

Since

    log a_j = log(j/2)-0.5 log(1-1/(4j^2)),

the error term is summable. Consequently

    log c_N=log(N!)+log((N+1)!)-N log 4+O(1)
      =2N log N-(2+log 4)N+O(log N).

Writing the numerator determinant as a product over the scaled
eigenvalues gives exactly

    (1/N)log|det P_N(cN^2)|
      =2+log 4+integral log(c-x) dmu_N(x)+O(log N/N).

For c in any compact interval [c0,c1] inside (0,infinity), all
sufficiently large spectral supports lie below c0/2. The
logarithm and its c derivative are uniformly bounded on that
common compact support. Weak convergence gives pointwise
convergence; the common Lipschitz bound and a finite mesh in c
give uniform convergence. The proof does not assert convergence
uniformly down to c=0.

## 4. Evaluation of the exponent

Differentiating the limiting logarithmic integral gives the
transform from Section 2. The proposed expression

    S(c)=2 asinh(sqrt(c))
          +2 sqrt(c) asinh(1/sqrt(c))

has exactly this derivative: the two algebraic derivative terms
cancel. As c tends to infinity, both this expression and the
logarithmic integral plus 2+log 4 equal
log c+2+log 4+o(1). This fixes the integration constant.

The alternative integral 2 integral_0^1 asinh(sqrt(c)/t) dt
also evaluates to S(c) by integration by parts; the omitted
boundary term is t log(1/t), which tends to zero. Thus S(c)>0
for c>0 and all constants in the determinant exponent agree.

Passing to the actual rational branch normalization changes the
determinant by the factor sqrt((2N+1)(2N+3))/sqrt(3), or its
reciprocal depending on direction. Its logarithm is O(log N),
so the same exponential rate follows.

## 5. Scope

The result concerns the eigenvalue distribution of the symmetric
five-diagonal row compression and the determinant of its two
adjacent branch rows. These eigenvalues are not the roots of
the degree-three accessory polynomial, and the density does
not impose a sign condition on those cubic roots.

The determinant rate alone does not specify the two separate
singular-value rates. A separately proved subexponential bound
on the condition number would do so. Nor does the theorem
bound a growing matrix of evaluations at distinct nodes, the
actual high-row remainder cofactors, or the primitive endpoint
gcd. Those distinctions are correctly retained in the note.

No new numerical spectral computation was used in this review.
