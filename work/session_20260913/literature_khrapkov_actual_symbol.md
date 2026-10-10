> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Khrapkov factorization: the actual limiting symbol and its obstruction

Date: 2026-09-13. Targeted primary-source continuation by root.
This is an active research note, not an imported nonvanishing theorem.

The reviewed odd boundary limit has y=sqrt(3)cos(theta), t=(1+iy)/(1-iy),

    M(y)=[[0,1+iy],[1-iy,0]],       M(y)^2=(1+y^2)I,
    a0=M/2,       K=M/(1-iy),      E=exp K,       a=a0 E.

Since K^2=tI, write c(t)=cosh(sqrt(t)) and
s(t)=sinh(sqrt(t))/sqrt(t), interpreted by entire power series. Then

    a(y)=(1+iy)s(t)I/2 + c(t)M(y)/2,
    det a(y)=-(1+y^2)/4.

These identities are exact. Thus the matrix is in a scalar-plus-
trace-zero-polynomial algebra whose square is scalar. Pointwise
commutation does not imply commutation after half-line compression.

## Primary literature checked

Yuri Antipov, "The Baker-Akhiezer function and factorization of the
Chebotarev-Khrapkov matrix", arXiv:1401.1253v2 (2014):
https://arxiv.org/pdf/1401.1253
The introduction and section 2 reduce this polynomial matrix class
to scalar factorization on the square-root surface. The paper specifies
contour, regularity, branch-point and growth hypotheses; the genus and
the removal of unwanted singularities matter. This provides a possible
factorization method, not automatic canonical partial indices for the
present Toeplitz operator.

Anastasia Kisil, "Stability analysis of matrix Wiener-Hopf factorisation
of Daniele-Khrapkov class and reliable approximate factorisation",
arXiv:1504.01108 (2015): https://arxiv.org/pdf/1504.01108
The partial-index discussion and section 4 distinguish factorization
from stable canonical factorization. No stability estimate from that
paper has been imported. In particular the hyperbolic representation
must be checked with the normalization theta=(2 Delta)^(-1)
log((1+Delta f)/(1-Delta f)) when the argument is Delta theta.
One must not copy a logarithm normalization without substituting it
back into the matrix identity.

## The circle change of variable increases the relevant algebraic degree

For zeta on the unit circle, y=(sqrt(3)/2)(zeta+zeta^(-1)). Put

    Q(zeta)=zeta M(y(zeta)).

This is a polynomial trace-zero matrix of degree two, and

    Q(zeta)^2=[(3/4)zeta^4+(5/2)zeta^2+3/4] I
              =(3/4)(zeta^2+3)(zeta^2+1/3) I.

The four distinct branch points are +/-i sqrt(3) and +/-i/sqrt(3).
The square-root surface in this circle variable has genus one. Thus
the fact that M(y)^2 is quadratic in y does not directly turn the
actual circle factorization into the genus-zero case. Working in y
instead folds the circle onto an interval and changes the boundary
problem; that change must be carried through explicitly.

The determinant is nonzero on the circle and has index zero, but this
controls only the sum of partial indices. It does not prove that the
two small limiting boundary determinants are nonzero. Likewise,
constant-matrix accretivity after a guessed similarity is not available
merely from the eigenvalue formula.

The most useful next step is a rigorous certificate for the explicit
fixed half-line boundary matrices, now being pursued independently.
An exact genus-one factorization remains an alternative if that
certificate fails or if a symbolic value of the limit is desired.
