> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the first matrix correction and limiting transport

Date: 2026-09-13. Reviewer: audit_results.

Reviewed raw_first_matrix_transport_correction.md in full, including
the subsequently added explicit solution in Section 7. All claims
pass the semantic audit. No correction was required. The review
uses the exact formulas and uniform estimates, not numerical rows
or an assumed asymptotic orientation.

## 1. Both channel shifts and every first-order coefficient

In boundary order (N-2,N-1), the two reversed chains have original
indices l=N-beta-2j with beta=2 and beta=1. Substituting this
expression into the exact diagonal
-l(l+1)/2+1/4+delta_l+delta_(l+1) gives

    -1/2+(beta+2j-1/2)/N+O((j+1)^2/N^2).

The coupling to the next depth is the original coupling from l
to l-2, namely a_(l-1)a_l. Its expansion is

    1/4-(beta/2+j+1/4)/N+O((j+1)^2/N^2).

For the beta=2 chain, its neighbors of opposite parity are
the beta=1 coordinates at depths j and j+1. Thus the cross block
really is -(v_j+v_(j+1))/2 at first order. Both terms and their
transpose are needed, and the note includes both.

For odd N, the longer chain has one extra low-index coordinate.
Every unmatched or omitted coupling occurs at depth comparable
to N. The weighted remainder estimate O((j+1)^2/N^2) absorbs
the constant coefficients and the O((j+1)/N) linear coefficients
there, including arbitrarily remote zero-tail rows. This verifies
the common first coefficient for both parities in boundary order.
Relabeling by absolute parity requires exactly the stated coordinate
swap, rather than claiming literal equality in different orders.

## 2. Why the localized second resolvent estimate is rigorous

On a fixed compact subset of Re c>0, the half-line boundary vector
w_j=m q^j has uniformly bounded polynomially weighted l2 norms,
because |q| is uniformly below one. Fixed bandwidth and the two
coefficient estimates therefore imply

    ||D_N w||=O(1/N),
    ||(D_N-H_1/N)w||=O(1/N^2).

The formal band action H_1 w is a well-defined l2 vector. No
resolvent or global boundedness of H_1 is invoked. The actual
B_N is bounded and self-adjoint, with its spectral upper edge
tending to zero; therefore its resolvent is uniformly bounded
on the fixed compact domain for all sufficiently large N.

The second resolvent identity

    R_N=R_0+R_0 D_N R_0+R_0 D_N R_N D_N R_0

is exact. In a boundary matrix element the last term is
(D_N w_beta)^T R_N(D_N w_gamma). It is O(1/N^2) by the two
localized norms and the global bounded resolvent. No estimate
that the resolvent itself preserves localization is needed.
Transpose symmetry correctly supplies the analytic bilinear form
in the complex parameter; its absolute value is bounded by the
product of the usual Hilbert norms. The first correction differs
from w_beta^T H_1 w_gamma/N by O(1/N^2).

Thus the far-tail error is accounted for on both sides of the
second resolvent term. The proof never claims the false global
estimate ||B_N-L_0||=O(1/N).

## 3. Independent evaluation and transfer normalization

For a diagonal block, direct geometric summation yields

    B_(beta,beta)/m^2
      =[(2beta-1)+(2beta-3)q]/[2(1+q)^2].

For the cross block, including both depths gives
B_(2,1)/m^2=-1/[2(1-q)]. These reproduce the full matrix (13).

The exact boundary coupling has the expansion

    Gamma_N/N^2=I/4+G_1/N+O(1/N^2),
    G_1=[[-1/4,0],[-1/2,1/4]].

In particular the two diagonal shifts have opposite signs. The
first correction to M_N/N^2 is B/16+(m/4)(G_1+G_1^T).
Expanding M_N^(-1)Gamma_N^T then gives the relative correction

    A=4G_1^T-[B/m+4(G_1+G_1^T)]=-4G_1-B/m.

Substitution gives exactly

    A_11=(1-4q-q^2)/(1+q)^2,
    A_22=(q^2-4q-1)/(1+q)^2,
    A_12=2q/(1-q), A_21=2/(1-q).

Using s=(1-q)/(1+q) and 4q/(1+q)^2=1/(c+1) recovers the
displayed A(c). The scale lambda=4/m=1/q is also correct.

All inversions are of two-by-two matrices with a nonzero scalar
limit on the complex compact domain. A slightly larger compact
neighborhood remains in Re c>0 and admits the same uniform
argument. Cauchy's formula therefore proves the stated derivative
bounds without differentiating an uncontrolled asymptotic estimate.

## 4. Ordered products converge at the asserted rate

At j/n=t, the exact normalized factor is
I+A(chi/t^2)/(nt)+O(1/n^2). A right-endpoint local propagator
for Y'=A(chi/t^2)Y/(2t), over mesh length 2/n, has exactly
the same first term and O(1/n^2) error. The generator and its
t derivative are uniformly bounded for t in [1,2] and chi in
a fixed compact subset of the right half-plane.

Both the exact factors and the ODE propagators, as well as their
inverses for sufficiently large n, have norms bounded by
1+C/n per step. Over O(n) steps this gives uniform product
bounds. Telescoping the ordered products gives O(1/n) uniformly
in the endpoint grid index m and chi. The inverse difference
follows by multiplication by the two bounded inverses. No
commutation of the factors is assumed.

Uniform holomorphy on a slightly larger chi compact neighborhood
then gives the same O(1/n) estimate for each of the first two
chi derivatives by Cauchy's formula. The finite-index thresholds
can depend on that larger compact set, as permitted by the
uniform-on-compacts theorem.

## 5. The explicit ODE solution and its branches

I also checked the explicit formula

    Y=f_t D_t exp(eta sigma_1) D_1^(-1),
    w_t=t/(sqrt(chi+t^2)+sqrt(chi)),
    D_t=diag(sqrt(w_t),1/sqrt(w_t)),
    eta=(t-1)/(2sqrt(chi)).

The principal square roots have a sum of positive real part, so
w_t and its square root are nonzero and holomorphic on the
specified domain. Direct differentiation gives

    (log w_t)'=sqrt(chi)/(t sqrt(chi+t^2)),
    f_t'/f_t=-t/[2(chi+t^2)].

Conjugating sigma_1 by D_t produces off-diagonal entries w_t
and 1/w_t. Multiplication by eta'=1/(2sqrt(chi)) gives the
two entries (1/s-1)/(2t) and (1/s+1)/(2t), with
s=sqrt(chi)/sqrt(chi+t^2). The diagonal terms also agree
with A(chi/t^2)/(2t). At t=1 the formula is I. Its determinant
is f_t^2=sqrt((chi+1)/(chi+t^2)), which matches the integral
of the trace of the generator.

The optional hyperbolic-variable gauge is consistent with this
direct derivative calculation and is not needed to establish
any additional continuation convention.

## 6. Scope

The result identifies the actual first matrix correction, its
uniform error, and the limiting change of orientation over a
fixed ratio of growing cuts. It does not determine the absolute
orientation from a fixed seed, nor the smallest singular value
of a growing mixed-node matrix after low-row deletion. Those
limitations remain explicit in the source note.
