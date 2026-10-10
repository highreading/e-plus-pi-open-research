> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Global corrected transport: a summable remainder and fixed-cut orientation

Date: 2026-09-13. Original continuation by audit_sources.
Independent review: `raw_global_corrected_transport_independent_review.md`
passes the full theorem and the diagonal product constants.

Subsequent quantitative continuation:
`raw_quantitative_fixed_cut_transport.md` proves the stronger
fixed-J error O_K(log(N)/N), with parameter derivatives. The
argument here establishes the underlying summable remainder
and qualitative fixed-cut orientation; its statements that no
N-rate is supplied refer to this original argument alone.

This note makes the first matrix correction uniform as c tends
to infinity, retains a necessary extra bound on its upper-right
entry, and then factors out the explicit cocycle F. The resulting
step errors are O(j^-2), uniformly at every preceding cut when
Re x>=aN^2. Consequently the corrected transport from J to N is
I+O(1/J), including parameter derivatives. For each fixed J it
also has a concrete positive diagonal limit as x=chi N^2 tends
to infinity. This goes beyond a compact-ratio dyadic estimate.

All matrices use the symmetric row normalization and boundary
order from `raw_first_matrix_transport_correction.md`. The proof
below does not use a crude bound on the condition number of F;
that bound would lose the summability needed at small cuts.

## 1. Uniformity on an unbounded right half-plane

Fix a>0 and put H_a={c:Re c>=a}. Use the principal branches

    q=(sqrt(c+1)-sqrt(c))^2, m=4q, lambda=1/q.

The following estimates are uniform on H_a:

    |q(c)|<=q(a)<1,
    1/(|c|+1)<=|m(c)|<=1/|c|.                          (1)

For the first inequality, write q=r exp(i theta), with r<1
as previously proved. The identity q+q^(-1)=4c+2 gives
(r+r^(-1))cos(theta)>=4a+2, and hence
r+r^(-1)>=4a+2. Its smaller positive solution is q(a).
For the lower m bound use
|sqrt(c+1)+sqrt(c)|^2<=4(|c|+1). For the upper bound,
m is the boundary entry of (cI-L)^(-1), whose norm is at most
1/|c| because spec L is contained in [-1,0] and Re c>0.

Let R_j(c) be the resolvent of the actual embedded K_j/j^2.
For all sufficiently large j depending only on a,

    ||R_j(c)||<=2/|c|, c in H_a.                       (2)

Indeed its positive eigenvalues are at most 1/j+3/(4j^2),
which is eventually at most a/2. Their distance from c is
at least |c|/2 by the triangle inequality; negative eigenvalues
have distance at least |c|. The zero-tail eigenvalues cause no
problem. This proves a bound in |c|, rather than the weaker
bound in Re c that would not suffice for the following scaling.

The geometric boundary vectors w_k=m q^k and every fixed
polynomially weighted norm of them are O_a(1/|c|) by (1).
Apply the weighted perturbation bounds and the exact second
resolvent identity from the first-correction proof. The linear
coefficient remainder is O_a(1/(|c|^2 j^2)); the quadratic
resolvent term is O_a(1/(|c|^3 j^2)) by (2). Thus the full
boundary compression has the more informative uniform expansion

    R_j^bd(c)=m(c)I+B(c)/j+E_j^bd(c),
    ||E_j^bd(c)||<=C_a/(|c|^2 j^2),                    (3)

where B is the explicit matrix in (13) of the first-correction
note. In particular ||B/m||=O_a(1/|c|). Dividing (3) by m
and using (1) gives

    R_j^bd(c)/m=I+(B/m)/j+O_a(1/(|c|j^2)),
    (R_j^bd(c)/m)^(-1)
       =I-(B/m)/j+O_a(1/(|c|j^2)).                    (4)

The inverse follows uniformly for large j by a Neumann series;
the quadratic error from B/m also has the stated bound because
|c|>=a.

## 2. The upper-right remainder keeps an extra factor

There is an exact useful factorization of the transfer. Let
G_j=Gamma_j/j^2, a lower triangular matrix. Since
M_j=Gamma_j^T R_j^physical Gamma_j, one has exactly

    T_j(x)=Gamma_j^(-1)(R_j^physical)^(-1).

At x=cj^2, this becomes

    Q_j(x):=T_j(x)/lambda(c)
        =(G_j^(-1)/4)(R_j^bd(c)/m)^(-1).                (5)

The first factor is lower triangular at every j and satisfies
G_j^(-1)/4=I-4G_1/j+O(j^-2), with the constant G_1 from the
first-correction note. Equations (4)-(5) prove

    Q_j(x)=I+A(c)/j+E_j(c),
    ||E_j(c)||<=C_a/j^2,
    |(E_j(c))_12|<=C_a/(|c|j^2), c=x/j^2 in H_a.        (6)

The final bound is essential. The upper-right entry of the
lower triangular factor in (5) is exactly zero, so the error
there comes only from the 1/|c| terms in (4). It does not
contain the unsuppressed lower triangular O(j^-2) remainder.

All statements in (3)-(6) are analytic estimates on H_a and
hold on its interior with holomorphic dependence on c. There
is no fixed upper bound on |c|.

## 3. The reference cocycle has the same entrywise error

Use the explicitly proved cocycle

    w(t,x)=t/(sqrt(x+t^2)+sqrt(x)),
    D(t,x)=diag(sqrt(w(t,x)),1/sqrt(w(t,x))),
    F(t,x)=(x+t^2)^(-1/4)D(t,x)
                        exp(t sigma_1/(2sqrt(x))),
    sigma_1=[[0,1],[1,0]],                              (7)

with the principal branches specified in that proof. It satisfies

    partial_t F(t,x)=[A(x/t^2)/(2t)]F(t,x).

For j>=4 put Z_j(x)=F(j,x)F(j-2,x)^(-1). On the interval
j-2<=t<=j, assume c=x/j^2 in H_a. The explicit A formula gives

    ||A(c)||+||cA'(c)||<=C_a,
    |A_12(c)|+|cA_12'(c)|<=C_a/|c|.                    (8)

For example A_12=sqrt(c+1)/sqrt(c)-1 equals
1/[sqrt(c)(sqrt(c+1)+sqrt(c))], and
cA_12'=-1/[2s(c)(c+1)]. The remaining entries and derivatives
are bounded directly from |s|<=1 and |1/s|<=sqrt(1+1/a).

It follows that the generator A(x/t^2)/(2t) and its t derivative
are O_a(1/j) and O_a(1/j^2); their upper-right entries have
an additional factor 1/|c|. The ordinary local ODE estimate
therefore gives

    Z_j(x)=I+A(c)/j+E_j^ref(c),
    ||E_j^ref(c)||<=C_a/j^2,
    |(E_j^ref(c))_12|<=C_a/(|c|j^2).                  (9)

One precise way to keep the last bound is to put
B_c=diag(1/|c|,1) and apply the same ODE estimate to the
generator B_c^(-1)[A(x/t^2)/(2t)]B_c. The transformed
generator and its derivative still have the
ordinary uniform bounds in (8); undoing the similarity gives
the extra factor for the upper-right error. Apply the unweighted
estimate separately to retain the bounds for the other entries.
This pointwise device is used only for norms and does not assert
holomorphic dependence of |c|.

## 4. Conjugating by F does not lose the summability

Let Delta_j=Q_j-Z_j. By (6) and (9), its ordinary entries are
O_a(j^-2) and its upper-right entry is O_a(1/(|c|j^2)). At
t=j the diagonal parameter in (7) obeys

    1/[2sqrt(|c|+1)]<=|w(j,x)|<=1/[2sqrt(|c|)].          (10)

These are exactly the bounds (1), since w(j,x)^2=q(c).
Consequently

    D(j,x)^(-1)Delta_j D(j,x)
       =[[Delta_11,Delta_12/w],
          [w Delta_21,Delta_22]]
       =O_a(j^-2).                                   (11)

The upper-right suppression in (6) compensates for the inverse
w. Ignoring it and using only cond D=O(sqrt(|c|)) would instead
produce an erroneous loss at early cuts.

The remaining factors of F are uniformly harmless on this short
interval. Direct differentiation gives

    partial_t log w(t,x)=sqrt(x)/(t sqrt(x+t^2)),
    partial_t log (x+t^2)^(-1/4)=-t/[2(x+t^2)].

Their absolute values are at most 1/t and 1/(2t), respectively,
when Re x>0. Thus the diagonal and scalar ratios between j-2
and j are bounded by constants. Also
||exp(plus-or-minus t sigma_1/(2sqrt(x)))||<=exp(1/(2sqrt(a)))
for t<=j and Re x>=aj^2. It follows from (11) that

    S_j(x):=F(j,x)^(-1)Q_j(x)F(j-2,x)
           =I+E_j^corr(x),
    ||E_j^corr(x)||<=C_a/j^2                           (12)

uniformly whenever j is sufficiently large and Re x>=aj^2.
This is the desired summable normalized remainder.

## 5. Global products and growing initial cuts

Let J<=N have the same parity, J sufficiently large depending
only on a, and assume Re x>=aN^2. Define

    Lambda_(N,J)(x)=product_(j=J+2,J+4,...,N)lambda(x/j^2),
    W_(N,J)(x)=F(N,x)^(-1)
          [Lambda_(N,J)(x)^(-1)P_N(x)P_J(x)^(-1)]F(J,x).

The exact recurrence and (12) give the ordered product

    W_(N,J)(x)=product_(j increasing to the left) S_j(x).

All actual branch matrices are invertible in this region for
large J by the Casoratian spectral separation. Taking J large
enough that each step error is at most 1/2, and using
sum_(j=J+2,J+4,...,N)j^-2<=1/(2J), proves

    ||W_(N,J)-I||<=exp(C_a/(2J))-1=O_a(1/J),
    ||W_(N,J)^(-1)||<=exp(C_a/J),
    ||W_(N,J)^(-1)-I||=O_a(1/J).                      (13)

These estimates are uniform over the whole interval of cuts;
neither N/J nor |x|/J^2 needs to be bounded.

For x=chi N^2 with chi in a fixed compact subset K of Re chi>0,
the functions in (13) are holomorphic on a fixed larger compact
neighborhood for all sufficiently large indices. Cauchy's
formula therefore gives

    ||partial_chi^r(W_(N,J)(chi N^2)-I)||<=C_(K,r)/J,
    ||partial_chi^r(W_(N,J)(chi N^2)^(-1)-I)||
                                      <=C_(K,r)/J, r=0,1,2.   (14)

In particular any initial cuts J_N tending to infinity, with
J_N<=N and the correct parity, give a quantified global limit.
They can tend to infinity arbitrarily slowly; no condition such
as J_N>>sqrt(N) is required.

## 6. A concrete limit from each fixed initial cut

Fix J sufficiently large and let N tend to infinity through its
parity class, with x=chi N^2 and chi in a compact subset of the
right half-plane. For each fixed j, the finite resolvent and
lambda expansions as x tends to infinity give

    Q_j(x)=j^2 Gamma_j^(-1)/4+O_j(1/x),
    (Q_j(x))_12=O_j(1/x).

Moreover w(j,x)=j/(2sqrt(x))(1+O_j(1/x)), the scalar ratio
in F tends to one, and exp(j sigma_1/(2sqrt(x))) tends to I.
Thus the exact corrected step has the uniform fixed-j limit

    S_j(chi N^2) -> L_j=diag(ell_j^+,ell_j^-),

    ell_j^+ = [j^2/(4a_(j-1)a_j)]sqrt((j-2)/j),
    ell_j^- = [j^2/(4a_ja_(j+1))]sqrt(j/(j-2)).          (15)

Both numbers are positive and equal 1+O(j^-2); this follows
either directly from a_j=j/2+O(1/j) or from the uniform step
bound (12) by taking x to infinity. Their infinite products

    D_J=diag(product_(j=J+2,J+4,...)ell_j^+,
             product_(j=J+2,J+4,...)ell_j^-)             (16)

therefore converge to nonzero finite constants. The uniform
tail estimate (13), first after a fixed later cut L and then
letting L tend to infinity, proves

    W_(N,J)(chi N^2) -> D_J                            (17)

uniformly on every such compact K. This is a usual finite-head
and uniformly summable-tail argument; no limit is interchanged
with an uncontrolled product. Also D_J=I+O(1/J).

No rate in N is asserted for (17). The convergence is locally
uniform and holomorphic, so its first and second chi derivatives
also converge to zero on smaller compact domains by Cauchy's
formula. Any fixed smaller cut J>=1 can be included by splitting
off finitely many initial factors before the uniform estimates
begin. Formula (15) handles those factors and gives the same
product (16); the resulting limit remains positive diagonal.

The exact global reconstruction can now be written

    P_N(x)=Lambda_(N,J)(x) F(N,x)
                [D_J+o_K(1)]F(J,x)^(-1)P_J(x),
    x=chi N^2.                                        (18)

Thus the remaining finite initial matrix is explicit and actual,
and its intervening infinite correction is the diagonal product
(16). The two parities use their own fixed cut and product.

### An explicit evaluation of the diagonal constants

The products in (16) can also be evaluated without an infinite
product notation. Write D_J=diag(d_J^+,d_J^-). For J>=1,

    d_J^+ = sqrt(pi J/2) 2^(-J) Gamma(J+1)^2
       /[Gamma(J/2+1)^2
                    sqrt(Gamma(J+1/2)Gamma(J+3/2))],
    d_J^- = (2a_(J+1)/J)d_J^+.                         (19)

For verification, let L=J+2r be a finite upper endpoint. The
positive factors in (15) telescope to

    product_(j=J+2,J+4,...,L)ell_j^+
      =sqrt(J/L)
         [Gamma(L/2+1)/Gamma(J/2+1)]^2
         /product_(k=J+1)^L a_k.                       (20)

The last denominator equals

    [Gamma(L+1)/Gamma(J+1)]^2 2^(-(L-J))
       sqrt[Gamma(J+1/2)Gamma(J+3/2)
               /(Gamma(L+1/2)Gamma(L+3/2))].

The gamma duplication identity and Stirling's ratio formula
give

    2^L Gamma(L/2+1)^2
        sqrt(Gamma(L+1/2)Gamma(L+3/2))
       /[sqrt(L)Gamma(L+1)^2] -> sqrt(pi/2).

Substitution proves the first expression in (19). The ratio
of the finite minus and plus products is exactly
(L/J)a_(J+1)/a_(L+1), which tends to 2a_(J+1)/J and proves
the second. These are positive constants. This evaluation is
separate from, and not needed for, the uniform product argument
or its error bounds.

## 7. Scope and the next comparison

Equations (13)-(18) remove the prior obstruction from unbounded
local ratios x/j^2. They determine the global corrected orientation
from a fixed finite starting matrix, or give an O(1/J_N) error
from an arbitrary growing starting cut. The proof preserves the
anisotropic entry estimate needed when F itself is ill-conditioned.

The finite matrix P_J(x) and F(J,x) still carry explicit powers
of x; equation (18) must retain them when comparing the two
channels. The little-o term is a matrix factor in the displayed
location. It must not be converted into relative errors for
individual entries that may cancel.

This result is not a lower bound for the actual mixed-node
remainder determinant after its prescribed row deletion. That
determinant combines different x values and actual endpoint
normalizations. No claim about its primitive denominator, its
sign, or the irrationality of e+pi is made here.

No new numerical degree or root scan was used.
